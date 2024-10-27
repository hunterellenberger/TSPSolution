from tspUtil import get_coordinates, calc_distance
from random import shuffle

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
def weed(baseGeneration, nodeAndDistance):
    survivingGeneration = []
    shuffle(baseGeneration)
    midpoint = len(baseGeneration) // 2
    for i in range(midpoint):
        if path_distance(baseGeneration[i], nodeAndDistance) < path_distance(baseGeneration[i + midpoint], nodeAndDistance):
            survivingGeneration.append(baseGeneration[i])
        else:
            survivingGeneration.append(baseGeneration[i + midpoint])
    return survivingGeneration


get_coordinates(tspFile, coordinates)
x = make_paths(60, 100)
y = weed(x, coordinates)
print(y)



tspFile.close()