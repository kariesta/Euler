'''
If we list all the natural numbers
below 10 that are multiples of 3
or 5, we get 3, 5, 6 and 9. The
sum of these multiples is 23.

Find the sum of all the multiples
of 3 or 5 below 1000.
'''
n = 995
m = 999
zum = 0
while m>0:
    print(n,m)
    if n%3==0:
        n-=5
    if n>0:
        zum+=m
        zum+=n
    else:
        zum+=m
    n-=5
    m-=3
print(zum)
#could be: 233168
#not: 234168
#could be: 239433
#could be: 267333
#not: 240600
#counts doulbe where r is multiple of 3 AND 5
print([r for r in range(0,1001,3)])
print("with 5s")
print([r for r in range(0,1001,5)])
print("with 15s")
print([r for r in range(0,1001,15)])

n = sum(range(0,1001,3))
m = sum(range(0,1001,5))
nm = sum(range(0,1001,15))
print(n+m-nm)
#not: 234168
print(n+m-(2*nm))
#could be: 201003

summy = 0
sum15 = 0
#for r in range(1001):
