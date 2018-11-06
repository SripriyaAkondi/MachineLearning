# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:59:40 2018

@author: akond
"""
import math
import numpy as np
import matplotlib.pyplot as plt

L=0.1
output=[]
iterations=[]
M=1000
#inputs
a0=np.matrix([[0, 0, 1, 1], [0, 1, 0, 1]])
print(a0)

#outputs
y=np.matrix([[0, 1, 1, 0]])

w1=np.random.random((4, 2)) - 0.5
print(w1)

w2=np.random.random((1,4))-0.5
print(w2)

b1=np.matrix([[0],[0],[0],[0]])
print(b1)

b2=np.matrix([[0]])
print(b2)

for j in range(M):
    

        #Calculating z and a for the first layer
        z1=np.dot(w1,a0)+b1
        print(z1)
        #Binary Sigmoid at hidden layer
        a1=1.0/(1+np.exp(-z1))
        print(a1)
        
        #Calculating z and a for the second layer
        z2=np.dot(w2,a1)+b2
        print(z2)
        #Sigmoid at output layer
        a2=1.0/(1+np.exp(-z2))
        print(a2)
        
        #Loss function
        x=np.log(a2)
        x1=np.log(1-a2)
        cost=-np.sum(np.multiply(y,x)+np.multiply((1-y),x1))/4
        print("The cost for the current iteration is:",cost)
        output.append(cost)
        iterations.append(j)
        
        
        #Back propogation using Binary Sigmaoid
        dz2=a2-y
        print(dz2)
        
        a1_Transpose=a1.transpose()
        dw2=np.dot(dz2,a1_Transpose)
        print(dw2)
        
        db2=dz2
        print(db2)
        
        w2_Transpose=w2.transpose()
        da1=np.dot(w2_Transpose,dz2)
        print(da1)
        
        z11=np.multiply(a1,(1-a1))
        dz1=np.multiply(da1,z11)
        print(dz1)
        
        
        a0_Transpose=a0.transpose()
        dw1=np.dot(dz1,a0_Transpose)
        print(dw1)
        
        db1=dz1
        
        w1_Transpose=w1.transpose()
        da0=np.dot(w1_Transpose,dz1)
        print(da0)
        
        w1=w1-np.multiply(L,dw1)
        
        b1=b1-np.multiply(L,db1)
        
        w2=w2-np.multiply(L,dw2)
        
        b2=b2-np.multiply(L,db2)
        
        


#Plotting the graph
plt.plot(iterations,output,color="blue")
plt.xlabel('No. of iterations , i.e j')
plt.ylabel('Cost , i.e J(theta)')
plt.title('Error function')







