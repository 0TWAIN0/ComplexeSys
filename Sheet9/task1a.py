#1a D*D*D*D*D

import matplotlib.pyplot as plt
import numpy as np

ITER = 1000

def foltowmap(x1,x2,x3):
    return (3.8 * x1 * (1.-x1) - 0.05 * (x2 + 0.35) * (1.-2.*x3),
            0.1 * ((x2 + 0.35) * (1.-2.*x3) - 1) * (1. - 1.9 * x1),
            3.78 * x3 * (1. - x3) + 0.2 * x2)

def Dfoltowmap(x1, x2, x3):
    return np.array( [ [3.8 * (1 - x1) - 3.8 * x1 , -0.05 * (1 - 2 * x3) , 0.1 * (x2 + 0.35)],
                         [-0.19 * ((x2 + 0.35) * (1 - 2 * x3) - 1) , 0.1 * (1 - 1.9 * x1) * (1 - 2 * x3) , -0.2 * (1 - 1.9 * x1) * (x2 + 0.35)],
                         [0 , 0.2 , 3.78 * (1 - x3) - 3.78 * x3 ] ] )
x1 = 0.5
x2 = 0
x3 = 0
D = Dfoltowmap(x1,x2,x3)
y1 = 0.1
y2 = 0
y3 = 0

plt.figure()
plt.ylim([0.2,0.6])

for i in range(0,ITER):
    x1,x2,x3 = foltowmap(x1,x2,x3)
    D = np.dot(Dfoltowmap(x1,x2,x3), D)
    yn = np.dot(D, np.array([y1,y2,y3]))
    lamda1 = np.log(np.sqrt(np.dot(yn,yn)) / 
                    np.sqrt((y1*y1 + y2*y2 + y3*y3)))/(i+1)
    #print(np.dot(yn,yn))
    #if np.mod(i,10) == 0 : print( i, np.dot(yn,yn))
    plt.plot( i, lamda1 ,'.k')
plt.show()
 

