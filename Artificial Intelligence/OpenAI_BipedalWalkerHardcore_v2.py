import time, math, random, bisect, copy
import gym
import numpy as np



class NeuralNet : 
    def __init__(self, nodeCount, loadFile):     
        self.fitness = 0.0
        self.nodeCount = nodeCount
        self.weights = []
        self.biases = []

        if loadFile:
            self.nodeCount, self.weights, self.biases = loadWeights()
        else:
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
            output = np.maximum(output, 0)
        return output


class Population :
    def __init__(self, populationCount, mutationRate, nodeCount, loadFile=False):
        self.nodeCount = nodeCount
        self.popCount = populationCount
        self.m_rate = mutationRate
        self.population = [ NeuralNet(nodeCount, loadFile) for i in range(populationCount)]


    def createChild(self, nn1, nn2):
        
        child = NeuralNet(self.nodeCount, False)
        for i in range(len(child.weights)):
            for j in range(len(child.weights[i])):
                for k in range(len(child.weights[i][j])):
                    if random.random() > self.m_rate:
                        if random.random() < nn1.fitness / (nn1.fitness+nn2.fitness):
                            child.weights[i][j][k] = nn1.weights[i][j][k]
                        else :
                            child.weights[i][j][k] = nn2.weights[i][j][k]
                        

        for i in range(len(child.biases)):
            for j in range(len(child.biases[i])):
                if random.random() > self.m_rate:
                    if random.random() < nn1.fitness / (nn1.fitness+nn2.fitness):
                        child.biases[i][j] = nn1.biases[i][j]
                    else:
                        child.biases[i][j] = nn2.biases[i][j]

        return child


    def createNewGeneration(self):    
        nextGen = []
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        for i in range(self.popCount):
            if random.random() < float(self.popCount-i)/self.popCount:
                nextGen.append(copy.deepcopy(self.population[i]));

        fitnessSum = [0]
        minFit = min([i.fitness for i in nextGen])
        for i in range(len(nextGen)):
            fitnessSum.append(fitnessSum[i]+(nextGen[i].fitness-minFit)**4)
        

        while(len(nextGen) < self.popCount):
            r1 = random.uniform(0, fitnessSum[len(fitnessSum)-1] )
            r2 = random.uniform(0, fitnessSum[len(fitnessSum)-1] )
            i1 = bisect.bisect_left(fitnessSum, r1)
            i2 = bisect.bisect_left(fitnessSum, r2)
            if 0 <= i1 < len(nextGen) and 0 <= i2 < len(nextGen) :
                nextGen.append( self.createChild(nextGen[i1], nextGen[i2]) )
            else :
                print("Index Error ");
                print("Sum Array =",fitnessSum)
                print("Randoms = ", r1, r2)
                print("Indices = ", i1, i2)
        self.population.clear()
        self.population = nextGen


def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

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
        res.append( mapRange(aVal[i], aMin[i], aMax[i], -1, 1) )
    return res

def scaleArray(aVal, aMin, aMax):   
    res = []
    for i in range(len(aVal)):
        res.append( mapRange(aVal[i], -1, 1, aMin[i], aMax[i]) )
    return res    

def replayBestBots(bestNeuralNets, steps, sleep):  
    choice = input("Do you want to watch the replay ?[Y/N] : ")
    if choice=='Y' or choice=='y':
        for i in range(len(bestNeuralNets)):
            if (i+1)%steps == 0 :
                observation = env.reset()
                totalReward = 0
                for step in range(MAX_STEPS):
                    env.render()
                    time.sleep(sleep)
                    action = bestNeuralNets[i].getOutput(observation)
                    observation, reward, done, info = env.step(action)
                    totalReward += reward
                    if done:
                        break
                print("Generation %3d | Expected Fitness of %4d | Actual Fitness = %4d" % (i+1, bestNeuralNets[i].fitness, totalReward))


def recordBestBots(bestNeuralNets):  
    print("\n Recording Best Bots ")
    print("---------------------")
    env.monitor.start('Artificial Intelligence/'+GAME, force=True)
    observation = env.reset()
    for i in range(len(bestNeuralNets)):
        totalReward = 0
        for step in range(MAX_STEPS):
            env.render()
            action = bestNeuralNets[i].getOutput(observation)
            observation, reward, done, info = env.step(action)
            totalReward += reward
            if done:
                observation = env.reset()
                break
        print("Generation %3d | Expected Fitness of %4d | Actual Fitness = %4d" % (i+1, bestNeuralNets[i].fitness, totalReward))
    env.monitor.close()




