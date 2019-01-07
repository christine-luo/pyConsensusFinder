import csv
import os, sys
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

thisdir = os.path.dirname(__file__)
libdir = os.path.join(thisdir, '../modules')

if libdir not in sys.path:
	sys.path.insert(0, libdir)

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

results = []
with open(HOME+"/uploads/1BNI_scores_replaced.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
results=np.asarray(results)

inputs=results[:, 0:5]
score=results[:, 6]

reg = linear_model.Lasso(alpha=0.01)
reg.fit(inputs, score)       
print reg.coef_
print reg.score(inputs, score)
print cross_val_score(reg, inputs, score, cv=5)



#reg = LinearRegression().fit(inputs, score)
#print reg.score(inputs, score)
#print reg.coef_
