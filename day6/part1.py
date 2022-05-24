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
        partOfLights.append("off")
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
                lights[numbersOfStrs[0]][nC] = "on"
        else:
            for nS in range(numbersOfStrs[0], numbersOfStrs[1] + 1):
                for nC in range(numbersOfColumns[0], numbersOfColumns[1] + 1):
                    lights[nS][nC] = "on"

    if "turn off" in line:
        parts_of_line = line.strip().split(" ")

        del parts_of_line[0]
        del parts_of_line[0]
        del parts_of_line[1]

        numbersOfColumns, numbersOfStrs = extractorNumber(parts_of_line)

        if numbersOfStrs[0] == numbersOfStrs[1]:
            for nC in range(len(lights[numbersOfStrs[0]]) + 1):
                lights[numbersOfStrs[0]][nC] = "off"
        else:
            for nS in range(numbersOfStrs[0], numbersOfStrs[1] + 1):
                for nC in range(numbersOfColumns[0], numbersOfColumns[1] + 1):
                    lights[nS][nC] = "off"

    if "toggle" in line:
        parts_of_line = line.strip().split(" ")

        del parts_of_line[0]
        del parts_of_line[1]

        numbersOfColumns, numbersOfStrs = extractorNumber(parts_of_line)

        if numbersOfStrs[0] == numbersOfStrs[1]:
            for nC in range(len(lights[numbersOfStrs[0]])):

                if lights[numbersOfStrs[0]][nC] == "off":
                    lights[numbersOfStrs[0]][nC] = "on"

                elif lights[numbersOfStrs[0]][nC] == "on":
                    lights[numbersOfStrs[0]][nC] = "off"
        else:
            for nS in range(numbersOfStrs[0], numbersOfStrs[1] + 1):
                for nC in range(numbersOfColumns[0], numbersOfColumns[1] + 1):

                    if lights[nS][nC] == "off":
                        lights[nS][nC] = "on"

                    elif lights[nS][nC] == "on":
                        lights[nS][nC] = "off"

countOfOn = 0

nS = 0
nC = 0

for nS in range(1000):
    for nC in range(1000):
        if lights[nS][nC] == "on":
            countOfOn += 1

with open("output1.txt", "w") as oFile:
    oFile.write(str(countOfOn))

