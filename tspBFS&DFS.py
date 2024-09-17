from tspUtil import get_coordinates, calc_distance
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

def breadthFirstSearch(nodeMap):
    i = 1
    while len(nodeMap[i]) != 0:
        print(nodeMap[i])
        i += 1

breadthFirstSearch(touchingNodes)
get_coordinates(tspFile, coordinates)
print(coordinates)

tspFile.close()