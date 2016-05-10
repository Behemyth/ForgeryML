import re
import fnmatch
import nltk.tag

# list of informal contractions
c = ["isn't", "aren't", "wasn't", "weren't", "haven't", "hasn't", "hadn't", "won't", 
        "wouldn't", "don't", "doesn't", "didn't", "can't", "couldn't", "shouldn't",
        "would've", "could've", "why's", "how'd", "when's", "what'd", "who'd", "i'm"]

# list of "visual" sensory words
vis = ["light", "dark", "black", "white", "blue", "red", "orange", "yellow", "green", "grey", "gray", "pink", "purple", 
       "saw", "see", "view", "eyes", "color", "colour", "shape", "round", "square", "corner", "large", "big", "small", 
       "tiny", "eye", "look", "looks", "looked", "seeing", "size", "distance", "far", "near"]

# list of auditory sensory words
aud = ["loud", "soft", "quiet", "silent", "hear", "ear", "ears", "song", "music", "chord", "dissonant", 
       "deaf", "note", "melody"]

# list of parts of speech for passage
pos = []

# for future functions; probably best to turn these into hashmaps with some
# sort of function and just check each word of the passage, hash it, and see
# if that key has a value in the below future hashmaps
	
""" FUNCTIONS THAT ARE USED THROUGHOUT THE ENTIRE CODE 
/ GENERIC FUNCTIONS THAT SHOULDNT BE CHANGED, ASHER """
	
# list of words from a line in passage
def listOfWords( line ):
	
	words = line.split()
	words = filter(None, words)
	return words

# parses the passage into a list of sentences
def extracting(file):

	#query = raw_input("where they at doe?? ")
	#f = filename

	passage=file.read()

	str_list = re.split('[.?!] |\n',passage)
	str_list = filter(None, str_list)
	
	for line in str_list:
		
		words = listOfWords(line)	
		tagged = nltk.pos_tag(words)
		pos.extend(tagged)	
		
	return str_list

def Extract(filename):

	passage = extracting(filename)
	
	featureVector = [sentLength(passage), wordLength(passage), contractions(passage), 
	                 adverbs(passage), commas(passage), commaSent(passage), 
	                 punctuation(passage), punctSent(passage), numerics(passage), 
	                 numSent(passage), numQuot(passage), adjAmt(passage), 
	                 artAmt(passage), nAmt(passage), preAmt(passage), 
	                 modAmt(passage), cocAmt(passage), carAmt(passage), 
	                 exiAmt(passage), detAmt(passage), comNA(passage), 
	                 uniWords(passage), special(passage), uncommon(passage), 
	                 common(passage), visWords(passage), audWords(passage)]
	
	return featureVector

# find elements in list
def findInList( passage, listOfThings ):

	numContract = 0.0

	for line in passage:

		words = listOfWords(line)

		for word in words:
			if (word.lower() in listOfThings):
				numContract += 1.0/len(words)

	return round(numContract/len(passage),2)

# how much "searchTerm" per sentence (per word)
def perSentence( passage, searchTerm ):
	
	count = 0.0
	
	for line in passage:
		
		words = listOfWords(line)
		
		smallCount = 0.0
		
		if len(words) > 0:
			for word in words:
				if re.search(searchTerm, word) != None:
					smallCount += 1
					
			smallCount = smallCount/len(words)
			count += smallCount
		
	return round(count/len(passage),2)

# how many sentences contain searchTerm
def sentAmt( passage, searchTerm ):
	
	count = 0.0
	
	for line in passage:
		
		if re.search(searchTerm, line) != None:
			count += 1
			
	return round (count/len(passage),2)

# number of searchTerm per sentence (fnmatch version)
def fperSentence( passage, searchTerm ):
	
	count = 0.0
	
	for line in passage:
		
		words = listOfWords(line)
		
		if len(words) > 0:
			filtered = fnmatch.filter(words, searchTerm)
			count += float(len(filtered))/len(words)

	return round(count/len(passage),2)
		
