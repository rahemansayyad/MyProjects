# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 12:02:08 2017

@author: rsayyad
"""

import csv
string =''
with open('exl.csv', newline='') as File:
    reader = csv.reader(File)
    for rows in reader:
        string +=rows[0]

string = string[7:]

#some precaution steps before word tokenization
#1. Remove punctuations
import re
string  = re.sub('[^a-zA-Z]', ' ', string)

#2. Lowercasing all words so that no 2 words appear 2 times
string = string.lower()

from nltk.tokenize import word_tokenize
word = word_tokenize(string)

#writing back to file
myDialect = csv.register_dialect('myDialect', delimiter=' ', quoting = csv.QUOTE_NONE, escapechar=' ')
with open('data_out1.csv', 'w') as File:
    writer = csv.writer(File, myDialect)
    writer.writerow(word)
    
