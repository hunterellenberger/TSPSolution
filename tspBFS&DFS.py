#import statements used to acquire functions for queue, distance formula, and lsp to coordinate dictionary converter
from tspUtil import get_coordinates, calc_distance
from collections import deque


tspFile = open("11PointDFSBFS.tsp", "r")
coordinates = {}

touchingNodes = {
    1: [2, 3, 4],
    2: [3],
    3: [4, 5],
    4: [5, 6, 7],
    5: [7, 8],
    6: [8],
    7: [9, 10],
    8: [9, 10, 11],
    9: [11],
    10: [11],
    11: []
}

def breadthFirstSearch(nodeMap, root):
    bfsQueue = deque([root])
    visitedNodes = []
    while bfsQueue:
        location = bfsQueue.popleft()
        visitedNodes.append(location)
        for edge in nodeMap[location]:
            bfsQueue.append(edge)
    print(visitedNodes)

get_coordinates(tspFile, coordinates)
breadthFirstSearch(touchingNodes, 1)

tspFile.close()