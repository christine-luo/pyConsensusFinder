import csv
import os, sys

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../modules')

if libdir not in sys.path:
	sys.path.insert(0, libdir)

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
MACHLEARN_MUTATIONS=[]

f1 = file(HOME+'/completed/MACHLEARN_MUTATIONS_ARRAY.csv', 'r')
f2 = file(HOME+'/completed/TRAINING_MUTATIONS.csv', 'r')
f3 = file(HOME+'/completed/machine_learning_mutations.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

traininglist = list(c2)

for mach_row in c1:
    row = 1
    for training_row in traininglist:
        results_row = mach_row
        if mach_row[6].strip() == training_row[1].strip() and str(mach_row[7].strip()) == str(training_row[2].strip()) and mach_row[8].strip()==training_row[3].strip():
            c3.writerow(results_row)
        row = row + 1

f1.close()
f2.close()
f3.close()
