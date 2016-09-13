'''
Alex Ring
September 2016
Naive Bayes Classification Programming Assignment 1

This program will generate a model and predict classes of iris flowers based
on data from the iris dataset. 

https://archive.ics.uci.edu/ml/datasets/Iris
'''

'''
There are 3 types of iris flowers that this will attempt to classify
they have each been assigned a value for classification. 
The Iris-setosa {0}
The Iris-versicolor {1}
The Iris-virginica {2}
'''
import csv
import random
import math
import decimal
from decimal import Decimal

#Find the mean of some numbers
#	@numbers : vector of numbers
def mean(numbers):
	length = float(len(numbers))
	mean = sum(numbers)/length
	return mean

#Find the standard deviation of some numbers
#	@numbers : vector of numbers
def stdev(numbers):
	avgerage = mean(numbers)
	deviation = sum([pow(x-avgerage,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(deviation)

#Load the Iris data from a csv file, covert it to a useable form
#and then randomly split it into training and test data
#	@file_name : The name of the csv file
#	@ratio : The ratio at which to split the data into train/test
def loadAndSplit(file_name, ratio):
	rawData = csv.reader(open(file_name, "rt"))
	data = list(rawData)
	for i in range(len(data)):
		data[i] = [float(x) for x in data[i]]

	size = len(data)
	trainSize = int(size * ratio)
	trainingData = []
	testingData = list(data)
	while len(trainingData) < trainSize:
		index = random.randrange(len(testingData))
		trainingData.append(testingData.pop(index))
	return [trainingData, testingData]

#Separate the data in the dataset into the different iris catagories
#Uses the last number of an iris object (0,1,2) to seperate
#	0:Iris-setosa, 1:Iris-versicolor, 2:Iris-virginica
def separateClasses(data):
	#Create new dicitonary that will be used to as the seperator
	length = (len(data))
	class_dict = {}
	for i in range(length):
		classNumber = data[i]
		if (classNumber[-1] not in class_dict):
			class_dict[classNumber[-1]] = []
		class_dict[classNumber[-1]].append(classNumber)
	return class_dict


#Summarize the dataset into the mean and standard deviation of each attribute for a class
#we use this in the gaussian distribution to calculate the probabilities
#	@dataset : Data to summarize
def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries

#Take summaries and map them to a class
#	@dataset : Data to map
def summarizeByClass(dataset):
	separated = separateClasses(dataset)
	summaries = {}
	for classValue, instances in separated.items():
		summaries[classValue] = summarize(instances)
	return summaries

#Given a feature, the mean, and the standard deviation, use gausian normilization to 
#calculate the odds that that feature belongs to a class
#	@x : Feature
#	@mean : Mean of the feature
#	@stdev : Standard deviation of the feature
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1/(math.sqrt(2*math.pi)*stdev)) * exponent

#Calculate the likelihood that the features belong to a class based on probabilities
#	@summaries: The means/stdevs of the features
#
def calculateClassProbabilities(summaries, testCase):
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = testCase[i]
			#Calculate class probabilities using logs instead of naive multiplication
			#Was having math domain errors, used decimal and ln() to fix
			#http://stackoverflow.com/questions/19095774/python-math-domain-errors-in-math-log-function
			probabilities[classValue] += Decimal(calculateProbability(x, mean, stdev)).ln()
	return probabilities

#Predict the class by comparing the summaries
def predictTheClass(summaries, testCase):
	probabilities = calculateClassProbabilities(summaries, testCase)
	probableClass, highestProb = None, -1
	for classValue, probability in probabilities.items():
		if probableClass is None or probability > highestProb:
			highestProb = probability
			probableClass = classValue
	return probableClass

#Do multiple predictions
def buildPredictions(summaries, testData):
	predictions = []
	length = len(testData)
	for i in range(length):
		result = predictTheClass(summaries, testData[i])
		predictions.append(result)
	return predictions

#Check accuracy 
def howAccurate(testData, predictions):
	correct = 0
	length = len(testData)
	for x in range(length):
		if testData[x][-1] == predictions[x]:
			correct = correct + 1
	flength = float(length)
	return (correct/flength * 100.0)

def main():
	filename = 'iris_encoded.csv'
	accuracy_vector = []
	print('\n\n')
	print('Running 100 trains/tests, this may take a moment...')
	#for i in range(1000000)
	for i in range(100):
		trainingData, testData = loadAndSplit(filename, 0.67)		
		summaries = summarizeByClass(trainingData)
		predictions = buildPredictions(summaries, testData)
		#print('Predicted Class For Test Data:',predictions)
		accuracy = howAccurate(testData, predictions)
		print(accuracy)
		accuracy_vector.append(accuracy)
	print('After 100 trains/tests on the iris dataset, with random splitting average accuracy is:',mean(accuracy_vector))

main()
