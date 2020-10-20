'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
'''

sum = 0
sqsum = 0

for r in range(1,100+1):
    sum+=r**2
    sqsum += r
sqsum = sqsum**2
print(sum)
print(sqsum)
print(sqsum-sum)
