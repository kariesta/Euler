'''
145 is a curious number,
as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to
the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are
not included.
'''
import math
for a in range(10):
    print(a,a*math.factorial(9))
#for r in range(3,)
x = 0
for a in range(3,9999999):
    ars = str(a)
    s = sum([math.factorial(int(r)) for r in ars])
    if s==a:
        x+=a
        print(a)
print("rr ",x)
