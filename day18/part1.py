with open('input.txt', 'r') as iFile:
    InputData = iFile.read().split('\n')

consistLigths = [[1 if x == "#" else 0 for x in line] for line in InputData]
count = len(consistLigths)

def switch(curr):
    def get_neighbor(row, col):
        if 0 <= row < count and 0 <= col < count:
            return curr[row][col]
        else:
            return 0

    def count_neighbor(row, col):
        sum = -curr[row][col]
        for i in range(-1, 2):
            for j in range(-1, 2):
                sum += get_neighbor(row + i, col + j)
        return sum

    def rule(row, col):
        state, neighbor = curr[row][col], count_neighbor(row, col)
        if state == 1 and neighbor in (2, 3):
            return 1
        elif state == 0 and neighbor == 3:
            return 1
        return 0
    return [[rule(row, col) for col in range(count)] for row in range(count)]


for i in range(100):
    consistLigths = switch(consistLigths)

with open('output1.txt', 'w') as oFile:
    oFile.write(str(sum(sum(row) for row in consistLigths)))