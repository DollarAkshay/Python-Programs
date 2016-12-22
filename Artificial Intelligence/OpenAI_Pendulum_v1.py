import time, math, random, bisect
import gym
import numpy as np



class NeuralNet : 
    def __init__(self, nodeCount):     
        self.fitness = 0
        self.nodeCount = nodeCount
        self.weights = []
        self.biases = []
        for i in range(len(nodeCount) - 1):
            self.weights.append( np.random.uniform(low=-1, high=1, size=(nodeCount[i], nodeCount[i+1])).tolist() )
            self.biases.append( np.random.uniform(low=-1, high=1, size=(nodeCount[i+1])).tolist())


    def printWeightsandBiases(self):
        
        print("--------------------------------")
        print("Weights :\n[", end="")
        for i in range(len(self.weights)):
            print("\n [ ", end="")
            for j in range(len(self.weights[i])):
                if j!=0:
                    print("\n   ", end="")
                print("[", end="")
                for k in range(len(self.weights[i][j])):
                    print(" %5.2f," % (self.weights[i][j][k]), end="")
                print("\b],", end="")
            print("\b ],")
        print("\n]")

        print("\nBiases :\n[", end="")
        for i in range(len(self.biases)):
            print("\n [ ", end="")
            for j in range(len(self.biases[i])):
                    print(" %5.2f," % (self.biases[i][j]), end="")
            print("\b],", end="")
        print("\b \n]\n--------------------------------\n")
  
    def getOutput(self, input):
        output = input
        for i in range(len(self.nodeCount)-1):
            output = np.reshape( np.matmul(output, self.weights[i]) + self.biases[i], (self.nodeCount[i+1]))
        return output


class Population :
    def __init__(self, populationCount, mutationRate, nodeCount):
        self.nodeCount = nodeCount
        self.popCount = populationCount
        self.m_rate = mutationRate
        self.population = [ NeuralNet(nodeCount) for i in range(populationCount)]


    def createChild(self, nn1, nn2):
        
        child = NeuralNet(self.nodeCount)

        for i in range(len(child.weights)):
            for j in range(len(child.weights[i])):
                for k in range(len(child.weights[i][j])):
                    if random.random() > self.m_rate:
                        child.weights[i][j][k] = (nn1.weights[i][j][k] + nn2.weights[i][j][k])/2.0

        for i in range(len(child.biases)):
            for j in range(len(child.biases[i])):
                if random.random() > self.m_rate:
                    child.biases[i][j] = (nn1.biases[i][j] + nn2.biases[i][j])/2.0

        return child


    def createNewGeneration(self):       
        nextGen = []
        fitnessSum = [0]
        for i in range(len(self.population)):
            fitnessSum.append(fitnessSum[i]+self.population[i].fitness**3)
        
        while(len(nextGen) < self.popCount):
            r1 = random.uniform(0, fitnessSum[len(fitnessSum)-1] )
            r2 = random.uniform(0, fitnessSum[len(fitnessSum)-1] )
            nn1 = self.population[bisect.bisect_right(fitnessSum, r1)-1]
            nn2 = self.population[bisect.bisect_right(fitnessSum, r2)-1]
            nextGen.append( self.createChild(nn1, nn2) )
        self.population.clear()
        self.population = nextGen


def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def replayBestBots(bestNeuralNets, steps, sleep):  
    for i in range(len(bestNeuralNets)):
        if i%steps == 0 :
            observation = env.reset()
            prevObservation = observation
            print("Generation %3d had a best fitness of %4d" % (i, bestNeuralNets[i].fitness))
            for step in range(MAX_STEPS):
                env.render()
                time.sleep(sleep)
                observation = normalizeArray( observation, obsMin, obsMax)
                prevObservation = normalizeArray( prevObservation, obsMin, obsMax)
                action = bestNeuralNets[i].getOutput(observation + prevObservation)
                prevObservation = observation
                observation, reward, done, info = env.step(action)
                if done:
                    break
            
def uploadSimulation():
    API_KEY = open('/home/dollarakshay/Documents/API Keys/Open AI Key.txt', 'r').read().rstrip()
    gym.upload('Artificial Intelligence/'+GAME, api_key=API_KEY)




def mapRange(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.

    return rightMin + (valueScaled * rightSpan)

def normalizeArray(aVal, aMin, aMax): 
    res = []
    for i in range(len(aVal)):
        res.append( mapRange(aVal[i], aMin[i], aMax[i], 0, 1) )
    return res

def scaleArray(aVal, aMin, aMax): 
    res = []
    for i in range(len(aVal)):
        res.append( mapRange(aVal[i], 0, 1, aMin[i], aMax[i]) )
    return res


RECORD = False
MAX_STEPS = 100
MIN_REWARD = -16
MAX_REWARD = 0
MAX_GENERATIONS = 20
POPULATION_COUNT = 100
MUTATION_RATE = 0.5

env = gym.make('Pendulum-v0')
env.monitor.start('Artificial Intelligence/Pendulum v1', force=True, video_callable=RECORD )

observation = env.reset()
prevObservation = observation
in_dimen = env.observation_space.shape[0]*2
out_dimen = env.action_space.shape[0]
obsMin = env.observation_space.low
obsMax = env.observation_space.high
actionMin = env.action_space.low
actionMax = env.action_space.high
pop = Population(POPULATION_COUNT, MUTATION_RATE, [in_dimen, 8, 4, out_dimen])
bestNeuralNets = []

print("\nObservation\n--------------------------------")
print("Shape :", in_dimen, " | High :", obsMax, " | Low :", obsMin)
print("\nAction\n--------------------------------")
print("Shape :", out_dimen, " | High :", actionMax, " | Low :", actionMin,"\n")


for gen in range(MAX_GENERATIONS):
    genAvgFit = 0.0
    maxFit = 0.0
    maxNeuralNet = None
    for nn in pop.population:
        totalReward = 0
        for step in range(MAX_STEPS):
            env.render()
            observation = normalizeArray( observation, obsMin, obsMax)
            prevObservation = normalizeArray( prevObservation, obsMin, obsMax)
            
            action = scaleArray(nn.getOutput(observation + prevObservation), actionMin, actionMax);
            prevObservation = observation
            observation, reward, done, info = env.step(action)
            totalReward += mapRange(reward, MIN_REWARD, MAX_REWARD, 0 , 1)
            if done:
                observation = env.reset()
                break
        nn.fitness = 100*totalReward/MAX_STEPS
        genAvgFit += nn.fitness
        if nn.fitness > maxFit :
            maxFit = nn.fitness
            maxNeuralNet = nn

    bestNeuralNets.append(maxNeuralNet)
    genAvgFit/=pop.popCount
    print("Generation : %3d |  Avg Fitness : %4.0f  |  Max Fitness : %4.0f  " % (gen+1, genAvgFit, maxFit) )
    pop.createNewGeneration()
        
env.monitor.close()

uploadSimulation()


choice = input("Do you want to watch the replay ?[Y/N] : ")
if choice=='Y' or choice=='y':
    replayBestBots(bestNeuralNets, int(math.ceil(MAX_GENERATIONS/10.0)), 0.0625)


