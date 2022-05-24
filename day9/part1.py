import sys
from itertools import permutations

with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

places = set()
distances = dict()

for line in InputData:
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

shortest = sys.maxsize

for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)

with open("output1.txt", "w") as oFile:
    oFile.write(str(shortest))