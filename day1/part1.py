with open("input.txt", "r") as iFile:
    InputData = iFile.read()

floor = 0

for i in InputData:
    if i == "(":
        floor += 1

    if i == ")":
        floor -= 1

with open("output1.txt", "w") as oFile:
    oFile.write(str(floor))

