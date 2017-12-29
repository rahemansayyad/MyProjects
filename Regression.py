# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:27:07 2017

@author: rsayyad
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ex1data1.txt')
x=df.iloc[:,0].values  # x is population
y=df.iloc[:,1].values  #y is profit

#Excercise1
plt.scatter(x,y,color='red')
plt.xlabel('population')
plt.ylabel('profit')
plt.title('population vs profit')

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

x_train = x_train.reshape(len(x_train),1)
y_train = y_train.reshape(len(y_train),1)

#Excercise 2
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

x_test = x_test.reshape(len(x_test),1)
y_test = y_test.reshape(len(y_test),1)

plt.scatter(x_train,y_train,color='red')
plt.plot(x_test,regressor.predict(x_test),color='blue')
plt.title('population vs profit')
plt.xlabel('population')
plt.ylabel('profit')
plt.show()

regressor.score(x_train,y_train)

#Quadratic form
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly)
lin_reg= LinearRegression()
lin_reg.fit(x_poly,y)

plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('population vs profit')
plt.xlabel('population')
plt.ylabel('profit')
plt.show()

