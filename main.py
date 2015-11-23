import csv

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
