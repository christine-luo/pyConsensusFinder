if protein=='1bjp.fasta':
    word = 'PIAQIHILEGRSDEQKETLIREVSEAISRSLDAPLTSVRVIITEMAKGHFGIGGELASKVRR'
    sequence=list(word)
if protein=='1ey0.fasta':
    word = 'ATSTKKLHKEPATLIKAIDGDTVKLMYKGQPMTFRLLLVDTPETKHPKKGVEKYGPEASAFTKKMVENAKKIEVEFDKGQRTDKYGRGLAYIYADGKMVNEALVRQGLAKVAYVYKPNNTHEQHLRKSEAQAKKEKLNIWSEDNADSGQ'
    sequence=list(word)

# f1 = file(HOME+'/completed/1588530147_1ey0.fasta_counts.csv', 'r')
# f3 = file(HOME+'/completed/1ey0_400_frequencytable.csv', 'w')

# c1 = csv.reader(f1)
# c3 = csv.writer(f3)
# traininglist = list(c1)

##nptraining as variable for Counts aka output from analyze module counts array
nptraining=counts

##AA_list is the list of amino acids in the order
AA_list=nptraining[:,0]
AA_list[0]='G'

##set counts as the array of the actual numbers, make them into numpy array
counts = nptraining[:,1:]
counts = counts.astype(np.float)


#counts = numpy.genfromtxt(HOME+'/completed/1590712404_1ey0.fasta_counts.csv', delimiter=',', usecols=range(1,150))
#AA_list = numpy.genfromtxt(HOME+'/completed/1590712404_1ey0.fasta_counts.csv', delimiter=',', dtype=None, usecols=range(1))

##divide each value by the wild type amino acid count
transpose = counts.transpose()
##index is length of protein
index=range(len(counts[1]))
for i in index:
    wt_AA=word[i]
    ##index of which amino acid WT would be
    x, = np.where(AA_list == wt_AA)
    ##divide row (which is a position) by the WT count
    transpose[i]= transpose[i]/transpose[i,x]
##transpose back
final = transpose.transpose()
##IDS is theoretically the same as AA_list
IDS = np.zeros([22,1],dtype=object)

IDS[:,0]=['G', 'P', 'A', 'V', 'L', 'I', 'M', 'C', 'F', 'Y', 'W', 'H', 'K', 'R', 'Q', 'N', 'E', 'D', 'S', 'T', '-', 'other']   
##put the IDS back as the first column
actualfinal=np.append(IDS, final, axis=1)

#withAA = numpy.hstack((AA_list, final))
##save as freq table
np.savetxt(HOME+'/completed/1ey0_400_frequencytable.csv', actualfinal, delimiter=",", fmt='%s')


#########same as file above, open again
f2 = file(HOME+'/completed/1ey0_400_frequencytable.csv', 'r')

c2 = csv.reader(f2)


traininglist = list(c2)
f2.close()

nonzerocount=0
newmatrix=[]
#### change everything into natural log and calculate consensus energy
for row in traininglist: 
    for i in range(len(row)):
        try:
            row[i]==float(row[i])

            if float(row[i]) == float(0):
                #######NUMBER OF SEQUENCES!!!!
                row[i]=float(1/(numberofsequences+1))
                row[i]=-0.592126*math.log(float(row[i]))
                print 'working for the zeros'
            else:
                row[i]=-0.592126*math.log(float(row[i]))
                print 'should work!'

        except ValueError:
            pass



nptraining=np.array(traininglist)

AA_list=nptraining[:,0]
AA_list[0]='G'

npcounts=nptraining[:,1:]
npcounts = npcounts.astype(np.float)



transpose = npcounts.transpose()
index=range(len(npcounts[1]))
for i in index:
    wt_AA=word[i]
    x, = np.where(AA_list == wt_AA)
    transpose[i,x]=0

IDS = np.zeros([22,1],dtype=object)

IDS[:,0]=['G', 'P', 'A', 'V', 'L', 'I', 'M', 'C', 'F', 'Y', 'W', 'H', 'K', 'R', 'Q', 'N', 'E', 'D', 'S', 'T', '-', 'other']   

final = transpose.transpose()
print final.shape
print IDS.shape

withAA = np.hstack((IDS, final))

np.savetxt(HOME+'/completed/new_1bjp_100_table_6_18.csv', withAA, delimiter=",", fmt='%s')

