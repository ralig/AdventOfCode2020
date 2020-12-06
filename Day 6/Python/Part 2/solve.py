from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()


def findInData(toFind, start):
    lastLine = start
    for x in range(start,len(data)):
        if data[x] == toFind:
            return x
        lastLine = x
    if lastLine == len(data)-1:
        return len(data)
    return False

answer = 0

first = 0 #first entry in group
last = 0  #last entry in group
last = findInData("\n",first) - 1
all4 = ""

while(last != -1):
    data[first] = data[first].replace("\n","")
    for letter in data[first]:

        foundCount = 0
        for x in range(first+1, last+1):
            if (letter in data[x]):
                foundCount += 1
        if foundCount == last-first:
            answer += 1
        
    first = last+2
    last = findInData("\n",first) - 1
        
print(answer)