import csv
import os, sys
import numpy as np

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../modules')

if libdir not in sys.path:
	sys.path.insert(0, libdir)

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

f1 = file(HOME+'/completed/3gb1_trimmed_mutations.csv', 'r')
f2 = file(HOME+'/completed/3gb1_scores.csv', 'w')


c1 = csv.reader(f1)
c2 = csv.writer(f2)

prev_row = next(c1)
if float(prev_row[11])>=0.5:
    score = 1

pH=float(prev_row[9])
temp=float(prev_row[10])
count=1

for current_row in c1:
    if current_row[0:5]==prev_row[0:5]:
        pH=pH+float(current_row[9])
        temp=temp+float(current_row[10])
        count=count+1

        if float(current_row[11])>=0.5:
            score = score+1

    else:
        pH=pH/count
        temp=temp/count
        score=score/count
        prev_row.append(pH)
        prev_row.append(temp)
        prev_row.append(score)
        
        index=[0,1,2,3,4,5,12,13,14]
        score_row=[prev_row[i] for i in index]
        c2.writerow(score_row)
        if float(current_row[11])>=0.5:
            score = score+1
        pH=float(current_row[9])
        temp=float(current_row[10])
        count=1
    prev_row = current_row


f1.close()
