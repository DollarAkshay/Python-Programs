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
            state = np.append(state, -1)
        else:
            state = np.append(state, 1)

        return np.reshape(state, (1, ip_features))

    def step(self, bet1, bet2):     
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
            return (True, [100, -100])
        elif self.pos==10:
            return (True, [-100, 100])
        elif self.player1Cash==0 and self.player2Cash==0:
            return (True, [5-self.pos, self.pos-5])
        else:
            return (False, [0, 0])
#
# Player 1 Neural Network
def neural_network1():
    
    nodeCount = [150, 100]

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
    hidden1 = tf.nn.sigmoid(hidden1)

    hidden2 = tf.add( tf.matmul(hidden1, weights['hidden2']), biases['hidden2'])
    hidden2 = tf.nn.sigmoid(hidden2)

    output = tf.add( tf.matmul(hidden2, weights['out']), biases['out'])
    output = tf.nn.sigmoid(output)
    output = tf.matmul(output, limit_placeholder)
    
    return output
#
# Player 2 Neural Network
def neural_network2():
    
    nodeCount = [175, 80]

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
    hidden1 = tf.nn.sigmoid(hidden1)

    hidden2 = tf.add( tf.matmul(hidden1, weights['hidden2']), biases['hidden2'])
    hidden2 = tf.nn.sigmoid(hidden2)

    output = tf.add( tf.matmul(hidden2, weights['out']), biases['out'])
    output = tf.nn.sigmoid(output)
    output = tf.matmul(output, limit_placeholder)
    
    return output
#
# Calc Bet Limit
def getBetLimit(state, player):
    playerCash = 0
    for i in range(op_features):
        if state[0][(player-1)*op_features +i] > 0:
            playerCash = i
    
    res = np.eye(op_features)
    for i in range(op_features):
        if i > playerCash:
            res[i][i] = 0

    if playerCash > 0:
        res[0][0] = 0
    return res

#
# Main
EPISODES = 1000
EPSILON = 0.1
DISCOUNT = 0.99


op_features = 101
ip_features = op_features*2+11+1
ip_placeholder = tf.placeholder('float', [1, ip_features])
op_placeholder = tf.placeholder('float', [1, op_features])
limit_placeholder = tf.placeholder('float', [op_features, op_features])

game = GameState()

output_prediction1 = neural_network1()
output_action1 = tf.argmax(output_prediction1, 1)[0]
output_target1 = tf.placeholder('float', [1, op_features])
loss1 = tf.reduce_sum(tf.square(output_target1 - output_prediction1))
trainer1 = tf.train.AdamOptimizer(learning_rate=0.01)
optimizer1 = trainer1.minimize(loss1)

output_prediction2 = neural_network2()
output_action2 = tf.argmax(output_prediction2, 1)[0]
output_target2 = tf.placeholder('float', [1, op_features])
loss2 = tf.reduce_sum(tf.square(output_target2 - output_prediction2))
trainer2 = tf.train.AdamOptimizer(learning_rate=0.01)
optimizer2 = trainer2.minimize(loss2)

with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())
    for episode in range(EPISODES):
        print("\n\nGame ", episode)
        game.reset()
        
        totalLoss1 = 0
        totalLoss2 = 0
        for turn in range(1000):
            print("Turn :", turn)
            curState = game.getState()
            for i in range(11):
                print("#", end=" ") if i == game.pos else print("_", end=" ")    
            print("")
            
            betlimit1 = getBetLimit(curState, 1)
            action1, actualQ1 = sess.run([output_action1, output_prediction1], feed_dict={ip_placeholder: curState, limit_placeholder: betlimit1 })
            if np.random.rand(1) < EPSILON and game.player1Cash > 0:
                print("Player 1 took random action")
                action1 = random.randint(1, game.player1Cash)
            print("Player 1 bet "+str(action1)+"/"+str(game.player1Cash))

            betlimit2 = getBetLimit(curState, 2)
            action2, actualQ2 = sess.run([output_action2, output_prediction2], feed_dict={ip_placeholder: curState, limit_placeholder: betlimit2 })
            if np.random.rand(1) < EPSILON  and game.player2Cash > 0: 
                print("Player 2 took random action")
                action2 = random.randint(1, game.player2Cash)
            print("Player 2 bet "+str(action2)+"/"+str(game.player2Cash))


            prevState = curState
            done, rewards = game.step(action1, action2)
            curState = game.getState()


            betlimit1 = getBetLimit(curState, 1)
            betlimit2 = getBetLimit(curState, 2)

            maxQ1CurState = np.max(sess.run(output_prediction1, feed_dict={ip_placeholder: curState, limit_placeholder: betlimit1 }))
            maxQ2CurState = np.max(sess.run(output_prediction2, feed_dict={ip_placeholder: curState, limit_placeholder: betlimit2 }))

            betlimit1 = getBetLimit(prevState, 1)
            betlimit2 = getBetLimit(prevState, 2)

            targetQ1 = actualQ1
            targetQ1[0, action1] = rewards[0] + DISCOUNT*maxQ1CurState

            targetQ2 = actualQ2
            targetQ2[0, action2] = rewards[1] + DISCOUNT*maxQ2CurState

            _, l1 = sess.run([optimizer1, loss1],feed_dict={ip_placeholder: prevState , output_target1: targetQ1, limit_placeholder: betlimit1})
            totalLoss1+=l1
            _, l2 = sess.run([optimizer2, loss2],feed_dict={ip_placeholder: prevState , output_target2: targetQ2, limit_placeholder: betlimit2})
            totalLoss2+=l2

            if True:
                input()

            if done:
                if max(rewards)==100:
                    print(" ~~~ PLAYER", np.argmax(rewards)+1,"WINS ~~~")
                break
        
        print("Total Loss for Player 1 :", totalLoss1)
        print("Total Loss for Player 2 :", totalLoss2)
        EPSILON-=0.1/100

