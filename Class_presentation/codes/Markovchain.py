# -*- coding: utf-8 -*-
"""MarkovChain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1raTSZ6lWk5-Ro6z1qIabRc8AhVmJqDuQ
"""

import matplotlib.pyplot as plt
import numpy as np

simlen = int(50000)
X = np.random.geometric(p=0.5, size=simlen)
a=0
b=0

for i in range(0,simlen):
  if(X[i]%3==1):
    a+=1
  else:
    b+=1

print('Theoretical Pr(A wins) = ', 4/7)
print('Simulation Pr(A wins) = ', a/simlen)
print('\nTheoretical Pr(B wins) = ', 3/7)
print('Simulation Pr(B wins) = ', b/simlen)

#plotting
cases = ["A wins","B wins"]

probab_theo = [4/7,3/7]
probab_sim = [a/simlen,b/simlen]

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, probab_sim, color = 'yellow', width = 0.25, label = 'Simulation')
plt.xlabel('Cases')
plt.ylabel('Probabilities')
plt.xticks(x  + 0.25/2,["A wins","B wins"])
plt.legend()
plt.show()