import math
from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

def FindRowOrCol(minSeatNum, maxSeatNum, info):
    if info == "":
        return minSeatNum
    elif (info[0] == "F") or (info[0] == "L"):
        info2 = info[1:]
        return FindRowOrCol(minSeatNum,((minSeatNum+maxSeatNum)//2),info2)
    elif (info[0] == "B") or (info[0] == "R"):
        info2 = info[1:]
        return FindRowOrCol(math.ceil((minSeatNum+maxSeatNum)/2),maxSeatNum,info2)
    

Seats = []
with path.open("rt") as f:
    data = "a"
    while(data):
        data = f.readline().replace("\n","")
        row = FindRowOrCol(0, 127, data[:-3])
        col = FindRowOrCol(0, 7, data[-3:])
        Seats.append((row*8)+col)

highest = 0
for seat in Seats:
    if seat > highest:
        highest = seat
print(highest)