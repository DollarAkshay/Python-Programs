import random
import math
import numpy as np

class GameState():    
    def __init__(self):
        self.pos = 5
        self.player1Cash = cashStates-1
        self.player2Cash = cashStates-1
        self.drawFavor = 1
    
    def reset(self):
        self.pos = 5
        self.player1Cash = op_features-1
        self.player2Cash = op_features-1
        self.drawFavor = 1
    
    def getState(self):     
        state = (self.pos, self.player1Cash, self.player2Cash, self.drawFavor)

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
# Update Table
def updateQTable(prevState, prevAction, reward, curState):
    q_table[prevState][prevAction] += LEARNING_RATE*( reward + DISCOUNT*max(q_table[curState]) -  q_table[prevState][prevAction])
#
# Update Table
def getAction(curState):
    if random.random() < EPSILON:
        return env.action_space.sample()
    else:
        return np.argmax(q_table[curState])

#
# Main
EPISODES = 10000
EPSILON = 0.1
DISCOUNT = 0.9
LEARNING_RATE = 1
REWARD = 100

boardStates = 11
cashStates = 101
drawStates = 2
q_table = np.zeros((boardStates, op_features, op_features, drawStates))


game = GameState()


winarray = []

for episode in range(EPISODES):
    print("\n\nGame ", episode)
    
    game.reset()
    totalLoss = 0
    for turn in range(1000):
        #print("Turn :", turn)
        curState = game.getState()
        
        action1 = int(game.player1Cash/game.pos)
        prevState = curState
        done, rewards = game.step(action1, action2)
        curState = game.getState()

        if done:
            if max(rewards)==REWARD :
                winarray.append( 1 if rewards[1]==REWARD else 0 )
                if len(winarray)>100:
                    winarray.pop(0)
            break
        
    print(" Player 2 wins: "+str(sum(winarray))+" / 100")
    EPSILON-=0.1/1000

