totalStrliterals = 0
totalCharsInMemory = 0

with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

for line in InputData:

    line.strip()

    s = line[1:-1]
    countOfChars = i = 0

    while i < len(s):
        countOfChars += 1

        if s[i] == "\\":
            if s[i+1] == "x":
                i += 4
            else:
                i += 2
        else:
            i += 1

    totalStrliterals += len(line)
    totalCharsInMemory += countOfChars

with open("output1.txt", "w") as oFile:
    oFile.write(str(totalStrliterals - totalCharsInMemory))