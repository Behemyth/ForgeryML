#-----------------------------------------------------#
#				AI Final Project					  #
#					Front End                         #
#													  #
#												      #
#-----------------------------------------------------#

import os
import random
import shutil
import Network
from features import vector

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

	data = [[[0,0], [0]],[[0,1], [1]],[[1,0], [1]],[[1,1], [0]]]

    #takes in input size, hidden size (same size as input), outputs size (1 for
    #binary yes/no)
	network = Network.Network(2, 2, 1)

	network.Train(data)
	network.Test(data)

    #Network startup idk what the heck it
    #takes---------------------------------------------------------



   

if __name__ == '__main__': main()




	
