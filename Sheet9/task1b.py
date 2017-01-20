import matplotlib.pyplot as plt
import numpy as np

ITER = 200

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
y1 = np.array([1,0,0])
y2 = np.array([0,1,0])
y3 = np.array([0,0,1])
Q = np.array([y1,y2,y3])
Rn = np.diag(Q)

plt.figure()
for i in range(1,ITER+1):
    x1,x2,x3 = foltowmap(x1,x2,x3)
    D = Dfoltowmap(x1, x2, x3)
    Q,R = np.linalg.qr(np.dot(D,Q))
    Rn = Rn * np.diag(R)
    lya = np.log(abs(Rn))/i
    plt.plot( i, lya[0] ,'_k')
    plt.plot( i, lya[1] ,'r_')
    plt.plot( i, lya[2] ,'_b')
plt.show()
print(lya)

