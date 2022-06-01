with open('input.txt', 'r') as iFile:
    InputData = iFile.read()

flyTime = 2503
score = {}
dist = {}
stats = []

for strAboutFly in InputData.split('\n'):
    n, _, _, speed, _, _, ftime,  _, _, _, _, _, _, rtime, _ = strAboutFly.split(" ")
    stats.append((n, int(speed), int(ftime), int(rtime)))
    dist[n] = 0
    score[n] = 0

for i in range(flyTime):
    for n, speed, ftime, rtime in stats:
        if i % (ftime + rtime) < ftime:
            dist[n] += speed

    best = max(dist.values())

    for n, d in dist.items():
        if d == best:
            score[n] += 1

with open('output2.txt', 'w') as oFile:
    oFile.write(str(max(score.values())))