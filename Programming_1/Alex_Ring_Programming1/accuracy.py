'''
Alex Ring
September 2016
Accuracy.py

Compare the lines in an answer file to those in a vowpal wabbit generated file for accuracy
'''

correctAnswers = []
predictedAnswers = []
correctCount = 0
length = 0

data = open('iris_test.vw').readlines()
for row in data:
	correctAnswers.append(int(row[0]))

print(correctAnswers)
vwData = open('predictions.txt').readlines()
for row in vwData:
	predictedAnswers.append(int(row[0]))
	length = length + 1


for i in range(length):
	if correctAnswers[i] == predictedAnswers[i]:
		correctCount = correctCount + 1

accuracy = float((correctCount/length) * 100)
print("Correct Count",correctCount)

print("-"*15)
print("Vowpal Wabbit Accuracy:", accuracy, "%")
print("-"*15)