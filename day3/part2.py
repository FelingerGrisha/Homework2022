with open("input.txt", "r") as iFile:
    InputData = iFile.read()

coordsS = [[0, 0]]
coordsRS = [[0, 0]]
i = 0
j = 0
d = 0
t = 0

while i != len(InputData):

    if InputData[i] == ">":
        if (i % 2 == 0):
            coordsS.append([coordsS[len(coordsS) - 1][0] + 1, coordsS[len(coordsS) - 1][1]])
        if (i % 2 != 0):
            coordsRS.append([coordsRS[len(coordsRS) - 1][0] + 1, coordsRS[len(coordsRS) - 1][1]])
    if InputData[i] == "<":
        if (i % 2 == 0):
            coordsS.append([coordsS[len(coordsS) - 1][0] - 1, coordsS[len(coordsS) - 1][1]])
        if (i % 2 != 0):
            coordsRS.append([coordsRS[len(coordsRS) - 1][0] - 1, coordsRS[len(coordsRS) - 1][1]])
    if InputData[i] == "^":
        if (i % 2 == 0):
            coordsS.append([coordsS[len(coordsS) - 1][0], coordsS[len(coordsS) - 1][1] + 1])
        if (i % 2 != 0):
            coordsRS.append([coordsRS[len(coordsRS) - 1][0], coordsRS[len(coordsRS) - 1][1] + 1])
    if InputData[i] == "v":
        if (i % 2 == 0):
            coordsS.append([coordsS[len(coordsS) - 1][0], coordsS[len(coordsS) - 1][1] - 1])
        if (i % 2 != 0):
            coordsRS.append([coordsRS[len(coordsRS) - 1][0], coordsRS[len(coordsRS) - 1][1] - 1])

    i += 1

while j != len(coordsS):
    for k in range(j):
        if (coordsS[j][0] == coordsS[k][0]) and (coordsS[j][1] == coordsS[k][1]) and (j != k):
            del coordsS[k]
            j -= 1
    j += 1

while d != len(coordsRS):
    for p in range(d):
        if (coordsRS[d][0] == coordsRS[p][0]) and (coordsRS[d][1] == coordsRS[p][1]) and (d != p):
            del coordsRS[p]
            d -= 1
    d += 1

while t != len(coordsS):
    for q in range(len(coordsRS)):
        if (coordsS[t][0] == coordsRS[q][0]) and (coordsS[t][1] == coordsRS[q][1]):
            del coordsS[t]
            t -= 1
            break
    t += 1


with open("output2.txt", "w") as oFile:
    oFile.write(str(len(coordsS) + len(coordsRS)))
