from itertools import permutations

with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

places = set()
distances = {}

for line in InputData:
    split_line = line.split(" ")
    start, end = split_line[0], split_line[2]
    places.add(start)
    places.add(end)
    distances[start + end] = int(split_line[4])
    distances[end + start] = int(split_line[4])

longest = 0

for combination in permutations(places):
    length = 0
    for firstPlace, secondPlace in zip(combination[:-1], combination[1:]):
        length += distances[firstPlace + secondPlace]
    if length > longest:
        longest = length

with open("output2.txt", "w") as oFile:
    oFile.write(str(longest))
