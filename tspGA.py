from tspUtil import get_coordinates, calc_distance
from random import shuffle

tspFile = open("Random100.tsp", "r")
populationOne = []
populationTwo = []
baseList = []
coordinates = {}


def make_population():
    print()


get_coordinates(tspFile, coordinates)

for element in coordinates.keys():
    baseList.append(element)

#makes shallow copy; fix this
shuffle(baseList)
populationOne = baseList
shuffle(baseList)
populationTwo = baseList

print(populationOne)
print(populationTwo)


tspFile.close()