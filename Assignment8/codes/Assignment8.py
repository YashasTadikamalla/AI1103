import matplotlib.pyplot as plt
import numpy as np

simlen = int(10000)
X = np.random.geometric(p=0.5, size=simlen)
a=0
b=0

for i in range(0,simlen):
  if(X[i]%3==1):
    a+=1
  else:
    b+=1

print('Theoretical Pr(A = win) = ', 0.5714)
print('Simulation Pr(A = win) = ', a/simlen)
print('\nTheoretical Pr(A = win) = ', 0.4285)
print('Simulation Pr(A = win) = ', b/simlen)


#plotting
cases = ["A wins","B wins"]

probab_theo = [0.5714,0.4285]
probab_sim = [a/simlen,b/simlen]

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, probab_sim, color = 'yellow', width = 0.25, label = 'Simulation')
plt.xlabel('Cases')
plt.ylabel('Probabilities')
plt.xticks(x  + 0.25/2,["A wins","B wins"])
plt.legend()
plt.show()