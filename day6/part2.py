with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()


def extractorNumber(splitStr):
    coord_switchConsist = splitStr[0].split(",")
    coord_throught = parts_of_line[1].split(",")

    numbersOfColumns = [int(coord_switchConsist[0]), int(coord_throught[0])]
    numbersOfStrs = [int(coord_switchConsist[1]), int(coord_throught[1])]

    return numbersOfColumns, numbersOfStrs


lights = []

for i in range(1000):
    partOfLights = []
    for j in range(1000):
        partOfLights.append(0)
    lights.append(partOfLights)

for line in InputData:
    if "turn on" in line:
        parts_of_line = line.strip().split(" ")

        del parts_of_line[0]
        del parts_of_line[0]
        del parts_of_line[1]

        numbersOfColumns, numbersOfStrs = extractorNumber(parts_of_line)

        if numbersOfStrs[0] == numbersOfStrs[1]:
            for nC in range(len(lights[numbersOfStrs[0]]) + 1):
                lights[numbersOfStrs[0]][nC] += 1
        else:
            for nS in range(numbersOfStrs[0], numbersOfStrs[1] + 1):
                for nC in range(numbersOfColumns[0], numbersOfColumns[1] + 1):
                    lights[nS][nC] += 1

    if "turn off" in line:
        parts_of_line = line.strip().split(" ")

        del parts_of_line[0]
        del parts_of_line[0]
        del parts_of_line[1]

        numbersOfColumns, numbersOfStrs = extractorNumber(parts_of_line)

        if numbersOfStrs[0] == numbersOfStrs[1]:
            for nC in range(len(lights[numbersOfStrs[0]]) + 1):
                if (lights[numbersOfStrs[0]][nC] - 1) >= 0:
                    lights[numbersOfStrs[0]][nC] -= 1
        else:
            for nS in range(numbersOfStrs[0], numbersOfStrs[1] + 1):
                for nC in range(numbersOfColumns[0], numbersOfColumns[1] + 1):
                    if (lights[nS][nC] - 1) >= 0:
                        lights[nS][nC] -= 1

    if "toggle" in line:
        parts_of_line = line.strip().split(" ")

        del parts_of_line[0]
        del parts_of_line[1]

        numbersOfColumns, numbersOfStrs = extractorNumber(parts_of_line)

        if numbersOfStrs[0] == numbersOfStrs[1]:
            for nC in range(len(lights[numbersOfStrs[0]])):
                lights[numbersOfStrs[0]][nC] += 2
        else:
            for nS in range(numbersOfStrs[0], numbersOfStrs[1] + 1):
                for nC in range(numbersOfColumns[0], numbersOfColumns[1] + 1):
                    lights[nS][nC] += 2

totalBrightness = 0

nS = 0
nC = 0

for nS in range(1000):
    for nC in range(1000):
        totalBrightness += lights[nS][nC]

with open("output2.txt", "w") as oFile:
    oFile.write(str(totalBrightness))