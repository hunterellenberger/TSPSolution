from tspUtil import get_coordinates, calc_distance
from random import shuffle, randint

#initialization of variables to be used throughout program
tspFile = open("Random100.tsp", "r")
coordinates = {}    #holds nodes and their coordinates

#calculates distance of a path
def path_distance(path, nodeAndDistance):
    totalLength = 0
    for i in range(0, len(path)):
        print(i)
        if i == len(path) - 1:
            totalLength += calc_distance(nodeAndDistance[path[i]][0], nodeAndDistance[path[i]][1], nodeAndDistance[path[-1]][0], nodeAndDistance[path[-1]][1])
            return totalLength
        else:
            totalLength += calc_distance(nodeAndDistance[path[i]][0], nodeAndDistance[path[i]][1], nodeAndDistance[path[i + 1]][0], nodeAndDistance[path[i + 1]][1])
    return totalLength

#makes original generation of paths
def make_paths(numberOfPaths, numberOfNodes):
    initialPaths = []
    for i in range(0, numberOfPaths):
        randomPath = list(range(1, numberOfNodes + 1))
        shuffle(randomPath)
        initialPaths.append(randomPath)
    return initialPaths

#weeds out old generation
def weed_generation(baseGeneration, nodeAndDistance):
    survivingGeneration = []
    shuffle(baseGeneration)
    midpoint = len(baseGeneration) // 2
    for i in range(midpoint):
        if path_distance(baseGeneration[i], nodeAndDistance) < path_distance(baseGeneration[i + midpoint], nodeAndDistance):
            survivingGeneration.append(baseGeneration[i])
        else:
            survivingGeneration.append(baseGeneration[i + midpoint])
    return survivingGeneration

#creates offspring based off of two parents, helper function for crossover functions
def offspring(parentOne, parentTwo):
    listOfOffspring = []
    extractStart = randint(0, len(parentOne) - 1)
    extractEnd = randint(extractStart, len(parentOne) - 1)
    subarrayOfOne = parentOne[extractStart : extractEnd]
    leftoverTwoPath = list([element for element in parentTwo if element not in subarrayOfOne])
    for iter in range(0, len(parentOne)):
        if extractStart <= iter < extractEnd:
            offspring.append(subarrayOfOne.pop(0))
        else:
            offspring.append(leftoverTwoPath.pop(0))
    return listOfOffspring

def crossoverA(survivingGeneration):
    offsprings = []
    midpoint = len(survivingGeneration) // 2
    for iter in range(midpoint):
        parentOne = survivingGeneration[iter]
        parentTwo = survivingGeneration[iter + midpoint]
        for j in range(2):
            offsprings.append(offspring(parentOne, parentTwo))
            offsprings.append(offspring(parentTwo, parentOne))
    return offsprings

def mutationOne(currentGeneration):
    mutatedGeneration = []
    for path in currentGeneration:
        if randint(0, 10000) < 10:
            indexOne = randint(0, len(path) - 1)
            indexTwo = randint(0, len(path) - 1)
            path[indexOne] = path[indexTwo]
            path[indexTwo] = path[indexOne]
        mutatedGeneration.append(path)
    return mutatedGeneration

get_coordinates(tspFile, coordinates)
x = make_paths(60, 100)
y = weed(x, coordinates)
print(y)



tspFile.close()