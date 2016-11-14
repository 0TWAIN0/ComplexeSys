
from scipy.integrate import ode
import matplotlib.pyplot as plt

c = 1

def f(t,x, arg1):
    return [ x[1], -c * x[1] + x[0] - x[0]**3]

def jac(t, x, arg1):
    return [[0, 1], [ 1-3*x[0]**2,-c]]


def RobIsInt(t0,x0,style):
    r = ode(f, jac).set_integrator('dopri5')
    r.set_initial_value( x0, t0).set_f_params(2.0).set_jac_params(2.0)
    t1 = 100
    dt = 0.1

    while r.successful() and r.t < t1:
        temp = r.integrate(r.t+dt)
        #print(r.t+dt, temp)
        plt.plot(temp[0], temp[1],style)

plt.figure()
RobIsInt(0,[0,3],'ro')
RobIsInt(0,[0,2],'bo')
RobIsInt(0,[2,0],'go')
RobIsInt(0,[3,0],'yo')
plt.show()
