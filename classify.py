#!/usr/bin/python3
import re;
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import sys
div=[[1],[0,2,3,4],[5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,19,20],[18]]
data=[]
def readfile(filepath):
    f=open(filepath)
    for line in f:
        tmp=re.split('~| |\.|_|\n',line)
        doc=[]
        for x in tmp:
            if(x!=''):
                doc.append(x);
        del doc[0]
        tmp=' '.join(doc)
        data.append(tmp)

readfile("TrainingData.txt")
#print(data[0])
count_vect = CountVectorizer(stop_words="english")
train_counts = count_vect.fit_transform (data)
tfidf_transformer = TfidfTransformer()
train_tfidf = tfidf_transformer.fit_transform(train_counts)
traincat=pd.read_csv("TrainCategoryMatrix.csv",header=None)
data=[]
readfile("TestData.txt")
count_vect_2 = CountVectorizer(vocabulary=count_vect.vocabulary_)
test_counts = count_vect_2.fit_transform (data)
test_tfidf = tfidf_transformer.fit_transform(test_counts)
testcat=pd.read_csv("TestTruth.csv",header=None)
svclf = SVC(C=0.7,kernel = 'linear')
bayesclf= MultinomialNB()
knnclf = KNeighborsClassifier()

for cati in range(22):
#for cati in div[int (sys.argv[1])]:

    #SVM
    svclf.fit(train_tfidf,traincat[cati])
    pred=svclf.predict(test_tfidf)

    #naive bayes
    #bayesclf.fit(train_tfidf,traincat[cati])
    #pred=bayesclf.predict(test_tfidf)

    #KNN
    #knnclf.fit(train_tfidf,traincat[cati])
    #pred=knnclf.predict(test_tfidf)
    TP=0
    FN=0
    FP=0
    TN=0
    for i in range(7077):
        if(int(testcat[cati][i])==1):
            if(int(pred[i])==1):
                TP+=1;
            elif(int(pred[i])==-1):
                FN+=1;
        elif(int(testcat[cati][i])==-1):
            if(int(pred[i])==1):
                FP+=1;
            elif(int(pred[i])==-1):
                TN+=1;
    print(cati,TP,FP,FN,TN)
