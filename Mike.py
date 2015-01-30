def main():

	print "Please Enter a Filename to be parsed: "
	input_file_name = raw_input()
	print ""
	print "Currently Parsing '%s'...\n" %input_file_name

	input_file = open(input_file_name, "r+")
	contents = input_file.read()
	output_file_name = "Output_" + input_file_name
	output_file = open(output_file_name, "w")

	characters_total = 0
	characters_removed = 0

	for c in contents:
		characters_total += 1
		if c =='a' or c == 'b':
			characters_removed += 1
		else:
			output_file.write(c)
		
	input_file.close()
	output_file.close()

	print "%s of %s characters were removed from '%s'\n"%(characters_removed,characters_total, input_file_name)
	print "Output stored in file: '%s'\n"%output_file_name

if __name__ == "__main__": main()