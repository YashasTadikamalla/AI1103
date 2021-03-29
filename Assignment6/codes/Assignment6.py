import random
import matplotlib.pyplot as plt

simlen =int(10000)
count=0
for i in range (0,simlen): 
  n=random.randint(10,99)
  if(n%7!=0):
    count+=1
prob=count/simlen
prob_th=77/90
print("The theoretical probability is ",prob_th)
print("The simulation probability is ",prob)

data = {'Theoretical':prob_th, 'Simulation':prob}
Cases = list(data.keys())
probs = list(data.values())
  
fig = plt.figure(figsize = (6, 4))
 
# creating the bar plot
plt.bar(Cases, probs, color ='Red',width = 0.25)
plt.ylabel("Probability")
plt.show()