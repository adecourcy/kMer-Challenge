from typing import List, Tuple, Set
from kManipulation import createInitialkMers, expandkMers, trimkMers
from findScores import findScores, reverseCompliment
from findPositions import findPosition
from math import ceil
from sys import argv

###############################################################################
#
# This program's parser for command line arguments is very feeble, so be
# careful. At the command line this program must be given a file name for a
# file in the Fast A format, the length of the median k-mer you are attempting
# to find, and the maximum distance an implanted k-mer can be from the median
# string.
#
# Additional, optional, arguments are available. They are listed in the order
# they must be passed to the program. Unfortunately, because of limited time,
# if you wish to modify the optional argument 5, you must pass a value for the
# optional argument 4.
#
# This program implements a branch and bound algorithm that starts with a
# k-mer size 6, however given an integer it can start with a k-mer of any size.
#
# This program expects that a k-mer will be present in 85% of the dna strings
# it is given, however this can be modified by passing an integer between 1
# and 100.
#
# This program keeps only the highest scoring 50% of k-mers by default.
# However, this can be modified by passing and integer between 1 and 100.
#
###############################################################################

def main(dnaStrings: List[str], lengthkMer: int, maxDistances: int, startingSize: int=6, expectedMissing: int=85, trim: int=50) -> str:
	
	expansionIterations = lengthkMer - startingSize
	
	numDnaStrings = len(dnaStrings)
	predictedMissing = numDnaStrings - ceil(numDnaStrings * (expectedMissing / 100))
	minScore = (numDnaStrings - predictedMissing) * maxDistances + (predictedMissing * ceil(0.8 * lengthkMer))
	
	searchSpace = createInitialkMers(startingSize)[1]
	
	for i in range(0, expansionIterations):
		scoredkMers = trimkMers(findScores(searchSpace, dnaStrings), minScore, trim)
		toExpand = []
		for k in scoredkMers:
			toExpand.append(reverseCompliment(k[0]))
			toExpand.append(k[0])
		(waste, searchSpace) = expandkMers(toExpand)
	
	scoredkMers = trimkMers(findScores(searchSpace, dnaStrings), minScore, trim)
	positions = findPosition(scoredkMers[0][0], dnaStrings)
	
	outputString = "Kmer Positions = " + str(positions)[1:-1]
	outputString += "\nMedian String = " + scoredkMers[0][0] + ", Score: " + str(scoredkMers[0][1])
	
	print(outputString)

def strToArray(fileName):
  dna = open(fileName)
  dnaStrings = []
  for line in dna:
    dnaStrings.append(line.replace("\n",""))
  return dnaStrings	

def fastAtoList(fileName):
  fastA = open(fileName)
  dnaStrings = []
  stringIndex = -1
  for line in fastA:
    if ">" in line:
      dnaStrings.append("")
      stringIndex += 1
    else:
      dnaStrings[stringIndex] += line.replace("\n","")
   
  return dnaStrings

if __name__ == "__main__":
	args = [int(x) for x in argv[2:]]
	main(fastAtoList(argv[1]), *args)
		
