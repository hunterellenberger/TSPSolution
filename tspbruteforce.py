#permutations is used to extract every combination from the given coordinates
#time is used to track the total time of the program
from tspUtil import get_coordinates, calc_distance
from itertools import permutations
import time
start = time.time()

#initializing variables that will be used throughout the program
tspFile = open("Random4.tsp", "r")
coordinates = {}
tspMap = {}
total = 0

#uses calc_distance function in tandem with the list of permutations to calculate every possible travelling salesman path
def permutations_compute(permutation):
    for element in permutation:
        total = 0
        for vertex in range(0, len(element) - 1):
            total += calc_distance(coordinates[element[vertex]][0], coordinates[element[vertex]][1], coordinates[element[vertex + 1]][0], coordinates[element[vertex + 1]][1])
        total += calc_distance(coordinates[element[0]][0], coordinates[element[0]][1], coordinates[element[len(element) - 1]][0], coordinates[element[len(element) - 1]][1])
        if total not in tspMap:
            tspMap[total] = [element]
        else:
            tspMap[total].append([element])

#creates permutations, calculates every possible path, then prints out the shortest route along with the points
#associated with reaching that path
get_coordinates(tspFile, coordinates)
p = list(permutations(coordinates.keys()))
permutations_compute(p)
bestRoute = min(tspMap.keys())
print(f"{bestRoute}: {tspMap[bestRoute]}")
tspFile.close()

end = time.time()
print("The total time it took the program to execute is:", (end - start) * 10**3, "ms")