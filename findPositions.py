from typing import List, Tuple, Set

def hammingDistance(first, second):
	distance = 0
	
	for i in range(0, len(first)):
		if first[i] != second[i]:
			distance += 1
	
	return distance

def reverseCompliment(dnaString: str) -> str:
	newString = ""
	
	for i in dnaString:
		if i == "A":
			newString = "T" + newString
		elif i == "C":
			newString = "G" + newString
		elif i == "G":
			newString = "C" + newString
		elif i == "T":
			newString = "A" + newString
	
	return newString

def lowestHamming(kMer: str, dnaString: List[str]) -> int:
	lowestScore = len(kMer)
	
	for i in range(0, len(dnaString)-len(kMer)):
		forward = hammingDistance(kMer, dnaString[i:i+len(kMer)])
		reverse = hammingDistance(reverseCompliment(kMer), dnaString[i:i+len(kMer)])
		if forward < reverse:
			score = forward
		else:
			score = reverse
		if score < lowestScore:
			lowestScore = score
			position = i
		
	
	return position

def findPosition(searchkMer: int, dnaArray: List[str]) -> List[int]:
	
	kMerPositions = []
	
	for dna in dnaArray:
		kMerPositions.append(lowestHamming(searchkMer, dna)+1)
	
	return kMerPositions
