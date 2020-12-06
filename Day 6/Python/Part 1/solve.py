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
yeses = []

while(last != -1):
    for x in range(first, last+1):
        for letter in data[x]:
            if not(letter in yeses):
                yeses.append(letter)
    
    answer+= len(yeses) - 1 #subtract one to compensate for \n
    yeses = []
    first = last+2
    last = findInData("\n",first) - 1
        
print(answer)