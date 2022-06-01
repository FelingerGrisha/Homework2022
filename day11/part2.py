import string

englishAlphabet = string.ascii_lowercase

replicate = []

for x in englishAlphabet:
    replicate.append(x + x)

letterCombs = []

for x in zip(englishAlphabet[:-2], englishAlphabet[1:-1], englishAlphabet[2:]):
    partOfComb = "".join(x)
    letterCombs.append(partOfComb)

bToZAAlphabet = {}

for c1, c2 in zip(englishAlphabet, englishAlphabet[1:] + 'a'):
    bToZAAlphabet[c1] = c2


def is_valid(password):

    if 'i' in password or 'o' in password or 'l' in password:
        return False

    if sum([x in password for x in replicate]) < 2:
        return False

    if not any([x in password for x in letterCombs]):
        return False

    return True


def next_password(password):
    password = password[:-1] + bToZAAlphabet[password[-1]]
    for i in range(-1, -8, -1):
        if password[i] == 'a':
            password = password[:i-1] + bToZAAlphabet[password[i - 1]] + password[i:]
        else:
            break
    return password


with open('input.txt', 'r') as iFile:
    InputData = iFile.readline()

while not is_valid(InputData):
    InputData = next_password(InputData)

InputData = next_password(InputData)

while not is_valid(InputData):
    InputData = next_password(InputData)

with open('output2.txt', 'w') as oFile:
    oFile.write(InputData)