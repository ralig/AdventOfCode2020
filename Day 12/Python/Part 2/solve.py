from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

directions = ["N","E","S","W"]
degrees = [0,90,180,270,360]

loc = [0,0]
waypoint = [10,1]

def moveWaypoint(direction, amount):
    if direction == "E":
        return [amount,0]
    elif direction == "W":
        return [-amount,0]
    elif direction == "N":
        return [0,amount]
    elif direction == "S":
        return [0,-amount]

def moveShip(amount):
    return [amount*waypoint[0],amount*waypoint[1]]

def rotateWaypoint(direction, amount):
    tmp = waypoint
    for x in range(0,degrees.index(amount)):
        if direction == "L":
            tmp = [-tmp[1],tmp[0]]
        else:
            tmp = [tmp[1],-tmp[0]]
    return tmp
    

with path.open("rt") as f:
    while (True):
        data = f.readline().strip("\n")
        if not data:
            break
        instr = data[0]
        amt = int(data[1:])

        if instr in directions:
            tmp = moveWaypoint(instr,amt)
            waypoint[0] += tmp[0]
            waypoint[1] += tmp[1]
        elif instr == "F":
            tmp = moveShip(amt)
            loc[0] += tmp[0]
            loc[1] += tmp[1]
        elif instr == "L" or instr == "R":
            waypoint = rotateWaypoint(instr,amt)
print (abs(loc[0]) + abs(loc[1]))