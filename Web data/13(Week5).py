'''
Extracting Data from XML

In this assignment you will write a Python program which will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment:
http://py4e-data.dr-chuck.net/comments_1736875.xml (Sum ends with 41)
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

#Open the desired url using urllib library
url = input("Enter url: ")
fh = urllib.request.urlopen(url)
input = fh.read()

#Parse the data obtained looking for the text within the count tags, convert the values into integers and sum them
stuff = ET.fromstring(input)
lst = stuff.findall('comments/comment')
#print('Number of count tags:', len(lst))

sum=0
for item in lst:
    a=int(item.find('count').text)
    sum=sum+a
print('Sum of all counting:',sum)
