import re

from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

class ruledef():
    def __init__(self, name, rules):
        self.name = name # ""
        self.rules = rules # []

data = []
with path.open("rt") as f:
    data = f.readlines()

#rules = [[[#,rule]]]
#rules[x][y][0] = rule amt
#rules[x][y][1] = type

def findruleLocs(name):
    if name.endswith('s'):
        name = name[:-1]
    counts = []
    count = 0
    for rule in rules:
        for item in rule:
            if item[1].startswith(name):
                #count = location of rule/type
                counts.append(count)
        count += 1
    return counts
locs = []
def findTopLevelRules(name, locstmp, iteration):
    if (iteration == 0):
        locstmp.clear()
    locstmp.append(findruleLocs(name))
    for num in locstmp[iteration]:
        locs.append(findTopLevelRules(types[num],locstmp,iteration+1))
    if locstmp[iteration] == []:
        iteration = 0
        return locstmp

types = []
rules = []
for rule in data:
    tmp = rule.split(" contain ")
    tmpPred = tmp[1].split(", ")
    subj = tmp[0]
    tmpPred[len(tmpPred)-1] = tmpPred[len(tmpPred)-1].strip(".\n")
    pred = []
    for x in range(0,len(tmpPred)):
        pred.append([tmpPred[x][0], tmpPred[x][2:]])
    types.append(subj)
    rules.append(pred)

findTopLevelRules("shiny gold bag",[],0)

colors = []
count = 0
for items in locs:
    count += 1
    if (items != None):
        for item in items:
            if isinstance(item,list):
                for i in item:
                    if colors.count(i) == 0:
                        colors.append(i)
            elif colors.count(item) == 0:
                colors.append(item)        
print(len(colors))