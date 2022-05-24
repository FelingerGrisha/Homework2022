with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

count_of_niceStr = 0

for strOfInDa in InputData:

    countRP = 0
    countRL = 0

    for i in range(len(strOfInDa) - 1):
        pair = strOfInDa[i] + strOfInDa[i+1]
        if ((strOfInDa.find(pair) != strOfInDa.rfind(pair)) and (abs(strOfInDa.find(pair) - strOfInDa.rfind(pair)) >= 2)):
            countRP += 1

    for i in range(len(strOfInDa)):
        for j in range(len(strOfInDa)):
            if (strOfInDa[i] == strOfInDa[j]) and (abs(i - j) == 2):
                countRL += 1

    if ((countRP >= 1) and (countRL >= 1)):
        count_of_niceStr += 1


with open("output2.txt", "w") as oFile:
    oFile.write(str(count_of_niceStr))