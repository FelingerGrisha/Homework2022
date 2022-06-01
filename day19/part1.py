replacements = []

medicine = None


with open('input.txt', 'r') as iFile:
    InputData = iFile.read().split('\n')

for line in InputData:
    parts = line.strip().split(" => ")
    if len(parts) == 1:
        if not line.strip():
            continue
        medicine = line.strip()
        continue
    replacements.append((parts[0], parts[1]))


molecules = set()

for src, repl in replacements:
    idx = 0
    while src in medicine:
        idx = medicine.find(src, idx+1)
        if idx == -1:
            break
        molecules.add(medicine[:idx] + repl + medicine[idx + len(src):])

with open('output1.txt', 'w') as oFile:
    oFile.write(str(len(molecules)))


def part2():
    med = medicine
    count = 0
    while med != 'e':
        for src, repl in replacements:
            if repl in med:
                med = med.replace(repl, src, 1)
                count += 1
    return count


print("Part 2: ", part2())
