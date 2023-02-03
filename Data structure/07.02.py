#--------------EXAMPLE 07.02----------
# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475. Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

#Desired output:
#Average spam confidence: 0.7507185185185187



fname = input("Enter file name: ")
total=0
count=0

#check if file name correspond to an available file
try:
    fh=open(fname,'r')
except:
    print('Wrong file name. Insert a valid file name:')
    quit()

#Slice values like requested, convert them into floats and compute average
for line in fh:
    line=line.strip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    count=count+1
    pos=line.find(':')
    svalue=(line[pos+1:])
    total=total+float(svalue)
    average=total/count

print("Average spam confidence:",average)

print('Done')
