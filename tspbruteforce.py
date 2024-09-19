#permutations is used to extract every combination from the given coordinates
#time is used to track the total time of the program
from tspUtil import get_coordinates, calc_distance, permutations_compute
from itertools import permutations
import time
start = time.time()

#initializing variables that will be used throughout the program
tspFile = open("Random4.tsp", "r")
coordinates = {}
tspMap = {}
total = 0

#creates permutations, calculates every possible path, then prints out the shortest route along with the points
#associated with reaching that path
get_coordinates(tspFile, coordinates)
p = list(permutations(coordinates.keys()))
permutations_compute(p, tspMap, coordinates)
bestRoute = min(tspMap.keys())
print(f"{bestRoute}: {tspMap[bestRoute]}")
tspFile.close()

end = time.time()
print("The total time it took the program to execute is:", (end - start) * 10**3, "ms")