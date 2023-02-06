#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output. You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
try:
    fh=open(fname,'r')
except:
    print('Wrong file name. Insert a valid file name:')
    quit()

lst = list()
for line in fh:
    line.rstrip()
    for words in line.split():
#add words to the "lst" list
        if not words in lst:
            lst.append(words)
#print words which are present more than once in the list
#        else:
#            print("Word already in the list:", words)
lst.sort()
print(lst)
