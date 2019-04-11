from typing import List, Tuple, Set
from findScores import reverseCompliment

def createInitialkMers(k: int) -> Tuple[List[str], Set[str]]:
	startkMers = (["A", "T", "C", "G"], set())
	
	for i in range(0, k-1):
		startkMers = expandkMers(startkMers[0])
		
	return startkMers

def expandkMers(kMers: List[str]) -> Tuple[List[str], Set[str]]:
	nucleotides = ["A", "T", "C", "G"]
	newkMers = []
	reverseCompliments = set()
	
	for k in kMers:
		for n in nucleotides:
			nextkMer = k + n
			if nextkMer in reverseCompliments:
				pass
			else:
				reverseCompliments.add(reverseCompliment(nextkMer))
			newkMers.append(nextkMer)
	
	return (newkMers, reverseCompliments)

def binSearch(kMerList: List[Tuple[str, int]], score, beginList: int, endList: int) -> int:
	
	if (endList - beginList) == 1:
		return beginList
	
	checkNext = (beginList + endList) // 2
	if kMerList[checkNext][1] == score:
		return checkNext
	elif kMerList[checkNext][1] < score:
		return binSearch(kMerList, score, checkNext, endList)
	else:
		return binSearch(kMerList, score, beginList, checkNext)
	

def trimkMers(kMerList: List[Tuple[str, int]], minScore: int, trim: int=50) -> List[Tuple[str,int]]:
	kMerList.sort(key=lambda tup: tup[1])
	midPoint = len(kMerList) // (100 // trim)
	
	if kMerList[midPoint][1] < minScore:
		return kMerList[:midPoint+1]
	elif kMerList[midPoint][1] == minScore:
		cutOff = midPoint
	elif kMerList[midPoint][1] > minScore:
		cutOff = binSearch(kMerList, minScore, -1, midPoint)

	while True:
		if kMerList[cutOff + 1] == kMerList[cutOff]:
			cutOff += 1
		else:
			break
	
	return kMerList[:cutOff+1]
