from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()

def bootComp(codes):
    visitedLoc = []
    loc = 0
    accum = 0
    isLoop = True
    while not(loc in visitedLoc) and isLoop:
        if loc == len(codes)-1:
            isLoop = False

        visitedLoc.append(loc)
        opCode = data[loc][:3]
        if opCode == 'acc':
            accum += int(data[loc].split(" ")[1])
            loc += 1
        elif opCode == 'jmp':
            loc += int(data[loc].split(" ")[1])
        elif opCode == 'nop':
            loc += 1
    return [isLoop,accum]

def changeCode(line):
    if line[:3] == 'jmp':
        line = "nop" + line[3:]
    elif data[x][:3] == 'nop':
        line = "jmp" + line[3:]
    else:
        line = ""
    return line


result = [True,0]
for x in range(0,len(data)):
    line = changeCode(data[x])
    if line == "":
        continue
    else:
        data[x] = line
    result = bootComp(data)
    if not(result[0]):
        break
    #change it back!
    data[x] = changeCode(data[x])

print(result[1])