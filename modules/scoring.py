import csv
import os, sys

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../modules')

if libdir not in sys.path:
	sys.path.insert(0, libdir)

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

f1 = file(HOME+'/completed/1EY0_trimmed_mutations.csv', 'r')
f2 = file(HOME+'/completed/1EY0_scores.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.writer(f2)

prev_row = next(c1)
print prev_row
score = 0

for current_row in c1:
    if current_row[0:5]==prev_row[0:5]:
        if current_row[9]<0:
            score = score-1
        elif current_row[9]>0:
            score = score+1
    else:
        prev_row.append(score)
        index=[0,1,2,3,4,5,10]
        score_row=[prev_row[i] for i in index]
        c2.writerow(score_row)
        score=0
    prev_row = current_row


f1.close()
