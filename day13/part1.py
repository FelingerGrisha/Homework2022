import itertools, math

HappinesFromPair = dict()
names = set()

with open('input.txt', 'r') as iFile:
    InputData = iFile.read()

for string in InputData.split('\n'):
    a, _, dr, sz, _, _, _, _, _, _, b = string[:-1].split(' ')
    names.add(b)
    if dr == "gain":
        HappinesFromPair[(a, b)] = int(sz) * 1
    else:
        HappinesFromPair[(a, b)] = int(sz) * -1

best = -math.inf

for combinations in itertools.permutations(list(names)):
    cost = HappinesFromPair[(combinations[0], combinations[-1])] + HappinesFromPair[(combinations[-1], combinations[0])]
    for a, b in zip(combinations[:-1], combinations[1:]):
        cost += HappinesFromPair[(a, b)] + HappinesFromPair[(b, a)]

    if cost > best:
        best = cost


with open('output1.txt', 'w') as oFile:
    oFile.write(str(best))
