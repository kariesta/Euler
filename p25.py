'''
F12 = 144
The 12th term, F12, is the first term to contain
three digits.

What is the index of the first term in the Fibonacci
sequence to contain 1000 digits?
'''
i = 2
f1 = 1
f2 = 1

while len(str(f2))<1000:
    if i%1000==0:
        print(i)
    i+=1
    t = f1
    f1 = f2
    f2 = f1+t
print(i)
print(f2)
