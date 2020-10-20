'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

n=10001
primes = [2,3, 5, 7, 11, 13, 17, 19]#, 23, 29, 31, 39, 41]
def dividable(m):
    for i in primes:
        if m%i==0:
            return True
    return False

print(n//600,n%600)
p=primes[-1]+2
while len(primes)<n:
    if not dividable(p):
        primes.append(p)
    p+=2
print(primes[-1])
#print(primes.index(77047))
#print(primes)
#not 104729
#not 77047
#104743
