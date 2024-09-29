from tspUtil import get_coordinates, calc_distance, plotter


tspFile = open("Random30.tsp", "r")
coordinates = {}
x = []
y = []


def greedyInsert():
    print("hello")

get_coordinates(tspFile, coordinates)
plotter(coordinates)


tspFile.close()