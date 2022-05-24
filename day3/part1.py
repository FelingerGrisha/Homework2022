with open("input.txt", "r") as iFile:
    InputData = iFile.read()

coords = [[0, 0]]
i = 0
j = 0

while i != len(InputData):
    if InputData[i] == ">":
        coords.append([coords[i][0] + 1, coords[i][1]])
    if InputData[i] == "<":
        coords.append([coords[i][0] - 1, coords[i][1]])
    if InputData[i] == "^":
        coords.append([coords[i][0], coords[i][1] + 1])
    if InputData[i] == "v":
        coords.append([coords[i][0], coords[i][1] - 1])

    i += 1

while j != len(coords):
    for k in range(j):
        if (coords[j][0] == coords[k][0]) and (coords[j][1] == coords[k][1]) and (j != k):
            del coords[k]
            j -= 1
    j += 1

with open("output1.txt", "w") as oFile:
    oFile.write(str(len(coords)))
