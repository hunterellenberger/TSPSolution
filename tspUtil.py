#reads in file and seperates the coordinates into pairs within a dictionary
def get_coordinates(file, dictionary):
    for line in file:
        if line[0].isdigit():
            splitLine = line.split(' ')
            dictionary[int(splitLine[0]) - 1] = [float(splitLine[1])]
            dictionary[int(splitLine[0]) - 1].append(float(splitLine[2]))

#calculates distance between two coordinates
def calc_distance(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)