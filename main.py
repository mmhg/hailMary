import csv
import math

def csvParser(filename):
    thisData = []
    file = open(filename)
    reader = csv.reader(file, delimiter=',', quotechar = '"')
    counter = 0
    for row in reader:
        if counter > 0:
            thisData.append(row)
        else:
            counter += 1
    return thisData

def euclidean(rating1, rating2):#still needs to be changed
    distance = 0
    commonRatings = False 
    for key in rating1:
        if key in rating2:
            distance += abs((rating1[key] - rating2[key])**2)
            commonRatings = True
    distance1=math.sqrt(distance)
    if commonRatings:
        return distance1
    else:
        return -1 #Indicates no ratings in common
