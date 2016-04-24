import os 

def main():
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + "/bin/database/"
	for author in os.listdir(path):
		dirPath = path + "/" + author + "/"
		features = open(path + author + ".txt", "w")
		for filename in os.listdir(dirPath):
			print filename
			inputFile = open(dirPath + filename, "r")
			features.write("<0,0,0>" + "\n")

if __name__ == '__main__': main()