'''
Extracting Data from JSON

In this assignment you will write a Python program which will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment:
http://py4e-data.dr-chuck.net/comments_1736876.json (Sum ends with 34)

Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''


import urllib.request, urllib.parse, urllib.error
import json

#Open the desired url using urllib library
url = input("Enter url: ")
fh = urllib.request.urlopen(url)
input = fh.read()
infojs = json.loads(input)

#Extract the comments count and print out the sum of it
sum=0
for item in infojs['comments']:
    sum = sum + int(item['count'])
print(sum)
