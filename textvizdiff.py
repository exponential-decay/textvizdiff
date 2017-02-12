# -*- coding: utf-8 -*-

import os
import sys
import math
import argparse
import StringIO

off = "0"
onn = "+"
non = "x"

#Ultimately unecessary at first, but see where program goes...
MATCH = 0
NOMATCH = 1
EOF = 9

def drawtext(comparelist):

	sys.stderr.write("Diffs computed. Outputting text." + "\n")

	l1 = comparelist

	fill = ""
	linelen = 80

	#for each entry, create a new set of pixels, e.g. 10x10
	for i, x in enumerate(l1):

		if x == MATCH:
			fill = off
		if x == NOMATCH: 
			fill = onn
		if x == EOF:
			fill = non

		sys.stdout.write(fill)
	
		if (i+1)%linelen == 0:
			sys.stdout.write("\n")

	sys.stdout.write("\n")
	return

#only consider files of equal size...
def comparesize(f1, f2):
	if os.stat(f1).st_size != os.stat(f2).st_size:
		return False
	return True

def imagefiles(f1, f2):
	comparelist = []

	a = open(f1)
	b = open(f2)

	b1eof = False
	b2eof = False

	read = True
	while read:

		if b1eof is not True:
			b1 = a.read(1)
			if len(b1) == 0:
				b1eof = True

		if b2eof is not True:
			b2 = b.read(1)
			if len(b2) == 0: 
				b2eof = True

		if b1eof is True and b2eof is True:
			break

		if len(b1) == 0 or len(b2) == 0:
			comparelist.append(EOF)
		elif b1 != b2:
			comparelist.append(NOMATCH)
		elif b1 == b2:
			comparelist.append(MATCH)

	drawtext(comparelist)
	return

def main():

	#	Handle command line arguments for the script
	parser = argparse.ArgumentParser(description='Draw an image showing the difference between two files.')
	parser.add_argument('--f1', help='Mandatory: File 1.', default=False)
	parser.add_argument('--f2', help='Mandatory: File 2.', default=False)

	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit(1)

	#	Parse arguments into namespace object to reference later in the script
	global args
	args = parser.parse_args()

	if args.f1 and args.f2:
		imagefiles(args.f1, args.f2)
	else:
		parser.print_help()
		sys.exit(1)

if __name__ == "__main__":      
   main()
