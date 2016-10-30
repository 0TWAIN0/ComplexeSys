from scipy.integrate import ode
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

alpha = beta = 0.5

def f(t,x, arg1):
    return [-2*x[0]-x[1]**2, -x[1]-x[0]**2]

def jac(t, x, arg1):
    return [[-2, -2*x[1]], [-2*x[0],-1]]


def RobIsInt(t0,x0):
    r = ode(f, jac).set_integrator('dopri5')
    r.set_initial_value( x0, t0).set_f_params(2.0).set_jac_params(2.0)
    t1 = 100
    dt = 0.1
    y = np.zeros((t1/dt+1, 3))
    i=0
    while r.successful() and r.t < t1:
        y[i,0:2] = r.integrate(r.t+dt)
        y[i,2] = 0.5*(alpha*y[i,0]**2 + beta*y[i,1]**2)
        print(r.t+dt, y[i,:])
        #ax.plot(temp[0],temp[1],4,'r')
        i = i+1
    return y


xlim = (-.5,.5)
ylim = (-1,1)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(35, -28)
ax.set_xlim(xlim)
ax.set_ylim(ylim)


X, Y = np.meshgrid(np.arange(-0.5, 0.5, .1), np.arange(-1, 1, .1))
Z = 0.5*(alpha * X**2 + beta * Y**2)


surf = ax.plot_surface(X,Y,Z, rstride=1, cstride=1, alpha=.5)

y = RobIsInt(0,[0.5,1])
ax.plot(y[:,0], y[:,1], y[:,2],color='r')

y = RobIsInt(0,[-0.5,0.6])
ax.plot(y[:,0], y[:,1], y[:,2],color='y')

y = RobIsInt(0,[0.5,-1])
ax.plot(y[:,0], y[:,1], y[:,2],color='b')

plt.show()

