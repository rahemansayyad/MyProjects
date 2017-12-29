# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 08:41:35 2017

@author: rsayyad
"""
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import re

#Reading data from text file
with open('data_in.txt', 'r') as File:
    string = File.read()


#removing all punctuations from string and word tokenizing
string = re.sub('[^a-zA-Z]', ' ', string)    
word = word_tokenize(string)

pos_words = pos_tag(word)


from nltk.chunk import ne_chunk
chunk_sent = ne_chunk(pos_words)
chunk_sent.draw()