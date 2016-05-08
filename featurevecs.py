import re


#list of informal contractions
c = ["isn't", "aren't", "wasn't", "weren't", "haven't", "hasn't", "hadn't", "won't", 
                "wouldn't", "don't", "doesn't", "didn't", "can't", "couldn't", "shouldn't",
                "would've", "could've", "why's", "how'd", "when's", "what'd", "who'd", "i'm"]

# for future functions; probably best to turn these into hashmaps with some
# sort of function and just check each word of the passage, hash it, and see
# if that key has a value in the below future hashmaps

#list of british spellings and turns of phrase
with open('britishspellings.txt', 'r') as f:
    britSpell = [line.strip() for line in f]
    
#list of american spellings and turns of phrase
with open('americanspellings.txt', 'r') as f:
    usSpell = [line.strip() for line in f]

# parses the passage into a list of sentences
def extracting(file):

    #query = raw_input("where they at doe?? ")
    #f = filename
    
    with file as myfile:
        passage=myfile.read()    

    str_list = re.split('[.?!]',passage)
    str_list = filter(None, str_list)
    return str_list

# counts average sentence length (in characters)
def sentLength( passage ):
    
    sumOfSents = 0
    
    for line in passage:
        sumOfSents += (len(line.lstrip()))
        
    avg = sumOfSents/len(passage)
    return avg

# counts average word length (in characters)
def wordLength( passage ):
    
    avgOfWords = 0
    
    for line in passage:
        
        firstSum = 0
        words = line.split()
        
        for word in words:
            firstSum += len(word)
            
        firstAvg = firstSum/len(words)
        avgOfWords += firstAvg
        
    avg = avgOfWords / len(passage)
    return avg

# number of contractions in passage
def contractions( passage ):
    
    numContract = 0
    
    for line in passage:
        
        words = line.split()
        
        for word in words:
            if (word.lower() in c):
                numContract += 1
                
    return numContract
            
def Extract(filename):

	passage = extracting(filename)

	featureVector = [sentLength(passage), wordLength(passage), contractions(passage)]
	return featureVector