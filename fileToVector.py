
def main():
	dir = os.path.dirname(os.path.realpath(__import__("__main__").__file__))
	path = dir + '/bin/database/'
	path = path + io.authorsWorks + '/'
	for filename in os.listdir(path):
		thisFile = open(path + filename, "r")
		for line in thisFile:
			i=5
if __name__ == '__main__': main()