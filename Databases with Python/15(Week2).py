'''
Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is mbox.txt, which is uploaded in the smae folder.


The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
'''

import sqlite3

#connect to cursor file
conn = sqlite3.connect('15(Week2).sqlite')
cur = conn.cursor()

#create table 'Counts' with organization 'org' and 'count' as attributes
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

#open file mbox.txt, after input request, and find the domain of all the email adresses
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    segments = email.split('@')
    org = segments[-1]

#group, count the different domains #sort them by descending number showing the first 10 results
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

#sort the domains by descending number showing the first 10 results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
