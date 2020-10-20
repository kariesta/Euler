'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
#837799
n = 10**6
nums ={}
for m in range(2,n):
    print(m)
    x = m
    s = 1
    while x!=1:
        if x%2==0:
            x=x/2
        else:
            x=(3*x)+1
        s+=1
    nums[m]=s

longest = 0
longname = 0
for k,v in nums.items():
    if v>longest:
        longest = v
        longname = k
print(longname,longest)



'''
#start på 1, lagre 1 i past
#gå et nivå videre, øk count med 1, fjern likt past
#gjenta til
class Node:
    def __init__(self,nth,stopable):
        self._next = None
        self._previous = []
        self.order = nth
        self.stopable = stopable

    def setNext(self,next):
        if self._next == None:
            self._next = next
            return next
        else:
            return False

    def hentNext(self):
        if self._next != None:
            return self._next
        else:
            return False

    def addPrev(self,prev):
        self._previous.append(prev)
        return self._previous

    def hentPrev(self):
        if self._previous == []:
            return False
        else:
            return self._previous

n=10**6
nodes = {}
for g in range(n):
    nodes[g+1] = Node(g+1,True)

#danne treet
for g in range(2,n):
    #if has next, already visited
    m = g
    #print(m, nodes[m].hentNext())
    while m != 1 and not nodes[m].hentNext():
        if m%2==0:
            #print("h=", m/2)
            h = int(m/2)
        else:
            #print("h=", 3*m+1)
            h = 3*m+1
        if h>n:
            nodes[h] = Node(h,False)
        nodes[m].setNext(h)
        nodes[h].addPrev(m)
        m=h

#begynne på 1. hente prev. til det er ingen flere noder med (Node[i].stopable = True) å hente.

levels = 1
found = [1]
currSmall = 0
#print(min(found))
#print(nodes[1].hentPrev())

while min(found)<n:
    currSmall = min(found)
    results = []
    for f in found:
        print(f, nodes[f].hentPrev())
        if nodes[f].hentPrev():
            results.extend(nodes[f].hentPrev())
    found = results
    levels +=1
print(found)

#915323

#for g in nodes.keys():
#    print(nodes[g].order, nodes[g]._next,nodes[g]._previous)

#'''



'''
n=10**6
#dict of (number, following chain)
past = {1:1,2:2,4:3,8:4,16:5,32:6,64:7}
bigD = [64,7]

for g in range(3,n):
    m = g
    if not m in past.keys():
        c = 1
        while m != 1 and not m in past.keys():
            if m%2==0:
                m = m/2
            else:
                m=3*m+1
            c += 1
        if m in past.keys():
            past[g] = c+past[m]
        else:
            past[g] = c
        if c>bigD[1]:
            bigD = [g,past[g]]
print(past)
print(bigD)
'''
