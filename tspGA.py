from tspUtil import get_coordinates, calc_distance
from random import shuffle
from copy import deepcopy

#initialization of variables to be used throughout program
tspFile = open("Random100.tsp", "r")
baseList = []       #holds original 1-100 nodes
populationOne = []  #holds one population that gets mixed with population 2
populationTwo = []  #holds one population that gets mixed with population 1
coordinates = {}    #holds nodes and their coordinates


#makes original generation of paths
def make_paths(numberOfPaths, numberOfNodes):
    initialPaths = []
    for i in range(0, numberOfPaths):
        randomPath = list(range(1, numberOfNodes + 1))
        shuffle(randomPath)
        initialPaths.append(randomPath)
    return initialPaths




get_coordinates(tspFile, coordinates)
print(make_paths(20, 100))




tspFile.close()