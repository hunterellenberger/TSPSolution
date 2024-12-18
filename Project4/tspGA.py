from tspUtil import get_coordinates, calc_distance, dynamic_plotter
from random import shuffle, randint
from statistics import median, stdev
import pandas as pd
import time
start = time.time()

#initialization of variables to be used throughout program
tspFile = open("Random100.tsp", "r")
coordinates = {}    #holds nodes and their coordinates
generationDictionary = {"Max": [], 
                        "Avg": [], 
                        "Min": [], 
                        "StdDev": [],
                        "Max Path": [], 
                        "Min Path": []
                        }

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
    for i in range(0, len(parentOne)):
        if extractStart <= i < extractEnd:
            listOfOffspring.append(subarrayOfOne.pop(0))
        else:
            listOfOffspring.append(leftoverTwoPath.pop(0))
    return listOfOffspring

#crossovers parents within a generation
def crossover(survivingGeneration):
    offsprings = []
    midpoint = len(survivingGeneration) // 2
    for i in range(midpoint):
        parentOne = survivingGeneration[i]
        parentTwo = survivingGeneration[i + midpoint]
        for j in range(2):
            offsprings.append(offspring(parentOne, parentTwo))
            offsprings.append(offspring(parentTwo, parentOne))
    return offsprings

#mutates survivors within a generation
def mutation(currentGeneration):
    mutatedGeneration = []
    for path in currentGeneration:
        if randint(0, 1000) < 10:
            indexOne = randint(1, len(path) - 1)
            indexTwo = randint(1, len(path) - 1)
            path[indexOne], path[indexTwo] = path[indexTwo], path[indexOne]
        mutatedGeneration.append(path)
    return mutatedGeneration

#determines the min, median, and max distances of a generation; loads this data into a dataframe
def compute_stats_of_generation(generation, dictOfGenerations, nodeAndDistance):
    tempDict = {}
    pathDistances = []
    pathRoutes = []

    for path in generation:
        pathDistances.append(path_distance(path, nodeAndDistance))
        pathRoutes.append(path)
    minWalk = [min(pathDistances), pathRoutes[pathDistances.index(min(pathDistances))]]
    avgWalk = [median(pathDistances)]
    maxWalk = [max(pathDistances), pathRoutes[pathDistances.index(max(pathDistances))]]
    standardDev = stdev(pathDistances)
    dictOfGenerations["Max"].append(maxWalk[0])
    dictOfGenerations["Avg"].append(avgWalk[0])
    dictOfGenerations["Min"].append(minWalk[0])
    dictOfGenerations["StdDev"].append(standardDev)
    dictOfGenerations["Max Path"].append(maxWalk[1])
    dictOfGenerations["Min Path"].append(minWalk[1])

#generates a new generation 
def generate_generation(baseGeneration, nodeAndDistance):
    survivingGeneration = weed_generation(baseGeneration, nodeAndDistance)
    crossoverAGeneration = crossover(survivingGeneration)
    finalGeneration = mutation(crossoverAGeneration)
    compute_stats_of_generation(finalGeneration, generationDictionary, coordinates)
    return finalGeneration

def run_genetic_algo(members, iterations, nodeAndDistance):
    distancesOfFinalPaths = []

    finalGeneration = make_paths(members, 100)
    for i in range(iterations):
        finalGeneration = generate_generation(finalGeneration, nodeAndDistance)

    for path in finalGeneration:
        distancesOfFinalPaths.append(path_distance(path, nodeAndDistance))
    return distancesOfFinalPaths

#loads points and coordinates into dictionary
get_coordinates(tspFile, coordinates)

#runs GA implementation with less members per generation, but more generations. Then loads it into dataframe and seperately dynamically plots it
moreIterationsList = run_genetic_algo(500, 5000, coordinates)
df = pd.DataFrame(generationDictionary)
dynamic_plotter(generationDictionary["Min Path"], coordinates, "moreIterations")

#clears generation dictionary so it can be reloaded by new cariation of GA
for stat in generationDictionary:
    generationDictionary[stat].clear()

#runs GA implementation with more members per generation, but less generations. Then loads it into dataframe and seperately dynamically plots it
moreMembersList = run_genetic_algo(1000, 2500, coordinates) 
df2 = pd.DataFrame(generationDictionary)
dynamic_plotter(generationDictionary["Min Path"], coordinates, "moreMembers")

with pd.ExcelWriter("data.xlsx") as writer:
    df.to_excel(writer, sheet_name="more_iterations")
    df2.to_excel(writer, sheet_name="less_iterations")

end = time.time()
print("The total time it took the program to execute is:", (end - start) * 10**3, "ms")
tspFile.close()