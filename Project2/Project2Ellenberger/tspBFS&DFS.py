#import statements used to acquire functions for queue, distance formula, and lsp to coordinate dictionary converter
from tspUtil import get_coordinates, calc_distance, permutations_compute
from collections import deque
import time
start = time.time()

tspFile = open("11PointDFSBFS.tsp", "r")
coordinates = {}
distances = {}

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
    bfsQueue = deque([(root, [root])])  # Queue will store list of (current_node, path_to_node)
    paths = []  # List to keep track of paths that reach final node

    while bfsQueue:
        location, currentPath = bfsQueue.popleft()

        # Check if the current node is a leaf node
        if not nodeMap[location]:  # If there are no edges for this node
            paths.append(currentPath)  # Store the path to the leaf node

        for edge in nodeMap[location]:
            bfsQueue.append((edge, currentPath + [edge]))  # Append the new path

    return paths

def depthFirstSearch(nodeMap, root):
    dfsStack = [(root, [root])]  # Stack will store tuples of (current_node, path_to_node)
    paths = []  # List to keep track of paths that reach final nodes

    while dfsStack:
        location, currentPath = dfsStack.pop()  # Use pop() to get the last element

        # Check if the current node is a leaf node
        if not nodeMap[location]:  # If there are no edges for this node
            paths.append(currentPath)  # Store the path to the leaf node

        for edge in reversed(nodeMap[location]):
            dfsStack.append((edge, currentPath + [edge]))  # Append the new path

    return paths

get_coordinates(tspFile, coordinates)

bfs = breadthFirstSearch(touchingNodes, 1)
print(bfs)
print()

permutations_compute(bfs, distances, coordinates)
for key in distances:
    print(f"{key}: {distances[key]}")
bestRoute = max(distances.keys())
print(bestRoute)

# dfs = depthFirstSearch(touchingNodes, 1)
# print(dfs)
# print()

# permutations_compute(dfs, distances, coordinates)
# for key in distances:
#     print(f"{key}: {distances[key]}")
# bestRoute = min(distances.keys())
# print(bestRoute)

end = time.time()
print("The total time it took the program to execute is:", (end - start) * 10**3, "ms")

tspFile.close()