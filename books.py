"""
Author: Steven Natera
Python Version: 2.7.5

README:
	This was fun! 

	Unfortunately I did not program logic if multiple flags 
	were entered onto the command line. The brute-force approach would be 
	to write if statements with all the permutations of flag orders. I figured
	if I couldn't come up with a better solution than I was probably going in 
	the wrong direction so I opted to leave it out.

	I also want to recognize that its not ideal to create files
	in order to have a working program but I just went with 
	that idea to complete the task.

	Thank you!

"""

import argparse
import subprocess


def createSortedOutput():
	""" Generates a files of book informations sorted by author last names.
	File output structure is formatted with the awk command line tool. """

	with open('unsorted_output.txt', 'w') as f:
		slashFile = subprocess.check_output(['awk', '{print $3, $2, $4, $1}', 'FS=/', 'OFS=, ', 'slash'])
		csvFile = subprocess.check_output(['awk', '{print $2, $3, $1, $4}', 'FS=,', 'OFS=, ', 'csv'])
		pipeFile = subprocess.check_output(['awk', '{print $2, $1, $3, $4}', 'FS=|', 'OFS=, ', 'pipe'])

		f.write(slashFile)
		f.write(csvFile)
		f.write(pipeFile)
		f.close()

	with open('sorted_output.txt', 'w') as f:
		subprocess.Popen(['sort', '-t,', '-k1,1', 'unsorted_output.txt'], stdout=f)	
		


def createCLI():
	""" Creates the command line interface with possible arguments """

	parser = argparse.ArgumentParser(description='Show a list of books, alphabetical ascending by author\'s last name')

	parser.add_argument('--filter', help='show subset of books, looks for the argument as a substring of any of the fields')
	
	parser.add_argument('--year', help='sort the books by year, ascending instead of default sort', action='store_true')
	
	parser.add_argument('--reverse', help='reverse sort', action='store_true')
	
	args = parser.parse_args()
	
	return args

def main():
	""" Runs command line logic. 
	Does not hadle logic if multiple flags are placed """

	createSortedOutput()
	args = createCLI()

	if args.filter:
		subprocess.Popen(['grep', str(args.filter), 'sorted_output.txt'])
	elif args.year:
		subprocess.Popen(['sort', '-t,', '-k4,4', 'sorted_output.txt'])
	elif args.reverse:
		subprocess.Popen(['sort', '-t,', '-r', '-k4,4', 'sorted_output.txt'])
	else:
		with open('sorted_output.txt', 'r') as f:
			print f.read()
			f.close()
		






if __name__ == "__main__":
	main()
