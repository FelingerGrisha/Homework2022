with open('input.txt', 'r') as iFile:
    InputData = sorted(list(map(int, iFile.read().split('\n'))))

sizes = []


def sum_to(containers, goal, values_in_goal=0):

    if len(containers) == 0:
        return 0

    first = containers[0]
    tail = containers[1:]

    if first > goal:
        with_first = 0
    elif first == goal:
        sizes.append(values_in_goal + 1)
        with_first = 1
    else:
        with_first = sum_to(tail, goal - first, values_in_goal + 1)

    return with_first + sum_to(tail, goal, values_in_goal)


with open('output1.txt', 'w') as oFile:
    oFile.write(str(sum_to(InputData, 150)))