from hashlib import md5

with open("input.txt", "r") as iFile:
    InputData = iFile.read()

h = ""
i = 0
tmp = ""

while not h.startswith("000000"):

    tmp = InputData + str(i)
    h = md5(tmp.encode()).hexdigest()
    i += 1


with open("output2.txt", "w") as oFile:
    oFile.write(tmp[len(str(i)) + 1:])