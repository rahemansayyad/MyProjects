# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:19:35 2017

@author: rsayyad
"""

import pandas as pd
import os
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

#creating list of all the sentences in given csv file
df=[]
with open('data_in.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        df.append(row)

#Converting the above list into string, so that we can apply sentence tokenization to it
string=''        
for item in df:
    string +=item[0]

#string sliced to remove "comment" from the string
string = string[7:]
    
sent = sent_tokenize(string)
        
#writing data to csv file
csv.register_dialect('myDialect', delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=' ')
with open('data_out.csv', 'w') as File:
    writer = csv.writer(File, dialect='myDialect')
    writer.writerows(sent)


#Performing NE Chuncking
from nltk.chunk import ne_chunk
chunk_sent = ne_chunk(sent)
chunk_sent.draw()

