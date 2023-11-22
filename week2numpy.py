# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:43:15 2023

@author: dowie
"""

#Question 1
#%% import numpy and rename it to np
import numpy as np # importing numpy and name it as 'np'

#1.1
a = np.array([0,1,2,3,4,5,6,7,8,9]) # create numpy array with 10 elements

#1.3
print(np.max(a)) # or you can use print(a.max())

#1.4
print(np.min(a)) # or you can use print(a.min())

#1.5
print(np.mean(a)) # or you can use print(a.mean())

#1.6
print(a.shape) # printing the array shape

#########################################################################################################
#########################################################################################################

#Question 2
# Creating a python list with 5 elements
b = [1,2,3,4,5]
print(b)

#2.1
b.append(6) # adding 6 to the end of the list
print(b)

#2.2
# appending 100 more values to the end of the list
for i in range(0,100): # running the code blow for 100 times
    b.append(0) # adding 0 to the end of the array

#2.3
c = np.array(b) # converting the list ot numpy array

#2.4
print(type(b)) # Type of list b before conversion

#2.5
print(type(c)) # type of the object after conversion

#####################################################################################################
#####################################################################################################

#Question 3
np.ones((1,1000))# Create a numpy array with 1000 elements of all ones (1)
np.zeros((1,1000)) # Create a numpy array with 1000 elements of all zeros (0)

#######################################################################################################
#######################################################################################################


#Question 4
# create a 2D numpy array
d = np.array([[1,2,3,4],[5,6,7,8]]) # crate a 2D array in format of [[row 1],[row 2],[row 3]...]

#4.1
# The number of elements in each row defines the number of the columns
print(f'Shape of 2D array is: {d.shape}')

#4.3
print(d.max())# maximum of the 2D array

#4.4
print(d.max(axis=0))# prints the maximum of each column
print(d.max(axis=1))# prints the maximum of each row
print(d.mean(axis=0)) # mean/average each column of array

#4.5
print(d.mean(axis=1)) # averages each row of the array

#4.6 & 4.7
# reshape the numpy array
e = d.reshape((4,2)) # reshape the array from 2x4 to 4x2
print(e)
print(e.shape)
e = e.reshape((-1,1)) # flattening (making a column array)
print(e); print(e.shape)

e = e.reshape((2,4))# reshaping it to its original shape
print('\n')

###############################################################################################################
##############################################################################################################


#Question 5
# extracting the last column of the array
f = e[:,-1] # extracting the last column
print(f)

####################################################################################################################
####################################################################################################################

#Question 6
# adding the f to the last column of e
g = np.hstack((e,f.reshape((2,1))))
print(g)

###################################################################################################################
###################################################################################################################


#Question 7
# read a random file to python 

filePath = r'C:\Users\sho6\Downloads\\'
fileName = 'file.txt'
file = open(filePath + fileName,'r') # rading the txt file
lineData = file.readline() # reading each line of the file
print(f'there are {lineData.count("the")} instances of word "the"') # print counts of the word "the"
# put the code above in a for loop to do it for all the lines in the data. Do this yourself
