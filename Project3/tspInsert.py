from tspUtil import get_coordinates, calc_distance, plotter # plotter is a new function used to implemnt the gui of the path taken
from sys import maxsize # used to make sure that no distance is more than the initialized shortest distance
import time # used to time program
start = time.time()

# opens tsp file to be converted into a dictionary called coordinates
# optimalSolution is used to track the best starting point for my greedy algorithm
tspFile = open("Random40.tsp", "r")                                  
coordinates = {}
optimalSolution = [[], maxsize]


# used to find the shortest path to the next node, based off of a starting node
# and list of possible paths
def find_shortest_path(node, listOfPaths, nodeAndCoordinates):
    shortestDistance = [None, maxsize]
    tempDistance = 0

    # so the final element does not mess up the distance calculation
    if len(listOfPaths) == 1:
        return [0, 0]
    
    # iterates through every element to find shortest path to next node (excluding the node itself)
    for element in listOfPaths:
        tempDistance = calc_distance(nodeAndCoordinates[node][0], nodeAndCoordinates[node][1], nodeAndCoordinates[element][0], nodeAndCoordinates[element][1])
        if tempDistance != 0 and tempDistance < shortestDistance[1]:
            shortestDistance = [element, tempDistance]

    return shortestDistance


# uses a greedy methodology to find a path through the TSP problem
def greedy_insert(start, nodePlusCoordinate):
    totalDistance = 0
    path = []
    notTouchedNodes = []

    # used to track which nodes have not been touched
    for element in nodePlusCoordinate:
        notTouchedNodes.append(element)

    # while there are nodes that are untouched search for the next node to insert into the path
    while notTouchedNodes:
        path.append(start)
        greedyPath = find_shortest_path(start, notTouchedNodes, nodePlusCoordinate)
        notTouchedNodes.remove(start)
        start = greedyPath[0]
        totalDistance += greedyPath[1]
    
    # add a return to the first node visited and calculate that distance 
    path.append(path[0])
    totalDistance += calc_distance(nodePlusCoordinate[path[-2]][0], nodePlusCoordinate[path[-2]][1], nodePlusCoordinate[path[-1]][0], nodePlusCoordinate[path[-1]][1])
    return path, totalDistance # return both the path and the total distance traveled


get_coordinates(tspFile, coordinates)

# calculates most optimal start point for the greedy_insert algorithm
for i in range(1, len(coordinates.keys())):
    currentSolution = greedy_insert(i, coordinates)
    if currentSolution[1] < optimalSolution[1]:
        optimalSolution[0] = currentSolution[0]
        optimalSolution[1] = currentSolution[1]


print(optimalSolution)
plotter(coordinates, optimalSolution[0])


end = time.time()
print("The total time it took the program to execute is:", (end - start) * 10**3, "ms")
tspFile.close()