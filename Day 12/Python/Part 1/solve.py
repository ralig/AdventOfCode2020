from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

directions = ["N","E","S","W"]
degrees = [0,90,180,270,360]

loc = [0,0]
currDir = 1   #refers to location in directions

def moveDir(direction, amount):
    if direction == "E":
        return [amount,0]
    elif direction == "W":
        return [-amount,0]
    elif direction == "N":
        return [0,amount]
    elif direction == "S":
        return [0,-amount]

def turnShip(direction, amount):
    if direction == "L":
        return -(degrees.index(amount))
    else:
        return degrees.index(amount)
    

with path.open("rt") as f:
    while (True):
        data = f.readline().strip("\n")
        if not data:
            break
        instr = data[0]
        amt = int(data[1:])

        if instr in directions:
            tmp = moveDir(instr,amt)
            loc[0] += tmp[0]
            loc[1] += tmp[1]
        elif instr == "F":
            tmp = moveDir(directions[currDir],amt)
            loc[0] += tmp[0]
            loc[1] += tmp[1]
        elif instr == "L" or instr == "R":
            currDir += turnShip(instr,amt)
            if currDir < 0:
                currDir += 4
            if currDir > 3:
                currDir -= 4
            pass
print (abs(loc[0]) + abs(loc[1]))