#-----------------------------------------------------#
#				AI Final Project					  #
#					Front End                         #
#													  #
#												      #
#-----------------------------------------------------#

import os
import random

class IOclass:
	def __init__(self):

		self.authorName = raw_input("ENTER AUTHOR NAME: ")
		self.filename = raw_input("ENTER FILENAME FOR PASSAGE: ")
		self.authorsWorks = raw_input("ENTER DIRECTORY NAME FOR KNOWN WORKS ('none' to skip): ")


def main():
	#Prompt user for file and directory name
	io = IOclass()

	#open input file
	filePath = "input/" + io.filename
	inputFile = open(filePath, "r")

	#FOR DEBUGGING (print input file data) ----------------------------------------
	for line in inputFile:
		print line
	#------------------------------------------------------------------------------
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + '/input/'
	path = path + io.authorsWorks + '/'

	for filename in os.listdir(path):
		thisFile = open(path + filename, "r")
		for line in thisFile:
			print line

if __name__ == '__main__': main()




	
