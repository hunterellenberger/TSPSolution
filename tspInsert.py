from tspUtil import get_coordinates, calc_distance, plotter
from sys import maxsize


tspFile = open("Random30.tsp", "r")
coordinates = {}
x = []
y = []


def find_shortest_path(node, listOfPaths, nodeAndCoordinates):
    shortestDistance = [None, maxsize]
    tempDistance = 0

    #so the final element does not mess up the distance calculation
    if len(listOfPaths) == 1:
        return [0, 0]
    
    #iterates through every element to find shortest path to next node (excluding the node itself)
    for element in listOfPaths:
        tempDistance = calc_distance(nodeAndCoordinates[node][0], nodeAndCoordinates[node][1], nodeAndCoordinates[element][0], nodeAndCoordinates[element][1])
        if tempDistance != 0 and tempDistance < shortestDistance[1]:
            shortestDistance = [element, tempDistance]

    return shortestDistance


def greedy_insert(start, nodePlusCoordinate):
    totalDistance = 0
    path = []
    notTouchedNodes = []

    for element in nodePlusCoordinate:
        notTouchedNodes.append(element)

    while notTouchedNodes:
        path.append(start)
        greedyPath = find_shortest_path(start, notTouchedNodes, nodePlusCoordinate)
        notTouchedNodes.remove(start)
        start = greedyPath[0]
        totalDistance += greedyPath[1]
    
    path.append(path[0])
    totalDistance += calc_distance(nodePlusCoordinate[path[-2]][0], nodePlusCoordinate[path[-2]][1], nodePlusCoordinate[path[-1]][0], nodePlusCoordinate[path[-1]][1])
    return path, totalDistance


get_coordinates(tspFile, coordinates)
solution = greedy_insert(1, coordinates)
print(solution)
plotter(coordinates, solution[0])


tspFile.close()