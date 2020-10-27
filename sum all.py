import re
hand = open("regex_sum_735179.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y
sum=0
for z in x:
    sum = sum + int(z)
print(sum)

#to sum all the digits in the file 'abc' using regular expression
