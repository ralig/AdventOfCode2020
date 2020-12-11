from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()


def calcSums(start, length):
    sums = []
    for x in range(start,start+length-1):
        for y in range(x+1, start+length):
            sums.append(int(data[x])+int(data[y]))
    return sums

def FindWrongSum(preambleLen):
    for x in range(preambleLen,len(data)):
        sums = calcSums(x-preambleLen,preambleLen)
        if (int(data[x]) in sums):
            continue
        else:
            return data[x]
    return 0


preambleLen = 25
print(FindWrongSum(preambleLen))