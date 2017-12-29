# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:05:11 2017

@author: rsayyad
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

#reading file contents
with open('data_in.txt', 'r') as File:
    string = File.read()
    

#Cleaning data 1st removing punchtuations and lowercasing all words
string = re.sub('[^a-zA-Z]',' ', string)
string = string.lower()

#removing stop words
word_list = word_tokenize(string)
new_list = [word for word in word_list if not word in stopwords.words('english')]

#we can see the difference between 2 list by comparing there lengths
print("word_list:",len(word_list))
print("new_list:",len(new_list))

#performing stemming
from nltk.stem.porter import PorterStemmer
from nltk import stem
ps = PorterStemmer()  #creating PorterStemmer object
leman = stem.WordNetLemmatizer()
stemmed=[]
lemmentized =[]
for word in new_list:
   stemmed.append(ps.stem(word))
   lemmentized.append(leman.lemmatize(word))

#performing comparision, for comparisin purpose i have created a list of true or false
#that by comparing each word and thus we can see the result in list compare
compare=[]
for i in range(len(stemmed)):
    if stemmed[i]==lemmentized[i]:
        compare.append(True)
    else:
        compare.append(False)
        

        
