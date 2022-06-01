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

count = 0
med = medicine

while med != 'e':
    for src, repl in replacements:
        if repl in med:
            med = med.replace(repl, src, 1)
            count += 1

with open('output2.txt', 'w') as oFile:
    oFile.write(str(count))