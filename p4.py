'''
A palindromic number reads the same both
ways. The largest palindrome made from the
product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the
product of two 3-digit numbers.
'''#                   abcdef
#print(999*999) #lim = 998001

# a=f,b=e,c=d
# a=f, (n//100000) == n%10
# b=e, (n%100000)//10000 == (n-n%10)%100
# c=d, (n%100000)//10000 == (n-n%10)%100
rs = []
for n in range(999,99,-1):
    ns= int(str(n)+''.join(reversed(str(n))))
    #print(ns)
    for r in range(999,99,-1):
        if ns%r==0:
            print(r,ns/r,ns)
            if len(str(ns//r))==3:
                rs.append((r,ns/r,ns))
                print("^^FOUND^^")
        #print(ns/r)
for n in range(999,99,-1):
    ns= int(str(n)+''.join(reversed(str(n)[:2])))
    for r in range(999,99,-1):
        if ns%r==0:
            print(r,ns/r,ns)
            if len(str(ns//r))==3:
                rs.append((r,ns/r,ns))
                print("^^FOUND^^")
        #print(ns/r)
print(rs)
print("\n\n",rs[0])

#not 995599
