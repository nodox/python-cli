# Python Command Line Tool

This programs reads in records from various input files and then outputs the list with command line options to sort or filter them.

Input file format:

pipe:
First name | Last name | Book Title | Book Publication Date

slash:
Book Publication Date/First name/Last name/Book Title

csv:
Book Title, Last Name, First name, Book Publication Date


Here is the program signature:

usage: books.py [-h] [--filter FILTER] [--year] [--reverse]

Pick each flag on at a time