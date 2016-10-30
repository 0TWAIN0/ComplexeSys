import matplotlib.pyplot as plt
import numpy as np
from numpy import ma

a = 0.1
b = 0.1
c = 0.1
d = 0.2

X, Y = np.meshgrid(np.arange(0, 2, .12), np.arange(0, 2, .1))
U = a*(1-X)*X - c*X*Y
V = d*X*Y - b*Y

# 1
fig1, (ax1, ax2) = plt.subplots(ncols=2)
ax1.streamplot(X,Y,U, V)
ax2.quiver(X,Y,U, V)
plt.show();
