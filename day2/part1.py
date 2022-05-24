with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

totalSquare = 0

def counterSquare(parametrs: list):
       squaresOfSides = [parametrs[0]*parametrs[1], parametrs[1]*parametrs[2], parametrs[0]*parametrs[2]]
       return squaresOfSides

for square in InputData:
    square = square.strip()

    splitStrParametrs = square.split("x")

    splitIntParametrs = list(map(int, splitStrParametrs))
    print(splitIntParametrs)

    extraPaper = min(counterSquare(splitIntParametrs))
    print(extraPaper)

    l, w, h = splitIntParametrs

    totalSquare += 2*l*w + 2*w*h + 2*h*l + extraPaper

with open("output1.txt", "w") as oFile:
    oFile.write(str(totalSquare))