# amount of a part of speech in passage
def posAmt( passage, part ):
	
	count = 0.0
	
	for tup in pos:
		if re.search(part, tup[1]) != None:
			count += 1;
	
	return round(count/len(pos),2)

""" SPECIFIC FUNCTIONS THAT DO SPECIFIC THINGS """

# counts average sentence length (in characters) and
# divides by 100 to produce a percentage
def sentLength( passage ):

	sumOfSents = 0.0
	
	for line in passage:
		sumOfSents += (len(line.lstrip()))

	avg = sumOfSents/len(passage)
	
	# an average sentence length of longer than 200
	# is considered 'the longest' avg length and just
	# be assigned the max
	if (avg >= 200):
		avg = 200
		
	return round(avg/200,2)

# counts average word length (in characters)
def wordLength( passage ):

	avgOfWords = 0.0
	
	for line in passage:
	    
	    firstSum = 0.0
	    words = listOfWords(line)
	    
	    if len(words) > 0:
		    
			for word in words:
				firstSum += len(word)
		    
			firstAvg = firstSum/len(words)
			avgOfWords += firstAvg
	    
	avg = avgOfWords / len(passage)
	
	# "longest" average of words (will 'max' at this point)
	if (avg >= 8):
		avg = 8
		
	return round(avg/8,2)

# number of contractions in passage
def contractions( passage ):
	return findInList(passage, c)

# number of simply horrid adverbs per sentence
def adverbs( passage ):
	return fperSentence(passage, "*ly")

# how many commas per sentence
def commaSent( passage ):
	return perSentence(passage, ",")
				
# how many sentences contain commas
def commas( passage ):
	
	commas = 0.0
	
	for line in passage:
		if ", " in line:
			commas += 1
			
	return round(commas/len(passage),2)

# how much 'odd' punctuation per sentence
def punctSent( passage ):
	return perSentence(passage, "[:;-]")

# how many sentences contain 'odd' punctuation 
def punctuation( passage ):
	return sentAmt(passage, "[:;-]")

# how many sentences contain numerical values (1,2,3,...9)
def numerics( passage ):
	return sentAmt(passage, "[1-9]")

# special character search
def special( passage ):
	return perSentence(passage, "[!@#$%^&*()+_=<>/~`]")

# uncommon characters
def uncommon( passage ):
	return perSentence(passage, "[qzwxkj]")

# very common characters excluding vowel
def common( passage ):
	return perSentence(passage, "[snmcyth]")

# how many numerical values per sentence
def numSent( passage ):
	return perSentence(passage, "[1-9]")

# how many sentences contain quotations
def numQuot( passage ):
	return sentAmt(passage, "\"")

# below are certain PoS in passage
def adjAmt( passage ):
	return posAmt(passage, "JJ")

def artAmt( passage ):
	return posAmt(passage, "AT")

def nAmt( passage ):
	return posAmt(passage, "NN")

def preAmt( passage ):
	return posAmt(passage, "IN")

def modAmt( passage ):
	return posAmt(passage, "MD")

def cocAmt( passage ):
	return posAmt(passage, "CC")

def carAmt( passage ):
	return posAmt(passage, "CD")

def exiAmt( passage ):
	return posAmt(passage, "EX")

def detAmt( passage ):
	return posAmt(passage, "DT")

# how many adjectives compared to nouns
def comNA( passage ):
	return round(float((posAmt(passage, "JJ"))/posAmt(passage, "NN"))/10,2)

# lexical richness of passage
def uniWords( passage ):
	
	count = 0.0 
	
	for line in passage:
		
		words = listOfWords(line)
		
		if len(words) > 0:
			count += len(set(words))/len(words)
		
	return round(count/len(passage),2)

# visual words in passage
def visWords( passage ):
	return findInList(passage, vis)

# aud words in passage
def audWords( passage ):
	return findInList(passage, aud)