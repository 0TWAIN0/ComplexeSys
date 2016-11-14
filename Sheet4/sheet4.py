import matplotlib.pyplot as plt
import numpy as np
from numpy import ma

a = 0.1

X, Y = np.meshgrid(np.arange(-10, 10, .05), np.arange(-10, 10, .05))
U = Y
V = -a*Y*X**2 - a * Y**3 + a*Y -X

# 1
ax1 = plt.figure()
plt.streamplot(X,Y,U, V)
plt.show();
