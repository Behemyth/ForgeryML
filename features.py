import os 
import featurevecs

def vector(filename, authorsName):
	#filename is one of the author's works, authorsName is their feature vector file
	inputFile = open(filename, "r")
	features = open(authorsName, "a+")
	#calculate the feature vector expected of the file
	#featurevecs.Extract(inputFile)
	features.write(str(featurevecs.Extract(inputFile))[1:-1] + "\n")

def passageToFeature(filename):
	inputFile = open(filename, "r")
	return featurevecs.Extract(inputFile)

def formDict(filename, dict):
	inputFile = open(filename, "r")

def main():
	#take the file path of the directory containing this python script, store that in dir
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	#save the path to the database to path
	path = dir + "/bin/database/"


	#for each author in the database...
	for author in os.listdir(path):
		#get a path to the directory containing their works
		dirPath = path + "/" + author + "/"
		#get a path to the file that will hold their feature vector
		authorFile = dir + "/bin/" + author + ".txt"
		#simple I/O message for tracking the progress of the script, can remove later
		print "Reading samples for author " + author
		#for each of the author's works
		for filename in os.listdir(dirPath):
			#get the path to the work
			featuresFile = dirPath + filename
			#call vector function
			vector(featuresFile, authorFile)

if __name__ == '__main__': main()
