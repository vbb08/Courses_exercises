#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#Desired output for mbox-short.txt file is: cwen@iupui.edu 5


#---NOTE:----
#  Every .txt file in the repo can be used for testing

fname = input("Enter file name: ")
try:
    fh=open(fname,'r')
except:
    print('Wrong file name. Insert a valid file name:')
    quit()

dic=dict()
for line in fh:
    line=line.rstrip()
    words=line.split()

#create a dictionary. From lines starting with 'From ' i take the second words (email addresses) to be placed in the dictionary where every item correspond to a counting of a different email address
    if line.startswith('From '):
        email=words[1]
        dic[email]=dic.get(email,0)+1

print(dic)

bigcount=None
bigword=None
for email,count in dic.items():
    if bigcount == None or count>bigcount:
        bigword=email
        bigcount=count
print('The most frequently email used is:', bigword, 'which is used:', bigcount, 'times')
