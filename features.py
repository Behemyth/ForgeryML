import os 

def vector(filename, authorsName):
	inputFile = open(filename, "r")
	features = open(authorsName, "w+")
	features.write("<0,0,0>" + "\n")


def main():
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + "/bin/database/"
	for author in os.listdir(path):
		dirPath = path + "/" + author + "/"
		authorFile = dir + "/bin/" + author + ".txt"
		print "Reading samples for author " + author
		for filename in os.listdir(dirPath):
			#print filename #creates a wall of text now that we actually have a database
			featuresFile = dirPath + filename
			vector(featuresFile, authorFile)

if __name__ == '__main__': main()
