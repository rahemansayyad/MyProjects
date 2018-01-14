# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:27:40 2018

@author: rsayyad
"""


import nltk
from nltk.corpus import movie_reviews
import random

#Importing reviews
documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]


#shuffling to get better results
random.shuffle(documents)

#print(documents[1])

#creating list of words
all_words=[]
for word in movie_reviews.words():
    all_words.append(word.lower())

#Analyzing which word appears the most
all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
print(all_words["stupid"])


#
word_features = list(all_words.keys())[:3000]

def find_features(document):
    word=set(document)
    features={}
    for w in word_features:
        features[w] = (w in word)

    return features

featuresets = [(find_features(rev), category) for (rev,category) in documents] 

#dividing dataset into training and test set
training_set = featuresets[:1900]
test_set = featuresets[1900:]

#Fitting a classificational model
classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy is:",nltk.classify.accuracy(classifier, test_set)*100)


