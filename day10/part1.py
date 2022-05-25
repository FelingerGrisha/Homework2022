with open("input.txt", "r") as iFile:
    InputData = iFile.read()

answer1 = InputData.strip()

for i in range(40):
    new = ''
    s = 0
    while s < len(answer1):
        c = answer1[s]
        n = 1
        s += 1
        while s < len(answer1) and answer1[s] == c:
            s += 1
            n += 1
        new += str(n) + str(c)
    answer1 = new

with open("output1.txt", "w") as oFile:
    oFile.write(str(len(answer1)))