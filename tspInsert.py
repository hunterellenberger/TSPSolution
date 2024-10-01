from tspUtil import get_coordinates, calc_distance, plotter
from sys import maxsize

tspFile = open("Random30.tsp", "r")
coordinates = {}
x = []
y = []

def find_shortest_path(node, listOfPaths, nodeAndCoordinates):
    shortestDistance = [None, maxsize]
    tempDistance = 0

    for element in listOfPaths:
        tempDistance = calc_distance(nodeAndCoordinates[node][0], nodeAndCoordinates[node][1], nodeAndCoordinates[element][0], nodeAndCoordinates[element][1])
        if tempDistance != 0 and tempDistance < shortestDistance[1]:
            shortestDistance = [element, tempDistance]
    print(shortestDistance)
    print()
    return shortestDistance

def greedy_insert(start, nodePlusCoordinate):
    path = []
    notTouchedNodes = []

    for element in nodePlusCoordinate:
        notTouchedNodes.append(element)

    while notTouchedNodes:
        path.append(start)
        greedyPath = find_shortest_path(start, notTouchedNodes, nodePlusCoordinate)
        notTouchedNodes.remove(start)
        start = greedyPath[0]
    
    return path


    print(notTouchedNodes)


get_coordinates(tspFile, coordinates)
print(greedy_insert(1, coordinates))
plotter(coordinates)


tspFile.close()