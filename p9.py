'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math
for a in range(1,334):
    for b in range(a+1,500):
        if a**2+b**2 == (1000-a-b)**2:
            print("hello!!!!",a,b,1000-a-b)
        if a+b <= 500:
            if math.sqrt(a**2+b**2)%1 == 0:
                print(a,b,math.sqrt(a**2+b**2))
                s = sum([a,b,math.sqrt(a**2+b**2)])
                if s == 1000.0:
                    print("\n@\n@\n@\n@\n@\n@\n***FOND***\n@\n@\n@\n@\n@*\n@*\n")
                print(sum([a,b,math.sqrt(a**2+b**2)]))

print(200**2+375**2,425**2)
print(200+375+425)
print(200*375*425)
