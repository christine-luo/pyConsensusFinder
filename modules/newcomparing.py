import csv
import os, sys

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../modules')

if libdir not in sys.path:
	sys.path.insert(0, libdir)

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

f1 = file(HOME+'/completed/1ey0full.csv', 'r')
f2 = file(HOME+'/completed/FREQTABLE1.csv', 'r')
f3 = file(HOME+'/completed/1ey0_scoring.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

traininglist = list(c2)

for mach_row in c1:
    row = 1
    for training_row in traininglist:
        results_row = mach_row
        if training_row[3]==mach_row[0]: #if same substitution? 
            difference = training_row[mach_row[2]+1] - mach_row[4] #idk what to do with this...square?
            results_row.append(difference)
            c3.writerow(results_row)
        row = row + 1

f1.close()
f2.close()
f3.close()
