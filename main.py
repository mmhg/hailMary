import csv
import math

class Classifier:

    	def __init__(self, filename, normalize=True):

        	self.medianAndDeviation = []
        	self.normalize = normalize
        	# reading the data in from the url
        
        	self.data = []
        	for line in lines[1:]:
            		fields = line.strip().split('\t')
            		ignore = []
            		vector = []
            		for i in range(len(fields)):
                		if self.format[i] == 'num':
                    			vector.append(float(fields[i]))
                		elif self.format[i] == 'comment':
                    			ignore.append(fields[i])
                		elif self.format[i] == 'class':
                    			classification = fields[i]
           		self.data.append((classification, vector, ignore))
        	self.rawData = list(self.data)
        	# get length of instance vector
        	self.vlen = len(self.data[0][1])
        	# now normalize the data
        	if self.normalize:
            		for i in range(self.vlen):
                		self.normalizeColumn(i)

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
        
    
    	##################################################
    	###
    	###  CODE TO COMPUTE THE MODIFIED STANDARD SCORE

    	def getMedian(self, alist):
        	"""return median of alist"""
        	if alist == []:
            		return []
        	blist = sorted(alist)
        	length = len(alist)
        	if length % 2 == 1:
            		# length of list is odd so return middle element
            		return blist[int(((length + 1) / 2) -  1)]
        	else:
            		# length of list is even so compute midpoint
            		v1 = blist[int(length / 2)]
            		v2 =blist[(int(length / 2) - 1)]
            		return (v1 + v2) / 2.0
        

    	def getAbsoluteStandardDeviation(self, alist, median):
        	"""given alist and median return absolute standard deviation"""
        	sum = 0
        	for item in alist:
            		sum += abs(item - median)
        	return sum / len(alist)


    	def normalizeColumn(self, columnNumber):
       		"""given a column number, normalize that column in self.data"""
       		# first extract values to list
       		col = [v[1][columnNumber] for v in self.data]
       		median = self.getMedian(col)
       		asd = self.getAbsoluteStandardDeviation(col, median)
       		#print("Median: %f   ASD = %f" % (median, asd))
       		self.medianAndDeviation.append((median, asd))
       		for v in self.data:
           		v[1][columnNumber] = (v[1][columnNumber] - median) / asd


    	def normalizeVector(self, v):
        	"""We have stored the median and asd for each column.
        	We now use them to normalize vector v"""
        	vector = list(v)
        	if self.normalize:
            		for i in range(len(vector)):
                		(median, asd) = self.medianAndDeviation[i]
                		vector[i] = (vector[i] - median) / asd
        	return vector

    
    	###
    	### END NORMALIZATION
    	##################################################
	def euclidean(rating1, rating2):
    		distance = 0
    		commonRatings = False
    		for key in rating1:
        		if key in rating2:
        	    		distance += abs((rating1[key] - rating2[key])**2)
            			commonRatings = True
    		distance1=math.sqrt(distance)
    		if commonRatings:
        		return distance1
    		else:        return -1


    	def manhattan(self, vector1, vector2):
        	"""Computes the Manhattan distance."""
        	return sum(map(lambda v1, v2: abs(v1 - v2), vector1, vector2))


    	def nearestNeighbor(self, itemVector):
        	"""return nearest neighbor to itemVector"""
        	return min([ (self.manhattan(itemVector, item[1]), item) for item in self.data])
    
    	def classify(self, itemVector):
        	"""Return class we think item Vector is in"""
        	return(self.nearestNeighbor(self.normalizeVector(itemVector))[1][0])

def main():
	filename='studentMath.csv'
	
