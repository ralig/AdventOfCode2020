from pathlib import Path
path = Path(__file__).parent / "../../input.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()

def checkBag(bags, name, currBag):
    if currBag==name:
        return 1
    if bags.get(currBag) is None:
        return 0
    else:
        counts = []
        for k, v in bags[currBag].items():
            counts.append(checkBag(bags, name, k))
        return max(counts)

################

allBags = {}

for rule in data:
    tmp = rule.split(" contain ")
    tmpPred = tmp[1].split(", ")
    subj = " ".join(tmp[0].split(" ")[:-1])
    bag = {}
    for p in tmpPred:
        pred = " ".join(p.split(" ")[:-1])
        bag.update({pred[2:] : pred[0]})
    allBags[subj] = bag


#create list of dictionary

myBag = "shiny gold"
found = 0
for k,v in allBags.items():
    if k != myBag:
        found += checkBag(allBags,myBag,k)
print (found)