def loadWeights():
    
    nodeCount = []
    weights = []
    biases = []
    try :
        f = open('Artificial Intelligence/'+GAME+"/"+GAME+".txt", 'r')
    except FileNotFoundError:
        print("File Not Found. Initializing random values")
        nodeCount = node_per_layer
        for i in range(len(nodeCount) - 1):
            weights.append( np.random.uniform(low=-1, high=1, size=(nodeCount[i], nodeCount[i+1])).tolist() )
            biases.append( np.random.uniform(low=-1, high=1, size=(nodeCount[i+1])).tolist())
        return nodeCount, weights, biases


    print("Type : ", type(f))
    
    f.readline()
    nodeCount = [int(i) for i in f.readline().split()]

    f.readline()
    for i in range(len(nodeCount) - 1):
        weights.append([])
        for j in range(nodeCount[i]):
            weights[i].append([float(i) for i in f.readline().split()])

    f.readline()
    for i in range(len(nodeCount) - 1):
        biases.append([float(i) for i in f.readline().split()])
    f.close()

    return nodeCount, weights, biases



def saveWeights(best):
    
    f = open('Artificial Intelligence/'+GAME+"/"+GAME+".txt", 'w')

    print("Node Count : ", file=f)
    for i in range(len(best.nodeCount)):
        print("%d " % best.nodeCount[i], file=f, end="");
    print("", file=f)

    print("Weights : ", file=f)
    for i in range(len(best.weights)):
            for j in range(len(best.weights[i])):
                for k in range(len(best.weights[i][j])):
                    print("%+.2f " % best.weights[i][j][k], file=f, end="")
                print("", file=f)

    print("Biases : ", file=f)
    for i in range(len(best.biases)):
            for j in range(len(best.biases[i])):
                print("%+.2f " % best.biases[i][j], file=f, end="")
            print("", file=f)

    f.close()


def uploadSimulation():
    API_KEY = open('/home/dollarakshay/Documents/API Keys/Open AI Key.txt', 'r').read().rstrip()
    gym.upload('Artificial Intelligence/'+GAME, api_key=API_KEY)
    


GAME = 'BipedalWalkerHardcore-v2'
env = gym.make(GAME)

MAX_STEPS = env.spec.timestep_limit
MAX_GENERATIONS = 5
POPULATION_COUNT = 10
MUTATION_RATE = 0.01

in_dimen = env.observation_space.shape[0]
out_dimen = env.action_space.shape[0]
obsMin = env.observation_space.low
obsMax = env.observation_space.high
actionMin = env.action_space.low
actionMax = env.action_space.high
node_per_layer = [in_dimen, 13, 8, 13, out_dimen]

pop = Population(POPULATION_COUNT, MUTATION_RATE, node_per_layer, False)
bestNeuralNets = []

print("\nGENERAL\n--------------------------------")
print("Max Steps :", MAX_STEPS)
print("\nOBSERVATION\n--------------------------------")
print("Shape :", in_dimen, " High :", obsMax, " Low :", obsMin)
print("\nACTION\n--------------------------------")
print("Shape :", out_dimen, " | High :", actionMax, " | Low :", actionMin,"\n")

try :
    for gen in range(MAX_GENERATIONS):
        genAvgFit = 0.0
        minFit =  1000000
        maxFit = -1000000
        maxNeuralNet = None
        for cr, nn in enumerate(pop.population):
            observation = env.reset()
            totalReward = 0
            for step in range(MAX_STEPS):
                if cr==-1:
                    env.render()
                action = nn.getOutput(observation)
                observation, reward, done, info = env.step(action)
                totalReward += reward
                if done:
                    break

            nn.fitness = totalReward
            minFit = min(minFit, nn.fitness)
            genAvgFit += nn.fitness
            if nn.fitness > maxFit :
                maxFit = nn.fitness
                maxNeuralNet = copy.deepcopy(nn);

        bestNeuralNets.append(maxNeuralNet)
        genAvgFit/=pop.popCount
        print("Generation : %3d  |  Min : %5.0f  |  Avg : %5.0f  |  Max : %5.0f  " % (gen+1, minFit, genAvgFit, maxFit) )
        pop.createNewGeneration()

    #recordBestBots(bestNeuralNets)
    #uploadSimulation()
    #replayBestBots(bestNeuralNets, max(1, int(math.ceil(MAX_GENERATIONS/10.0))), 0)

except KeyboardInterrupt:
    print("\nKeyboard Interrupt")
except:
    print("\nUnknown Exception")
finally :
    if len(bestNeuralNets) > 1:
        print("\nSaving Weights to file")
        saveWeights(bestNeuralNets[-1])
    else:
        print("No weights to save")
    print("\nQuitting")





