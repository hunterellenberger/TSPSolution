from tspUtil import get_coordinates, calc_distance, plotter
from random import shuffle, randint
import matplotlib.pyplot as plt
from statistics import median

#initialization of variables to be used throughout program
tspFile = open("Random100.tsp", "r")
coordinates = {}    #holds nodes and their coordinates
generationDictionary = {}
generationCounter = 1

#calculates distance of a path
def path_distance(path, nodeAndDistance):
    totalLength = 0
    for i in range(0, len(path)):
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
    extractEnd = randint(extractStart, len(parentOne))
    subarrayOfOne = parentOne[extractStart:extractEnd]
    leftoverTwoPath = []
    for element in parentTwo:
        if element not in subarrayOfOne:
            leftoverTwoPath.append(element)
    for iter in range(0, len(parentOne)):
        if extractStart <= iter < extractEnd:
            listOfOffspring.append(subarrayOfOne.pop(0))
        else:
            listOfOffspring.append(leftoverTwoPath.pop(0))
    return listOfOffspring

def crossover(survivingGeneration):
    offsprings = []
    midpoint = len(survivingGeneration) // 2
    for iter in range(midpoint):
        parentOne = survivingGeneration[iter]
        parentTwo = survivingGeneration[iter + midpoint]
        for j in range(2):
            offsprings.append(offspring(parentOne, parentTwo))
            offsprings.append(offspring(parentTwo, parentOne))
    return offsprings

def mutation(currentGeneration):
    mutatedGeneration = []
    for path in currentGeneration:
        if randint(0, 10000) < 10:
            indexOne = randint(1, len(path) - 1)
            indexTwo = randint(1, len(path) - 1)
            path[indexOne], path[indexTwo] = path[indexTwo], path[indexOne]
        mutatedGeneration.append(path)
    return mutatedGeneration

def compute_min_avg_max_of_generation(generation, counter, dictOfGenerations, nodeAndDistance):
    tempDict = {}
    for path in generation:
        tempDict[path_distance(path, nodeAndDistance)] = path
    minWalk = [min(tempDict.keys()), tempDict[min(tempDict.keys())]]
    avgWalk = [median(tempDict.keys())]
    maxWalk = [max(tempDict.keys()), tempDict[max(tempDict.keys())]]
    dictOfGenerations[counter] = [minWalk, avgWalk, maxWalk]
    counter += 1

#generates a new generation 
def generate_generation(baseGeneration, nodeAndDistance):
    survivingGeneration = weed_generation(baseGeneration, nodeAndDistance)
    crossoverAGeneration = crossover(survivingGeneration)
    finalGeneration = mutation(crossoverAGeneration)
    compute_min_avg_max_of_generation(finalGeneration, generationCounter, generationDictionary, coordinates)
    return finalGeneration

def less_members_more_iterations(nodeAndDistance):
    #iterations = 10000
    #members = 500
    iterations = 1000
    members = 50
    distancesOfFinalPaths = []


    finalGeneration = make_paths(members, 100)
    for iter in range(iterations):
        finalGeneration = generate_generation(finalGeneration, nodeAndDistance)

    for path in finalGeneration:
        distancesOfFinalPaths.append(path_distance(path, nodeAndDistance))
    return distancesOfFinalPaths

def more_members_less_iterations(nodeAndDistance):
    #iterations = 5000
    #members = 1000
    iterations = 500
    members = 100
    distancesOfFinalPaths = []

    finalGeneration = make_paths(members, 100)
    for iter in range(iterations):
        finalGeneration = generate_generation(finalGeneration, nodeAndDistance)

    for path in finalGeneration:
        distancesOfFinalPaths.append(path_distance(path, nodeAndDistance))
    return distancesOfFinalPaths

get_coordinates(tspFile, coordinates)

moreIterationsList = less_members_more_iterations(coordinates)
print(generationDictionary)
print()

generationCounter = 1

moreMembersList = more_members_less_iterations(coordinates) 
print(generationDictionary)

print(min(moreIterationsList), min(moreMembersList))

tspFile.close()