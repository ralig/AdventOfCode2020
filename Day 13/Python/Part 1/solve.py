from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

startTimestamp = 0
with path.open("rt") as f:
    startTimestamp = int(f.readline().strip("\n"))
    buses = f.readline().replace(",x","").strip("\n").split(",")

foundBus = 0
ts = startTimestamp
while foundBus == 0:
    for bus in buses:
        if (ts % int(bus)) == 0:
            foundBus = int(bus)
            break
    ts += 1

print(foundBus * (ts-1-startTimestamp))

