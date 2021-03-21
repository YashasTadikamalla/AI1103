import numpy as np
from scipy.stats import bernoulli
import random
import matplotlib.pyplot as plt

#theoretical value
pr_th_1=5.0/12
pr_th_2=5.0/12
pr_th_3=2.0/12

sample_size=10000
count_1=0
count_2=0
count_3=0
#initialise
sample_1=[0]*sample_size
sample_2=[0]*sample_size

# assigning random values between 1 and 6
for i in range(sample_size):
    sample_1[i],sample_2[i]=int(6*random.random()+1),int(6*random.random()+1)

for i in range(sample_size):
    if (sample_2[i]>sample_1[i]):
      count_1+=1
    elif (sample_2[i]<sample_1[i]):
      count_2+=1
    else :
      count_3+=1

pr_sim_1=count_1/sample_size
pr_sim_2=count_2/sample_size
pr_sim_3=count_3/sample_size

print("A fair dice is tossed two times.")
print("\nThe probability for the result of second toss being higher than the first toss is : ")
print("Theoretical probability = %f\nSimulation probability = %f"%(pr_th_1,pr_sim_1))
print("\nSimilarly, we can caluclate the probability for the result of first toss being higher than the second toss is : ")
print("Theoretical probability = %f\nSimulation probability = %f"%(pr_th_2,pr_sim_2))
print("\nAlso, the probability for the result of first toss being equal to that of the second toss is : ")
print("Theoretical probability = %f\nSimulation probability = %f"%(pr_th_3,pr_sim_3))


#plotting
cases = ["X_1<X_2","X_1>X_2","X_1=X_2"]

probab_theo = [pr_th_1,pr_th_2,pr_th_3]
probab_sim = [pr_sim_1,pr_sim_2,pr_sim_3]

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, probab_sim, color = 'yellow', width = 0.25, label = 'Simulation')
plt.xlabel('Cases')
plt.ylabel('Probabilities')
plt.xticks(x  + 0.25/2,["X_1<X_2","X_1>X_2","X_1=X_2"])
plt.legend()
plt.show()

