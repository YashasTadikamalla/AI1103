import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.arange(-2, 2, 0.5)
y = np.arange(-2, 2, 0.5)

X, Y = np.meshgrid(x, y)
nu1 = X*X+X*Y+Y*Y
nu2=-nu1

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, nu1)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,nu2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()