with open("input.txt", "r") as iFile:
    InputData = iFile.read()

floor = 0
i = 0

while floor != -1:
    if InputData[i] == "(":
        floor += 1

    if InputData[i] == ")":
        floor -= 1

    i += 1

with open("output2.txt", "w") as oFile:
    oFile.write(str(i))
