from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()

for x in range(0,len(data)):
    data[x] = int(data[x])
data.sort()

diff1 = 0
diff3 = 0
for x in range(1,len(data)):
    if (data[x] - data[x-1] == 1):
        diff1 += 1
    elif(data[x] - data[x-1] == 3):
        diff3 += 1
print((diff1+1)*(diff3+1))