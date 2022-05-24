data = {}
results = {}

def get_value(item):
    if item in data:
        return int(results[item])
    else:
        return int(item)

def decideEquation(expression):
    if len(expression) == 1:
        return get_value(expression[0])
    if len(expression) == 2:
        return ~get_value(expression[1])
    elif len(expression) == 3:
        in_1 = get_value(expression[0])
        in_2 = get_value(expression[2])

        if expression[1] == "AND":
            return int(f"{in_1 & in_2:016b}", 2)
        elif expression[1] == "OR":
            return int(f"{in_1 | in_2:016b}", 2)
        elif expression[1] == "LSHIFT":
            return int(f"{in_1 << in_2:016b}", 2)
        elif expression[1] == "RSHIFT":
            return int(f"{in_1 >> in_2:016b}", 2)

with open("input.txt", "r") as iFile:
    InputData = iFile.read()

for equation in InputData.splitlines():
    expression, wire = equation.split(" -> ")
    data[wire] = expression.split()

keys = set(data.keys())

while keys:
    for key in keys.copy():
        try:
            results[key] = decideEquation(data[key])
            keys.remove(key)
        except KeyError:
            continue

with open("output1.txt", "w") as oFile:
    oFile.write(str(results["a"]))