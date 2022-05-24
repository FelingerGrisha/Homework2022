data = {}
results = {}

def get_value(item):
    if item in data:
        return int(results[item])
    else:
        return int(item)

def decideEquation(equation):
    if len(equation) == 1:
        return get_value(equation[0])
    if len(equation) == 2:
        return ~get_value(equation[1])
    elif len(equation) == 3:
        in_1 = get_value(equation[0])
        in_2 = get_value(equation[2])

        if equation[1] == "AND":
            return int(f"{in_1 & in_2:016b}", 2)
        elif equation[1] == "OR":
            return int(f"{in_1 | in_2:016b}", 2)
        elif equation[1] == "LSHIFT":
            return int(f"{in_1 << in_2:016b}", 2)
        elif equation[1] == "RSHIFT":
            return int(f"{in_1 >> in_2:016b}", 2)

with open("input.txt", "r") as iFile:
    InputData = iFile.read()

a_value = 16076

for equation in InputData.splitlines():
    expression, wire = equation.split(" -> ")
    data[wire] = expression.split()

data["b"] = [str(a_value)]

keys = set(data.keys())

while keys:
    for key in keys.copy():
        try:
            results[key] = decideEquation(data[key])
            keys.remove(key)
        except KeyError:
            continue

with open("output2.txt", "w") as oFile:
    oFile.write(str(results["a"]))
