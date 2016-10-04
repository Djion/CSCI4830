import random

def shuffle():
	with open('positivenegative.vw') as myfile:
		content = myfile.readlines()
	size = len(content)
	trainSize = int(size * 0.80)
	trainingData = []
	testingData = content
	while len(trainingData) < trainSize:
		index = random.randrange(len(testingData))
		trainingData.append(testingData.pop(index))
	with open('PA2_train.vw','w') as myfile:
		for i in range(len(trainingData)):
			myfile.write(str(trainingData[i]))
	with open('PA2_test.vw','w') as myfile:
		for i in range(len(testingData)):
			myfile.write(str(testingData[i]))

	with open('PA2_train.vw') as myfile:
		lines = myfile.readlines()
		random.shuffle(lines)
	with open('PA2_train.vw','w') as myfile:
		myfile.writelines(lines)

	with open('PA2_test.vw') as myfile:
		lines = myfile.readlines()
		random.shuffle(lines)
	with open('PA2_test.vw','w') as myfile:
		myfile.writelines(lines)

shuffle()