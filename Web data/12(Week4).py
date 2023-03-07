
'''
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

File for this assignment: http://py4e-data.dr-chuck.net/comments_1736873.htm
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve 'span' tags, convert them into integers and sum them
sum=0
tags = soup('span')
for tag in tags:
    print('Contents:', tag.contents[0])
    n=int(tag.contents[0])
#    print(n)
    sum=sum+n
print('Sum:',sum)
