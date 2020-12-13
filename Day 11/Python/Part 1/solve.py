from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

rows = []
with path.open("rt") as f:
    rows = f.readlines()

for x in range(0,len(rows)):
    rows[x] = rows[x].strip()

newRows = rows.copy()

def countSeatsAdjacent(seatX,seatY, typeToCount):
    countEmpty = 0
    countOcc = 0
    for y in range(seatY-1,seatY+2):
        if (y > -1) and (y < len(rows)):
            for x in range(seatX-1,seatX+2):
                if (x > -1) and (x < len(rows)):
                    if not((x == seatX) and (y == seatY)):
                        if rows[x][y] == "L":
                            countEmpty += 1
                        elif (rows[x][y] == "#"):
                            countOcc += 1
    if typeToCount == "Empty":
        return countEmpty
    elif typeToCount == "Occ":
        return countOcc


def determineNewSeatState(seatX, seatY):
    if rows[seatX][seatY] == "L":
        occ = countSeatsAdjacent(seatX,seatY,"Occ")
        if occ == 0:
            tmp = list(newRows[seatX])
            tmp[seatY] = "#"
            newRows[seatX] = "".join(tmp)
    elif rows[seatX][seatY] == "#":
        occ = countSeatsAdjacent(seatX,seatY,"Occ")
        if occ >= 4:
            tmp = list(newRows[seatX])
            tmp[seatY] = "L"
            newRows[seatX] = "".join(tmp)

#main
while True: 
    for x in range(0,len(rows)):
        for y in range(0,len(rows[x])):
            determineNewSeatState(x,y)
    if rows != newRows:
        rows = newRows.copy()
    else:
        break

#count occ seats
answer = 0
for row in newRows:
    answer += row.count("#")


path = Path(__file__).parent / "../../output.txt"
with path.open("wt") as f:
    for row in newRows:
        f.write(row + "\n")

with path.open("rt") as f:
    s= f.read()


print(answer)