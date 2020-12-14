from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

startTimestamp = 0
with path.open("rt") as f:
    data = f.readlines()

startTimestamp = int(data[0].strip("\n"))
busesRaw = data[1].strip("\n").split(",")
buses = []

for x in range(0,len(busesRaw)):
    if busesRaw[x].isnumeric():
        buses.append([int(busesRaw[x]),x])

#sort buses
buses.sort(reverse=True)

#find first possible ts
currentTimestamp = startTimestamp
found = False
while not found:
    if ((currentTimestamp + buses[0][1]) % buses[0][0]) == 0:
        found = True
    else:
        currentTimestamp += 1

largestCount = 0
while (True):
    count = 0
    for bus in buses:
        if ((currentTimestamp + bus[1]) % bus[0]) != 0:
            break
        else:
            count += 1
    if count == len(buses):
        break
    if count > largestCount:
        largestCount = count
    currentTimestamp += buses[0][0]
print(currentTimestamp)
pass