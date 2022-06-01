import re

with open("input.txt", "r") as iFile:
    InputData = iFile.read()

suma = 0

with open('output1.txt', 'w') as oFile:
    for x in re.findall('-?[0-9]+', InputData):
        suma += int(x)

    oFile.write(str(suma))
