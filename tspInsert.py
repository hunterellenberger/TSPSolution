from tspUtil import get_coordinates, calc_distance, plotter
from collections import deque

tspFile = open("Random30.tsp", "r")
coordinates = {}
x = []
y = []


def greedy_insert(start, pathPlusDistance):
    path = []
    for i in range(start, len(pathPlusDistance)):
        for j in range():
            print("placeholder")


get_coordinates(tspFile, coordinates)
greedy_insert(0, coordinates)
plotter(coordinates)


tspFile.close()