infile = "hey/testData.txt"
outfile = "hey/newData.txt"

fin = open(infile,"r")
fout = open(outfile, "w")

	newString=""
	for word in string.split():
		if not'>' in word and not'=' in word and not'{' in word and not'}' in word and not'<' in word and not'&' in word and not'\\' in word and not'/' in word and not'1' in word and not'2' in word and not'3' in word and not'4' in word and not'5' in word and not'6' in word and not'7' in word and not'8' in word and not'9' in word and not'0' in word and not'*' in word and not'@' in word and not'%' in word and not'[' in word and not']' in word:
			newString =(newString+word+" ")

	