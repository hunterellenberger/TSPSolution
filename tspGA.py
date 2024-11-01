from tspUtil import get_coordinates, calc_distance, plotter
from random import shuffle, randint
import matplotlib.pyplot as plt
from statistics import median

#initialization of variables to be used throughout program
tspFile = open("Random100.tsp", "r")
coordinates = {}    #holds nodes and their coordinates
generationDictionary = {}
generationCounter = 1

#calculates distance of an entire path
def path_distance(path, nodeAndDistance):
    totalLength = 0
    for i in range(0, len(path)):
        if i == len(path) - 1:
            totalLength += calc_distance(nodeAndDistance[path[i]][0], nodeAndDistance[path[i]][1], nodeAndDistance[path[-1]][0], nodeAndDistance[path[-1]][1])
            return totalLength
        else:
            totalLength += calc_distance(nodeAndDistance[path[i]][0], nodeAndDistance[path[i]][1], nodeAndDistance[path[i + 1]][0], nodeAndDistance[path[i + 1]][1])
    return totalLength

#makes original generation of paths randomly
def make_paths(numberOfPaths, numberOfNodes):
    initialPaths = []
    for i in range(0, numberOfPaths):
        randomPath = list(range(1, numberOfNodes + 1))
        shuffle(randomPath)
        initialPaths.append(randomPath)
    return initialPaths

#weeds out old generation leaving only the most fit 
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

#crossovers parents within a generation
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

#mutates survivors within a generation
def mutation(currentGeneration):
    mutatedGeneration = []
    for path in currentGeneration:
        if randint(0, 10000) < 10:
            indexOne = randint(1, len(path) - 1)
            indexTwo = randint(1, len(path) - 1)
            path[indexOne], path[indexTwo] = path[indexTwo], path[indexOne]
        mutatedGeneration.append(path)
    return mutatedGeneration

#determines the min, median, and max distances of a generation
def compute_min_avg_max_of_generation(generation, dictOfGenerations, nodeAndDistance):
    tempDict = {}
    global generationCounter

    for path in generation:
        tempDict[path_distance(path, nodeAndDistance)] = path
    minWalk = [min(tempDict.keys()), tempDict[min(tempDict.keys())]]
    avgWalk = [median(tempDict.keys())]
    maxWalk = [max(tempDict.keys()), tempDict[max(tempDict.keys())]]
    dictOfGenerations[generationCounter] = [minWalk, avgWalk, maxWalk]
    generationCounter += 1

#generates a new generation 
def generate_generation(baseGeneration, nodeAndDistance):
    survivingGeneration = weed_generation(baseGeneration, nodeAndDistance)
    crossoverAGeneration = crossover(survivingGeneration)
    finalGeneration = mutation(crossoverAGeneration)
    compute_min_avg_max_of_generation(finalGeneration, generationDictionary, coordinates)
    return finalGeneration

#COULD BE CONDENSED INTO ONE FUNCTION
def run_genetic_algo(members, iterations, nodeAndDistance):
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

moreIterationsList = run_genetic_algo(50, 1000, coordinates)
print(generationDictionary)

generationCounter = 1

moreMembersList = run_genetic_algo(100, 500, coordinates) 
print(generationDictionary)

print(min(moreIterationsList), min(moreMembersList))

tspFile.close()