#!/usr/bin/python3
import sys
file=open(sys.argv[1])
TP=0
FN=0
FP=0
TN=0
for line in file:
    if(line.startswith('DONE')==False):
        line=line.split(' ')
        TP+=int(line[1])
        FN+=int(line[2])
        FP+=int(line[3])
        TN+=int(line[4])
pre=TP/(TP+FP)
rec=TP/(TP+FN)
print("precision:",pre)
print("racall:",rec)
print("accuracy",(TP+TN)/(TP+TN+FP+FN))
print("F:",2*pre*rec/(pre+rec))
