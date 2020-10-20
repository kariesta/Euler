'''
The prime factors of 13195 are
5, 7, 13 and 29.

What is the largest prime factor
of the number 600851475143 ?
'''
import math

def nextP(previous):
    prev = previous[-1]+1
    while prev < previous[-1]**2:
        #sjekk om delelig
        i = 0
        while prev%previous[i]==0 and i<len(previous):
            i+=1
        if i!=len(previous):
            return prev
        prev+=1


#p = 2, minste prime
p=2
n = 600851475143
past = []

#når n=p har du funnet største prim tall.
while p!=n:
    #del n så lenge det går
    while n%p == 0:
        n = n/p
        print(p)
    #finne neste prim
    past.append(p)
    p = nextP(past)
print("printos",n)

'''
import math
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,]
p = 3
#bygg videre på primes
print(math.sqrt(600851475143))
#høyeste faktor av 600851475143 er 600851475143/2
#sil kun 0-sqrt(600851475143), bruk heller  x fra primes-listen til å danne faktor 600851475143/x og sjekk om det er prime.
#Lag en liste av påfølgende heltall fra 2 til n: (2, 3, 4, ..., n).
n = math.ceil(math.sqrt(600851475143))
primes = [True]*n
primes[0] = False
primes[0] = False

#La p til å begynne med være lik 2, det første primtallet.
p = 2
while p**2<=n:
    print("primes: ",p)
    #Stryk ut alle multipler av p som er større enn eller lik p*p, fra listen.
    for r in range(p*p,n,p):
        primes[r] = False
    #Finn det første tallet større enn p som står igjen på listen. Dette tallet
    #er det neste primtallet. Sett p lik dette tallet.
    p+=1
    while not primes[p]:
        p+=1
    #Gjenta trinn 3 og 4 inntil p**2 er større enn n.
#Alle gjenværende tall på listen er primtall.
print("did!")
#finner høyeste primtall
l = len(primes)-1
while not primes[l]:
    l-=1
print(l) #775146.0992245268
#finner høyeste faktor
print("looking!")
oc = 8462696833
for r in range(2,math.ceil(math.sqrt(oc))):
    if oc%r==0:
        if primes[r]:
            print("by prime\t",oc/r,"r:",r)
        else:
            print("by else \t",oc/r,"r:",r)

'''
'''
 8462696833 np
  716151937 np
  408464633 np
   87625999 np
   10086647 np
    5753023 np
    1234169 np
   10086647
    5753023
    1234169
#'''



#'''

'''
def isprime(maybe):
    if maybe%2==0:
        return False
    while r<=sqrt(maybe):
        if maybe%r==0:
            return False

    return True

def nonmultiple(resents):
    return

n = 600851475143
r = 2
rs = [2]

while r<=sqrt(600851475143):
    prim = n/r
    if isprime(prim):
        print(prim)
    else:
        rs.append(r)
        r+= nonmultiple(rs)


#'''
