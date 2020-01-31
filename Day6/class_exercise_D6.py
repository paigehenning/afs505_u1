def main():
	from sys import argv
	script, filename = argv
	filehand=open(filename) #Need indent to make local not global
	linecount = 0
	wordcount=0
	charactercount=0
	line =filehand.readline()
	while line:
		linecount+=1
		charactercount+=len(line)
		words=str.split(line)			#splits string into an array
		wordcount+=len(words)			#using the len we can now count objects in array
		line=filehand.readline()
	print(f"You have ",linecount,"lines")
	print(f"You have ",wordcount," words")
	print(f"You have ",charactercount," characters")
	print(f"The name of your file is ",filename)
	
	
main()
