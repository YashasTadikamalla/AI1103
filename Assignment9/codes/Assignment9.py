import matplotlib.pyplot as plt
import numpy as np
import math

n=int(1000000)
def F(x):
    if(x<=0):
        return 0
    elif(x>0):
        return 1-np.exp(-x)
    
    
X = np.linspace(-20,50,1000)
Y = [F(x) for x in X]

plt.plot(X,Y)
plt.xlabel('$x$')
plt.ylabel('$\lim_{n=\infty}F_{n(1-T_{n})}(x)$')
plt.title('Cumulative Distribution Function')
plt.grid()
plt.show()