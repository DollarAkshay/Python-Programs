import time, random, math
import gym
import numpy as np
import tensorflow as tf


def neural_network():
    
    weights = {
        'hidden1': tf.Variable( tf.random_normal( [ip_features, nodeCount[0]] )) ,
        #'hidden2': tf.Variable( tf.random_normal( [nodeCount[0], nodeCount[1]] )),
        'out'    : tf.Variable( tf.random_normal( [nodeCount[0], op_features] ))
    }

    biases = {
        'hidden1': tf.Variable( tf.random_normal( [nodeCount[0]] )) ,
        #'hidden2': tf.Variable( tf.random_normal( [nodeCount[1]] )),
        'out'    : tf.Variable( tf.random_normal( [op_features] ))
    }

    hidden1 = tf.add( tf.matmul(ip_placeholder, weights['hidden1']), biases['hidden1'])
    hidden1 = tf.nn.relu(hidden1)

    #hidden2 = tf.add( tf.matmul(hidden1, weights['hidden2']), biases['hidden2'])
    #hidden2 = tf.nn.relu(hidden2)

    output = tf.add( tf.matmul(hidden1, weights['out']), biases['out'])

    return output

def uploadSimulation():
    API_KEY = open('/home/dollarakshay/Documents/API Keys/Open AI Key.txt', 'r').read().rstrip()
    gym.upload('Artificial Intelligence/'+GAME, api_key=API_KEY)

    


GAME = 'MountainCar-v0'
env = gym.make(GAME)

RECORD = None
MAX_EPISODES = 10001
MAX_STEPS = env.spec.timestep_limit     # 100 for FrozenLake v0
EPSILON = 0.1
DISCOUNT = 0.99
LEARNING_RATE = 0.1


ip_features = env.observation_space.shape[0]
op_features = env.action_space.n
obsMin = env.observation_space.low
obsMax = env.observation_space.high
actionMin = 0
actionMax = env.action_space.n - 1 

nodeCount = [4]
ip_placeholder = tf.placeholder('float', [1, ip_features])
op_placeholder = tf.placeholder('float', [1, op_features])

print("\nGENERAL\n--------------------------------")
print("Max Steps :", MAX_STEPS)
print("\nOBSERVATION\n--------------------------------")
print("Shape :", ip_features, " High :", obsMax, " Low :", obsMin)
print("\nACTION\n--------------------------------")
print("Shape :", op_features, " | High :", actionMax, " | Low :", actionMin,"\n")


#env.monitor.start('Artificial Intelligence/'+GAME, force=True, video_callable=RECORD)


output_prediction = neural_network()
output_action = tf.argmax(output_prediction, 1)[0]
output_target = tf.placeholder('float', [1, op_features])
loss = tf.reduce_sum(tf.square(output_target - output_prediction))
trainer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
optimizer = trainer.minimize(loss)

with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())
    for episode in range(MAX_EPISODES):
        curState = env.reset()
        totalReward = 0
        EPSILON = 1./((episode/50) + 10)
        for step in range(MAX_STEPS):
            if episode%100 == 0:
                env.render()
            
            action, actualQ = sess.run([output_action, output_prediction], feed_dict={ip_placeholder: np.reshape(curState, [1, 2]) })
            if np.random.rand(1) < EPSILON:
                action = env.action_space.sample()

            curState, reward, done, info = env.step(action)
            totalReward += reward
            maxQCurState = np.max(sess.run(output_prediction, feed_dict={ip_placeholder: np.reshape(curState, [1, 2]) }))
            targetQ = actualQ
            targetQ[0, action] = reward + DISCOUNT*maxQCurState

            _, l = sess.run([optimizer, loss],feed_dict={ip_placeholder: np.reshape(curState, [1, 2]) , output_target: targetQ})
            if done :
                
                break
        print("Episode %d wit a reward of %d" % (episode, totalReward))


#env.monitor.close()

uploadSimulation()