if protein=='1bjp.fasta':
    f1 = file(HOME+'/completed/1bjp_experimental_data.csv', 'r')
if protein=='1ey0.fasta':
    f1 = file(HOME+'/completed/1ey0full.csv', 'r')

f2 = file(HOME+'/completed/new_1bjp_100_table_6_18.csv', 'r')
f3 = file(HOME+'/completed/1bjp_100_testrun_6_18.csv', 'w')


c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)


prev_row = next(c2)

traininglist = list(c2)
nonzerocount=0
newmatrix=[]

if protein=='1ey0.fasta':
    for mach_row in c1:
        row = 1
        for training_row in traininglist:
            if training_row[0]==mach_row[3]: #if same substitution? 
                results_row=[]
                #difference = (float(training_row[int(mach_row[2])]) + float(mach_row[4]))**2 
                difference=0
                results_row.append(difference)
                results_row.append(difference)
                results_row.append(training_row[int(mach_row[2])]) #prediction 
                results_row.append(-float(mach_row[4])) #actual
                c3.writerow(results_row)


if protein=='1bjp.fasta':
    for mach_row in c1: #training data 
        for training_row in traininglist: #frequency table 
            split=re.split('(\d+)',mach_row[0])
            if training_row[0]==split[2]:#if same substitution? 
                results_row=[]
                results_row.append(split[1]) #substitution
                results_row.append(split[2]) #substitution 
                results_row.append(float(training_row[int(split[1])])) #prediction 
                results_row.append(float(mach_row[1])) #actual 
                c3.writerow(results_row)

f1.close()
f2.close()
f3.close()

# inside = open(HOME+'/completed/1bjp_5k_roc_6_18.csv', 'rb')
# output = open(HOME+'/completed/1bjp_nozero_5k_roc_6_18.csv', 'wb')
# writer = csv.writer(output)
# for row in csv.reader(inside):
#     if float(row[2])!=float(0):
#         writer.writerow(row)

# inside.close()
# output.close()



f3 = file(HOME+'/completed/1bjp_100_testrun_6_18.csv', 'r')
f2 = file(HOME+'/completed/1bjp_100_roc_7_2.csv', 'w')

c3 = csv.reader(f3)
c2 = csv.writer(f2)

traininglist = list(c3)

if haszeros==0:
    nozerolist=[]
    nptraininglist=np.array(traininglist)
    tosort=nptraininglist[:,2]
    largestone=tosort[-1]

    for row in traininglist:
        if float(row[2])!=float(largestone):
            nozerolist.append(row)
    traininglist=nozerolist

negtot=0
negcount=0

postot=0
poscount=0

nptraininglist=np.array(traininglist)
tosort=nptraininglist[:,2]
tosort = tosort.astype(np.float)
tosort.sort()
smallestone=tosort[0]
largestone=tosort[-1]



for row in traininglist:

    # if float(row[1])<0:
    #     # negtot=negtot+1
    #     # if float(row[0])<0:
    #     #     negcount=negcount+1
    #     # else:            
    #     #     negcount=negcount-1
    #   ###for ROC  
    #     row[1]=1

    # else:
    #     # postot=postot+1
    #     # if float(row[0])>0:
    #     #     poscount=poscount+1
    #     # else:            
    #     #     poscount=poscount-1

    #     ###for ROC
    #     row[1]=0

    ###### for 1ey0 ----
    if protein=='1ey0.fasta':
        if float(row[3])<0:
            row[3]=1
        else:
            row[3]=0
        ####----- end 
    if protein=='1bjp.fasta':
        if float(row[3])>2.5:
            row[3]=1
        else:
            row[3]=0

    ### when 1ey0 below, use row[0]
    row[2]=-float(row[2])

    # subtract biggest number 
    if float(smallestone)==float(largestone):
        if float(smallestone)>0:
            row[2]=1
        if float(smallestone)==0:
            row[2]=0.5
        else:
            row[2]=0
    else:
        row[2]=float(row[2])+float(largestone)
    # divide by the smallest subtract biggest
        row[2]=float(row[2])/float(-float(smallestone)+float(largestone))


    c2.writerow(row)

roclist=np.array(traininglist)
roclist=roclist[:,2:]
roclist=roclist.astype(np.float)

true=roclist[:,1].astype(np.int)
predict=roclist[:,0]


roc_score = roc_auc_score(true,predict)
