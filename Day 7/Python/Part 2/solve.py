from pathlib import Path
path = Path(__file__).parent / "../../sample.txt"

data = []
with path.open("rt") as f:
    data = f.readlines()

def recurseBag(bags, name):
    pass

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

for k, v in allBags[myBag]:
    count *= v
    for j,u in allBags[k]

for k,v in allBags.items():
    if k != myBag:
        found += checkBag(allBags,myBag,k)
print (found)