from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()

for x in range(0,len(data)):
    data[x] = int(data[x])

def findSum(matchNum):
    for x in range(0,len(data)):
        #add until sum = or > num
        sum = 0
        for y in range(x,len(data)):
            sum += data[y]
            if sum > matchNum:
                break
            elif sum == matchNum:
                return min(data[x:y]) + max(data[x:y])
    return 0

invalidNumber = 3199139634

print(findSum(invalidNumber))