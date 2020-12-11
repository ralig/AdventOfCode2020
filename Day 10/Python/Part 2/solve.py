from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()

for x in range(0,len(data)):
    data[x] = int(data[x])
data.sort()

waysToConnect = 0


def findBranches():
    sol = {0:1}
    for num in data:
        sol[num] = 0
        if num - 1 in sol:
            sol[num]+=sol[num-1]
        if num - 2 in sol:
            sol[num]+=sol[num-2]
        if num - 3 in sol:
            sol[num]+=sol[num-3]
    return sol

fb = findBranches()
print(fb[max(data)])


