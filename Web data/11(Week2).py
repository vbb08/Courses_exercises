'''
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
File to be used in this exercise : regex_sum_1736871.txt.
Expected outcome: 466577
Notes: The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
'''
import re

sum=0

x=open('regex_sum_1736871.txt', 'r')

for line in x:
    line=line.rstrip()

    y=re.findall('[0-9]+', line)
    for num in y:
        if len(y)>0:
            sum=sum+int(num)
print(sum)
