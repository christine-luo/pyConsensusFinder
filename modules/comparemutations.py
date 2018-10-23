import csv
import numpy as np
import os, sys

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../modules')

if libdir not in sys.path:
	sys.path.insert(0, libdir)

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
MACHLEARN_MUTATIONS=[]
with open(HOME+'/completed/TRAINING_MUTATIONS.csv', 'rb') as csv1:
    with open(HOME+'/completed/MACHLEARN_MUTATIONS_ARRAY.csv') as csv2:
            training_set = csv.reader(csv1, delimiter=',')
            machlearn_set = csv.reader(csv2, delimiter=',')
            for train_row in training_set:
                for mach_row in machlearn_set:
                    if mach_row[6].strip()==train_row[1].strip() and mach_row[7].strip()==train_row[2].strip() and mach_row[8].strip()==train_row[3].strip():
                        MACHLEARN_MUTATIONS.append(mach_row)
print MACHLEARN_MUTATIONS
