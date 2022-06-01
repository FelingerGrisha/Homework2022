import re

facts = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3,
         'akitas':0, 'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2,
         'perfumes':1
         }

tok = re.compile(r'Sue (?P<n>\d+): (?P<a>\w+): (?P<aval>\d+), (?P<b>\w+): (?P<bval>\d+), (?P<c>\w+): (?P<cval>\d+)')

def parse_line(line):
    m = tok.search(line)
    n = int(m.group('n'))
    d = { m.group('a'): int(m.group('aval')),
          m.group('b'): int(m.group('bval')),
          m.group('c'): int(m.group('cval')) }
    return n, d

numberOfAuntSue = 0

for line in open('input.txt'):
    n, d = parse_line(line)
    matches = 0
    for k, v in d.items():
        if k in facts:
            if k in ('cats', 'trees') and v > facts[k]:
                matches += 1
            elif k in ('pomeranians', 'goldfish') and v < facts[k]:
                matches += 1
            elif k not in ('cats', 'trees', 'pomeranians', 'goldfish') and v == facts[k]:
                matches += 1
    if matches == 3:
        numberOfAuntSue = n

with open("output2.txt", "w") as oFile:
    oFile.write(str(numberOfAuntSue))