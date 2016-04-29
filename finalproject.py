#-----------------------------------------------------#
#				AI Final Project					  #
#					Front End                         #
#													  #
#												      #
#-----------------------------------------------------#

import os
import random
import shutil
from features import vector
import pybrain

class IOclass:
	def __init__(self):

		self.authorName = raw_input("ENTER AUTHOR NAME: ")
		self.filename = raw_input("ENTER FILENAME FOR PASSAGE: ")
		#note: shouldn't we be able to figure out the directory name for known works based on the author's name pretty easily? Take a look at features.py or I can too I guess
		self.authorsWorks = raw_input("ENTER DIRECTORY NAME FOR KNOWN WORKS ('none' to skip): ")

def authorToVector(author):
	#note: what does this function used for? just opens a bunch of files
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + '/bin/database/'
	path = path + author + '/'
	for filename in os.listdir(path):
		thisFile = open(path + filename, "r")

def movePassagesToDirectory(io):
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + '/input/' + io.authorsWorks + '/'

	#note: if directory doesn't exist should we just create one?
	if not os.path.exists(path):
		print "ERROR: desired directory does not exist"
		return

	if not os.path.exists(dir + "/bin/database/" + io.authorName):
		os.makedirs(dir + "/bin/database/" + io.authorName)

	for filename in os.listdir(path):
		thisFile = open(path + filename, "r")
		for line in thisFile:
			# DO STUFF WITH INPUT DIRECTORY -----------------------
			print line
			# -----------------------------------------------------
			# COPY INPUT DIRECTORY INTO DATABASE --------------------------
			shutil.copy(path + filename, dir + "/bin/database/" + io.authorName + "/")
			# -------------------------------------------------------------
			vector(path + filename, io.authorName)

def main():
	#Prompt user for file and directory name
	io = IOclass()

	#open input file
	filePath = "input/" + io.filename
	inputFile = open(filePath, "r")

	#FOR DEBUGGING (print input file data)
	#----------------------------------------
	#for line in inputFile:
	#	print line
	#------------------------------------------------------------------------------

	if io.authorsWorks.lower() is 'none':
		print "no directory selected"
	else:
		movePassagesToDirectory(io)



    #Network startup idk what the heck it
    #takes---------------------------------------------------------
	from pybrain.tools.shortcuts import buildNetwork
	net = buildNetwork(2, 3, 1)

	from pybrain.datasets import SupervisedDataSet
	ds = SupervisedDataSet(2, 1)
	ds.addSample((0, 0), (0,))
	ds.addSample((0, 1), (1,))
	ds.addSample((1, 0), (1,))
	ds.addSample((1, 1), (0,))

	from pybrain.supervised.trainers import BackpropTrainer
	trainer = BackpropTrainer(net, ds)
	trainer.trainUntilConvergence()


if __name__ == '__main__': main()
