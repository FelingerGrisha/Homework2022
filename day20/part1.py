import math

def GetDivisors(n):
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

with open('input.txt', 'r') as iFile:
    InputData = int(iFile.readline())

lowestNumber = None
i = 0

while not lowestNumber:
    i += 1
    divisors = GetDivisors(i)
    if not lowestNumber:
        if sum(divisors) * 10 >= InputData:
            lowestNumber = i
            break

with open('output1.txt', 'w') as oFile:
    oFile.write(str(lowestNumber))