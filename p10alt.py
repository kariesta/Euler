"sum of primes under 2*10**6"

n = 2*(10**6)

primes = [True]*n
primes[0] = False

p = 2
while p**2<n:
    if primes[p-1]:
        print()
        for r in range(p**2,n+1,p):
            primes[r-1]=False
    p+=1
    while not primes[p-1]:
        p+=1
summy = 0
for r in range(n):
    if primes[r]:
        #print(r+1)
        summy+=r+1

print(summy)
#not 666667333338
#not 666668000007
#not 1000000000001
