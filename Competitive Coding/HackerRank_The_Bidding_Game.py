import random
import math
import numpy as np
import tensorflow as tf

class GameState():    
    def __init__(self):
        self.pos = 5
        self.player1Cash = op_features-1
        self.player2Cash = op_features-1
        self.drawFavor = 1
    
    def reset(self):
        self.pos = 5
        self.player1Cash = op_features-1
        self.player2Cash = op_features-1
        self.drawFavor = 1
    
    def getState(self):     
        state = np.array([])
        player1input = [(0 if i>self.player1Cash else 1) for i in range(op_features)]
        player2input = [(0 if i>self.player2Cash else 1) for i in range(op_features)]
        state = np.append(state, player1input)
        state = np.append(state, player2input)

        board = np.zeros(11)
        board[self.pos] = 1
        state = np.append(state, board)
        if self.drawFavor == 1:
            state = np.append(state, 0)
        else:
            state = np.append(state, 1)

        return np.reshape(state, (1, ip_features))

    def step(self, bet1, bet2):

        if (bet1 > self.player1Cash) or (bet1==0 and self.player1Cash>0):
            return (True, [-REWARD, REWARD])   

        if (bet2 > self.player2Cash) or (bet2==0 and self.player2Cash>0):
            return (True, [REWARD, -REWARD])

        if bet1 > bet2 :
            self.pos-=1
            self.player1Cash -= bet1
        elif bet2 > bet1:
            self.pos+=1
            self.player2Cash -= bet2
        elif bet1==bet2 and self.drawFavor == 1:
            self.pos-=1
            self.player1Cash -= bet1
            self.drawFavor = 2
        else:
            self.pos+=1
            self.player2Cash -= bet2
            self.drawFavor = 1

        if self.pos==0:
            return (True, [REWARD, -REWARD])
        elif self.pos==10:
            return (True, [-REWARD, REWARD])
        elif self.player1Cash==0 and self.player2Cash==0:
            return (True, [0, 0])
        else:
            return (False, [0, 0])
#
#
# Player 2 Neural Network
def neural_network():
    
    nodeCount = [150, 120]

    weights = {
        'hidden1': tf.Variable( tf.random_normal( [ip_features, nodeCount[0]] )) ,
        'hidden2': tf.Variable( tf.random_normal( [nodeCount[0], nodeCount[1]] )),
        'out'    : tf.Variable( tf.random_normal( [nodeCount[1], op_features] ))
    }

    biases = {
        'hidden1': tf.Variable( tf.random_normal( [nodeCount[0]] )) ,
        'hidden2': tf.Variable( tf.random_normal( [nodeCount[1]] )),
        'out'    : tf.Variable( tf.random_normal( [op_features] ))
    }

    hidden1 = tf.add( tf.matmul(ip_placeholder, weights['hidden1']), biases['hidden1'])
    hidden1 = tf.nn.relu(hidden1)

    hidden2 = tf.add( tf.matmul(hidden1, weights['hidden2']), biases['hidden2'])
    hidden2 = tf.nn.sigmoid(hidden2)

    output = tf.add( tf.matmul(hidden2, weights['out']), biases['out'])
    output = tf.nn.sigmoid(output)
    
    return output

#
# Main
EPISODES = 100000
EPSILON = 0.1
DISCOUNT = 0.9
LEARNING_RATE = 1
REWARD = 1

op_features = 20
ip_features = op_features*2+11+1
ip_placeholder = tf.placeholder('float', [1, ip_features])
op_placeholder = tf.placeholder('float', [1, op_features])

game = GameState()

output_prediction = neural_network()
output_action = tf.argmax(output_prediction, 1)[0]
output_target = tf.placeholder('float', [1, op_features])
loss = tf.reduce_sum(tf.square(output_target - output_prediction))
trainer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
optimizer = trainer.minimize(loss)

np.set_printoptions(precision=3, suppress=True, linewidth=120)

with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())
    winarray = []

    for episode in range(EPISODES):
        print("\n\nGame ", episode)
        
        game.reset()
        totalLoss = 0
        for turn in range(1000):
            #print("Turn :", turn)
            curState = game.getState()
            
            
            action1 = int(game.player1Cash/game.pos)
            if np.random.rand(1) < 0.2  and game.player1Cash > 0: 
                action1 = random.randint(1, game.player1Cash)

            action2, actualQ = sess.run([output_action, output_prediction], feed_dict={ip_placeholder: curState })
            if np.random.rand(1) < EPSILON  and game.player2Cash > 0: 
                action2 = random.randint(1, game.player2Cash)

            prevState = curState
            done, rewards = game.step(action1, action2)
            curState = game.getState()


            maxQCurState = np.max(sess.run(output_prediction, feed_dict={ip_placeholder: curState}))



            targetQ = actualQ
            targetQ[0, action2] = LEARNING_RATE*(rewards[1] + DISCOUNT*maxQCurState - targetQ[0, action2])

            _, l = sess.run([optimizer, loss],feed_dict={ip_placeholder: prevState , output_target: targetQ})
            totalLoss+=l

            if done:
                if max(rewards)==REWARD :
                    winarray.append( 1 if rewards[1]==REWARD else 0 )
                    if len(winarray)>100:
                        winarray.pop(0)
                break
        
        print("Total Loss for Player 2 :", totalLoss)
        print(" Player 2 wins: "+str(sum(winarray))+" / 100")
        EPSILON-=0.1/1000

