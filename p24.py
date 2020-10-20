'''
permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of
the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or
alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

#[1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]
n=[0,1,2,3,4,5,6,7,8,9]
z = 0
for a in n:#1
    m=n.copy()
    m.remove(a)
    #print(n,m,a)
    for b in m:#2
        o=m.copy()
        o.remove(b)
        for c in o:#3
            p=o.copy()
            p.remove(c)
            for d in p:#4
                q=p.copy()
                q.remove(d)
                for e in q:#5
                    r=q.copy()
                    r.remove(e)
                    for f in r:#6
                        #print(r)
                        s=r.copy()
                        s.remove(f)
                        for g in s:#7
                            t=s.copy()
                            t.remove(g)
                            for h in t:#8
                                u=t.copy()
                                u.remove(h)
                                for i in u:#9
                                    v=u.copy()
                                    v.remove(i)
                                    for j in v:#10
                                        w=v.copy()
                                        z+=1
                                        if z%100000==0 and z<1000100:
                                            print(z,":\t",a,b,c,d,e,f,g,h,i,j)


# 2783915460



#    for r in range(10):









'''
n = 10**6
inters = 10
intervals =[1]

for r in range(1,inters):
    intervals.append(intervals[r-1]*10)
intervals.reverse()
print(intervals)

num = 0
for r in range(inters):
    if intervals[r]<n:
        print(r,intervals[r],inters-r)
        print("fff",(n//intervals[r])*10**(inters-r))
        num+=(n//intervals[r])*10**(inters-r)
        #n = n%intervals[r]
        print(n)
        #num += (n%(intervals[r]))*10**r
        #n = n//intervals[r]
print(num)
'''
