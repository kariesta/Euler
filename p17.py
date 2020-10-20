'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''
#not: 21224, 21248,21251
small_words = ["one", "two", "three", "four", "five","six","seven","eight","nine"]
small_med_words = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
medium_words = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
large_words = ["hundredand","onethousand"]

summ = 0
for i in range(1,1001):
    r = i
    sum = 0
    words = ""
    if i==1000:
        sum += len(large_words[1])
        i-=1000
        print(i)
        words+=large_words[1]+" "
    if i>=100:
        n = i//100
        sum += len(large_words[0])+len(small_words[n-1])
        i -= n*100
        if i==0:
            sum-=3
        words+= small_words[n-1]+" "+large_words[0]+" "
    if i>=20:
        n=i//10
        sum += len(medium_words[n-2])
        i -= n*10
        words+= medium_words[n-2]+" "
    if i<10 and i>0 :
        sum += len(small_words[i-1])
        words+= small_words[i-1]+" "
    if i>9:
        sum += len(small_med_words[i-10])
        words+= small_med_words[i-10]+" "
    print(r,": ",words,", ",sum)
    summ+=sum
print(summ)


#1-9 *8 = ganger i 100
#10-19 *1 = ganger i 100
#20,30..80,90 *10 = ganger i 100
#and for hvert tall med hundre, + tall for 1-99 *10
#"one thousand" = 1

'''
wordsInhudred = 0
smallwordsLen = sum([len(r) for r in small_words])*(1+len(medium_words))
medium_wordsLen = sum([len(r) for r in medium_words])*10
small_med_wordsLen = sum([len(r) for r in small_med_words])
wordsInhudred = medium_wordsLen+medium_wordsLen+smallwordsLen

large_wordsLen = (len(large_words[0])*100*99)-1
print(smallwordsLen,medium_wordsLen,small_med_wordsLen)
print(wordsInhudred,large_wordsLen)
print(wordsInhudred*100+large_wordsLen+len(large_words[1]))
#225407

sLen =sum([len(r) for r in small_words])
mLen =sum([len(r) for r in medium_words])
smLen=sum([len(r) for r in small_med_words])
lLen =len(large_words[0])
#print(10*((9*sum[len(r) for r in small_words])+(10*(sum([len(r) for r in medium_words])))+sum([len(r) for r in small_med_wordsLen]))+(sum([len(r) for r in small_words])+len(large_words[0]))*10)
print(10*((9*sLen)+(10*mLen)+smLen)+((sLen+lLen)*10))
#9100
print("{:5.65f}".format(1/7))
'''
