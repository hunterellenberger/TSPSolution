import matplotlib.pyplot as plt
import numpy as np 

#reads in file and seperates the coordinates into pairs within a dictionary
def get_coordinates(file, dictionary):
    for line in file:
        if line[0].isdigit():
            splitLine = line.split(' ')
            dictionary[int(splitLine[0])] = [float(splitLine[1])]
            dictionary[int(splitLine[0])].append(float(splitLine[2]))

#calculates distance between two coordinates
def calc_distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

#uses calc_distance function in tandem with the list of permutations to calculate every possible travelling salesman path
def permutations_compute(permutation, pathPlusDistances, nodes):
    for element in permutation:
        total = 0
        for vertex in range(0, len(element) - 1):
            total += calc_distance(nodes[element[vertex]][0], nodes[element[vertex]][1], nodes[element[vertex + 1]][0], nodes[element[vertex + 1]][1])
        total += calc_distance(nodes[element[0]][0], nodes[element[0]][1], nodes[element[len(element) - 1]][0], nodes[element[len(element) - 1]][1])
        if total not in pathPlusDistances:
            pathPlusDistances[total] = [element]
        else:
            pathPlusDistances[total].append([element])

def plotter(points, pathMap):
    xValues = []
    yValues = []
    for element in pathMap:
        xValues.append(points[element][0])
        yValues.append(points[element][1])

    

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    for i in range(0, len(xValues)):
        plt.plot(xValues[:i + 1], yValues[:i + 1], 'red')

    plt.plot(xValues, yValues, 'b*')
    plt.axis([0, 100, 0, 100])

    plt.show()
