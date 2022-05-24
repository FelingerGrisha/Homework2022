totalStrLiterals = 0
totalEncodedStr = 0

with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

for line in InputData:
    line.strip()

    totalStrLiterals += len(line)

    countOfChars = 2

    for char in line:
        if char in ('"', "\\"):
            countOfChars += 2
        else:
            countOfChars += 1

    totalEncodedStr += countOfChars

with open("output2.txt", "w") as oFile:
    oFile.write(str(totalEncodedStr - totalStrLiterals))
