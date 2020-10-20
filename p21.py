'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10 000.
'''
n =10**4
divs = [[1] for r in range(n+1)]
ambi = []
for m in range(2,int(n/2)+1):
    o = m*2
    while o<=n:
        divs[o].append(m)
        o+=m
print("Roops: ",divs)
print(divs[220],sum(divs[220]))
print(divs[284],sum(divs[284]))
print(divs[5020])
print(divs[5564])
print(divs[6232])
print(divs[6368])

divs = [sum(r) for r in divs]
for m in range(2,n+1):
    if divs[m]>m and divs[m]<=n and divs[divs[m]]==m:
        ambi.extend([m,divs[m]])
print("Loops: ",ambi)
print("Momo: ",sum(ambi))

'''
def divor(intus):
    result = 1
    for a in range(2,(intus+2)//2):
        if intus%a==0:
            result+= a+(intus/a)
    return result


def amic(intur):
    for a in range(n):
        if diviors[a]==intur and a ==diviors[intur] and intur !=diviors[intur]:
            return [a,intur]
    return False

n=10**4
amicable = []
diviors = [0,0]

for m in range(2,n):
    diviors.append(divor(m))



print([str(d)+": "+str(diviors[d]) for d in range(n)])

for m in range(2,n):
    if not m in amicable:
        a = amic(m)
        if a:
            print(a)
            amicable.extend(a)
print(sum(amicable))

''
n=10000
divisors = [1]*n

for r in range(n):
    print(r)
    for j in range(1,int(r/2)):
        if (r+1)%j==0:
            divisors[r]+=j+((r+1)/j)

sum = 0
for r in range(n-1):
    for m in range(r+1,n):
        if divisors[r] == divisors[m]:
            sum += r+m+2
print(sum)
'''
