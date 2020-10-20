'''
2520 is the smallest number
that can be divided by each
of the numbers from 1 to 10
without any remainder.

What is the smallest positive
number that is evenly
divisible by all of the
numbers from 1 to 20?
'''
n = 20*19*18*17*14*13*11
#n = 2*5*7*4*9
print(n)

for r in range(20):
    if n%(r+1)!=0:
        print("not this!",r+1)
#not: 3724680960
#232792560
