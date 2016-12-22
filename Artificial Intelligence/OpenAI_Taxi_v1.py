import time, random, math
import numpy as np
import gym

def uploadSimulation():
    API_KEY = open('/home/dollarakshay/Documents/API Keys/Open AI Key.txt', 'r').read().rstrip()
    gym.upload('Artificial Intelligence/'+GAME, api_key=API_KEY)


def updateQTable(prevState, prevAction, reward, curState):
    q_table[prevState][prevAction] += LEARNING_RATE*( reward + DISCOUNT*max(q_table[curState]) -  q_table[prevState][prevAction])


def getAction(curState):
    if random.random() < EPSILON:
        return env.action_space.sample()
    else:
        return np.argmax(q_table[curState])


GAME = 'Taxi-v1'
env = gym.make(GAME)
env.seed(19950604)

RECORD = None
MAX_EPISODES = 1001
MAX_STEPS = env.spec.timestep_limit     # 100 for FrozenLake v0
EPSILON = 0
DISCOUNT = 0.99
LEARNING_RATE = 0.5

in_dimen = env.observation_space.n
out_dimen = env.action_space.n
obsMin = 0
obsMax = env.observation_space.n
actionMin = 0
actionMax = env.action_space.n
q_table = np.zeros((in_dimen, out_dimen))

env.monitor.start('Artificial Intelligence/'+GAME, force=True, video_callable=RECORD)

print("\nObservation\n--------------------------------")
print("Shape :", in_dimen, " | High :", obsMax, " | Low :", obsMin)
print("\nAction\n--------------------------------")
print("Shape :", out_dimen, " | High :", actionMax, " | Low :", actionMin,"\n")

totalreward = 0

for episode in range(MAX_EPISODES):
    
    if episode%100 == 0 :
        print("Episode =", episode, " |  Avg Reward =", totalreward/100)
        totalreward = 0

    EPSILON -= 0.001
    curState = env.reset()
    for step in range(MAX_STEPS):
        #env.render()
        prevState = curState
        action = getAction(curState)
        curState, reward, done, info = env.step(action)
        totalreward += reward
        updateQTable(prevState, action, reward, curState)
        if done :
            break


env.monitor.close()

uploadSimulation()


