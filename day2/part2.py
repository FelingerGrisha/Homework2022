with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

TotalFeetOfRibbon = 0

def ribbonToWrap(parametrs: list):
    while len(parametrs) != 2:
        maxParametr = max(parametrs)
        del parametrs[parametrs.index(maxParametr)]
    return 2*parametrs[0] + 2*parametrs[1]

def ribbonToBow(parametrs: list):
       return parametrs[0] * parametrs[1] * parametrs[2]

for square in InputData:
    square = square.strip()

    splitStrParametrs = square.split("x")

    splitIntParametrs = list(map(int, splitStrParametrs))
    print(splitIntParametrs)

    TotalFeetOfRibbon += ribbonToBow(splitIntParametrs) + ribbonToWrap(splitIntParametrs)

with open("output2.txt", "w") as oFile:
    oFile.write(str(TotalFeetOfRibbon))
