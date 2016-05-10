#-----------------------------------------------------#
#				AI Final Project					  #
#					Front End                         #
#													  #
#												      #
#-----------------------------------------------------#

import os
import random
import shutil
from features import *
#import sklearn


class IOclass:
	def __init__(self):

		self.authorName = raw_input("ENTER AUTHOR NAME: ")
		self.filename = raw_input("ENTER FILENAME FOR PASSAGE: ")
		self.authorsWorks = raw_input("ENTER DIRECTORY NAME FOR KNOWN WORKS ('none' to skip): ")

def authorToVector(author):
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + '/bin/database/'
	path = path + author + '/'
	for filename in os.listdir(path):
		thisFile = open(path + filename, "r")
		#call feature vector code here!

def movePassagesToDirectory(io):
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + '/input/'
	path = path + io.authorsWorks + '/'

	if not os.path.exists(path):
		print "ERROR: desired directory does not exist"
		return

	if not os.path.exists(dir + "/bin/database/" + io.authorName):
		os.makedirs(dir + "/bin/database/" + io.authorName)

	for filename in os.listdir(path):
		thisFile = open(path + filename, "r")
		for line in thisFile:
			# DO STUFF WITH INPUT DIRECTORY -----------------------
			#print line
			# -----------------------------------------------------
			# COPY INPUT DIRECTORY INTO DATABASE --------------------------
			shutil.copy(path + filename, dir + "/bin/database/" + io.authorName + "/")
			# -------------------------------------------------------------
			vector(path + filename, dir+"/bin/"+io.authorName+".txt")

def main():
	#Prompt user for file and directory name
	io = IOclass()

	#open input file
	filePath = "input/" + io.filename
	inputFile = open(filePath, "r")

	#FOR DEBUGGING (print input file data) ----------------------------------------
	#for line in inputFile:
	#	print line
	#------------------------------------------------------------------------------

	if io.authorsWorks.lower() is 'none':
		print "no directory selected"
	else:
		movePassagesToDirectory(io)

	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	dir += "/bin/"
	featureList = []
	classifierList = []
	for filename in os.listdir(dir):
		if filename == "database":
			continue;
		authorFile = open(dir + filename, "r")
		for line in authorFile:
			authorVec = []
			for feature in line.split(","):
				authorVec.append(float(feature))
			featureList.append(authorVec)
			if filename == io.authorName + ".txt":
				classifierList.append(1)
			else:
				classifierList.append(0)

	inputVector = passageToFeature(filePath)


	print("Support Vector Machine:\n")
	from sklearn import svm

	print("	Creating...\n")
	train1 = svm.SVC(kernel='rbf')

	print("	Training...\n")
	train1.fit(featureList, classifierList)

	print("	Predicting...\n")

	result = train1.predict([inputVector])
	if result ==0:
		print("	Result: "+"Forgery")
	else:
		print("	Result: "+"Legit")
	score=train1.score(featureList, classifierList)

	print("		Mean accuracy of the SVM (training set): "+str(score)+'\n')

	print("Nueral Network:\n")
	from pybrain.tools.shortcuts import buildNetwork

	print("	Creating...\n")
	from pybrain.structure import TanhLayer
	net = buildNetwork(len(featureList[0]), len(featureList[0])+1, 1, hiddenclass=TanhLayer)

	from pybrain.datasets import SupervisedDataSet

	#size= amount of features per feature vector
	ds = SupervisedDataSet(len(featureList[0]), 1)

	for item, classifier in zip(featureList,classifierList):
		ds.addSample(tuple(item),(classifier,))

	
	print("	Training...\n")
	from pybrain.supervised.trainers import BackpropTrainer

	trainer = BackpropTrainer(net, ds)

	NUM_EPOCHS=100

	for i in range(NUM_EPOCHS):
		error = trainer.train()
	error = trainer.train()
	print "Epoch: %d, Error: %7.4f" % (50, error)

	print("	Predicting...\n")
	result = net.activate(inputVector)
	print ("	Result: "+str(result)[1:-1] + "% a forgery")



if __name__ == '__main__': main()




	
