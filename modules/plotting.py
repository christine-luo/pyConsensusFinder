import csv
import os, sys
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../modules')

if libdir not in sys.path:
	sys.path.insert(0, libdir)

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

with open(HOME+'/completed/1vqb_scores.csv') as f:
    score_array=np.asarray(list(csv.reader(f)))

a=score_array
ind = np.lexsort((a[:,1],a[:,2],a[:,3],a[:,4],a[:,5]))    
a=a[ind]
#np.savetxt('foo.csv',a)
with open(HOME+'/completed/1vqb_ordered.csv',"w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(a)

prev = None

add=0
ordered=[]

for i in range(len(a)):
    if i==0:
        prev = None
    else: 
        prev = a[i-1]
    if prev is not None and np.array_equal(prev[1:5],a[i,1:5]) == False:
        ordered.append(a[add:i]) 
        add=i
ordered=np.asarray(ordered)
x=[]
y=[]
for i in range(len(ordered)):
    for i in range(len(ordered[0])):
        x.append(ordered[0][i][0])
        y.append(ordered[0][i][6])
        plt.plot(x,y, '-o')

print x
print y
#fig = plt.plot(x,y, '-o')
#plt.scatter(x,y, '-o', label='1')


plt.savefig(HOME+'/completed/plot1.svg') # Any filename will do

#if score_array[:,1]

