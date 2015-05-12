import random
import math
import sys

count = len(sys.argv) - 1
argumentList = sys.argv

def drop_needle(L):
    x = random.random()
    y = random.random()
    a = random.vonmisesvariate(0,0)
    
    x1 = x + L * math.cos(a)
    y1 = y + L * math.sin(a)
    
    if (x >= 0 and x1 < 0) or (x < 1 and x1 >= 1):
        return True
    return False
    
if (count < 2):
    sys.exit('Use: python estimate_pi.py N L')

if (count == 3):
    random.seed(int(argumentList.pop()))

L = float(argumentList.pop())
N = int(argumentList.pop())

count = 0

for i in range(0, N):
    if(drop_needle(L)):
        count += 1
approxPi = -1

if L > 1:
    approxPi = 2*L / (count/N - 1) - (2/(count/N - 1) * (math.sqrt(L**2 - 1) + math.asin(1/L)))
else:
    approxPi = 2*L * N / count

print('%d hits in %d tries' % (count, N))
print('Pi = %s' % approxPi)