# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:32:15 2018

@author: akond
"""
import math
import numpy as np
import matplotlib.pyplot as plt
 

X=[0.5,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50]
Y=[0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1]
M=20
N=5000
L=0.1 #Learning factor
Z=[]
Z1=[]
intial_theta0=0.1
intial_theta1=0.2

#Computing htheta(X),Cost function and updated theta values
def myFunction():
    theta0=0.1;
    theta1=0.2;
    Z=[]
    output=[]
    iterations=[]
    sum1=0
    sum2=0
    sum3=0
    
    for j in range(N):
        #Computing htheta(X)
        for i in range(M):
            y1=theta0 + theta1*X[i]
            result=1/(1+math.exp(-y1))
            Z.append(result)
        print("htheta(x) values are:",Z)

#Computing cost function
        for i in range(M):
             sum1=sum1+(-(Y[i]*math.log(Z[i]))-((1-Y[i])*math.log(1-Z[i])))
        cost=sum1/M
        output.append(cost)
        iterations.append(j)
        print("The cost for the current iteration is:",cost)
        print("The current iteration is:",iterations)
    
#updating theta values
        
        for i in range(M):
            diff=Z[i]-Y[i]
            sum2=sum2+diff
    
        for i in range(M):
            diff1=(Z[i]-Y[i])*X[i]
            sum3=sum3+diff1
        
    
        theta0=theta0-((L/M)*sum2)
        print("Updated theta0 value is:",theta0)
        theta1=theta1-((L/M)*sum3)
        print("Updated theta1 value is",theta1)
        if j!=N-1:
            Z=[]
    #Clearing the values in order to load the updated values
        sum1=0
        sum2=0
        sum3=0
    
#Plotting the graph
#    print('Predicted values are:',Z)
#    plt.plot(iterations,output,color="blue")
#    plt.xlabel('No. of iterations , i.e j')
#    plt.ylabel('Cost , i.e J(theta)')
#    plt.title('Gradient Descent Algorithm')
    print('Predicted values are:',Z)
    plt.plot(X,Z,color="red")
    plt.xlabel('input X')
    plt.ylabel('predicted value Z')
    plt.title('Logistic Regression')
#Calling the defined function
myFunction()