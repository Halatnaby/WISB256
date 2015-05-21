import math
import bisection

divider = '________'
print('findRoot testing:')
print(divider)

print(bisection.findRoot(lambda x:x*(x-1),0,3,.1))
print(bisection.findRoot(lambda x:x**2,0,3,.1))
print(bisection.findRoot(lambda x:math.cos(x),0,3,.1))

print(divider)

print("Done!")