with open("input.txt", "r") as iFile:
    InputData = iFile.readlines()

vowels = "aeiou"
prohibited_strs = ["ab", "cd", "pq", "xy"]
count_of_niceStr = 0

for string in InputData:

    string.strip()
    countV = 0
    countS = 0
    not_contain = False

    for vowel in vowels:

        for letter in string:

            if vowel == letter:
                countV += 1

    for i in range(len(string)):
        for j in range(len(string)):
            if (string[i] == string[j]) and (abs(i - j) == 1) and (i != j):
                countS += 1

    for prohibited_str in prohibited_strs:
        if prohibited_str in string:
            break
    else:
        not_contain = True

    if ((countV >= 3) and (countS >= 1) and (not_contain == True)):
        count_of_niceStr += 1

with open("output1.txt", "w") as oFile:
    oFile.write(str(count_of_niceStr))
