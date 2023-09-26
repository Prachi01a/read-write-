# in reading mode
with open("C:/Users/pnikhoria.ext/Documents/techno.txt", "r") as input:
	
	
	# file in write mode
	with open("C:/Users/pnikhoria.ext/Documents/techno.txt", "w") as output:
		
		# Writing each line from input file to
		# output file using loop
		for line in input:
			output.write(line)
