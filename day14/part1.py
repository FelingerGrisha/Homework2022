with open('input.txt', 'r') as iFile:
    InputData = iFile.read()

flyTime = 2503
best = 0

for strAboutFly in InputData.split('\n'):
    n, _, _, speed, _, _, ftime,  _, _, _, _, _, _, rtime, _ = strAboutFly.split(" ")
    speed, ftime, rtime = int(speed), int(ftime), int(rtime)
    dist = 0

    cycle = ftime + rtime
    bursts = flyTime // cycle
    dist += speed * ftime * bursts

    leftover = flyTime % cycle
    dist += speed * min(leftover, ftime)

    if dist > best:
        best = dist

with open('output1.txt', 'w') as oFile:
    oFile.write(str(best))
