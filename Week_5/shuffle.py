import random

def shuffle():
	with open('week5.vw') as myfile:
		content = myfile.readlines()
	size = len(content)
	trainSize = int(size * 0.80)
	trainingData = []
	testingData = content
	while len(trainingData) < trainSize:
		index = random.randrange(len(testingData))
		trainingData.append(testingData.pop(index))
	with open('week5_train.vw','w') as myfile:
		for i in range(len(trainingData)):
			myfile.write(str(trainingData[i]))
	with open('week5_test.vw','w') as myfile:
		for i in range(len(testingData)):
			myfile.write(str(testingData[i]))

	with open('week5_train.vw') as myfile:
		lines = myfile.readlines()
		random.shuffle(lines)
	with open('week5_train.vw','w') as myfile:
		myfile.writelines(lines)

	with open('week5_test.vw') as myfile:
		lines = myfile.readlines()
		random.shuffle(lines)
	with open('week5_test.vw','w') as myfile:
		myfile.writelines(lines)

shuffle()