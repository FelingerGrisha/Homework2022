import json

with open('input.txt') as iFile:
    InputData = json.load(iFile)

def sumOfItem(item):

    if isinstance(item, list):
        return sum([sumOfItem(i) for i in item])

    if isinstance(item, dict):
        if 'red' in item.values():
            return 0
        return sum([sumOfItem(i) for i in item.values()])

    if isinstance(item, str):
        return 0

    if isinstance(item, int):
        return item

with open('output2.txt', 'w') as oFile:
    oFile.write(str(sumOfItem(InputData)))
