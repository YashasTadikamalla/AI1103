import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Let us set the number of candies in the bag to 1000
sim_len=int(1000)

#All 1000 candies in the bag are lemon flavoured candy
print("Let the random variable X={0,1} represent the outcome of the flavour of the candy Malini picks.")
print("X=0 denotes an orange flavoured candy, while X=1 denotes a lemon flavoured candy.")

#As picking lemon flavoured candy(i.e, X=1) is a sure event, its probability is 1
prob = 1

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=sim_len,p=prob)

#Calculating the number of favourable outcomes(i.e, X=1)
err_ind = np.nonzero(data_bern)

#calculating the probability
err_n = np.size(err_ind)/sim_len 

#Total no. of orange flavoured candies

#Using simulation
o_sim=sim_len*(1-err_n)

#Using exact probability
o_act=sim_len*(1-prob)

#Theory vs simulation

print("")
print("Number of orange flavoured candies in the bag(i.e, n(X=0)) : ")
print("actual : ",(o_act))
print("simulation : ",(o_sim))
print("")
print("Number of lemon flavoured candies in the bag(i.e, n(X=1)) : ")
print("actual : ",(1000-o_act))
print("simulation : ",(1000-o_sim))
print("")
print("Probability for Malini choosing an orange flavoured candy from the bag(i.e, Pr(X=0)) : ")
print("actual : ",(1-prob))
print("simulation : ",(1-err_n))
print("")
print("Probability for Malini choosing an lemon flavoured candy from the bag(i.e, Pr(X=1)) : ")
print("actual : ",(prob))
print("simulation : ",(err_n))

data1 = {'Orange(X=0)':(o_act), 'Lemon(X=1)':(1000-o_act)}
flavours = list(data1.keys())
numbers = list(data1.values())
  
fig = plt.figure(figsize = (8, 4))
 
# creating the bar plot
plt.bar(flavours, numbers, color ='Yellow',width = 0.08)
plt.xlabel("Flavours of candies")
plt.ylabel("Number of candies")
plt.title("Distribution of the 1000 candies in the bag(actual)")
plt.show()

data2 = {'Orange(X=0)':(o_sim), 'Lemon(X=1)':(1000-o_sim)}
flavours = list(data2.keys())
numbers = list(data2.values())
  
fig = plt.figure(figsize = (8, 4))
 
# creating the bar plot
plt.bar(flavours, numbers, color ='Yellow',width = 0.08)
plt.xlabel("Flavours of candies")
plt.ylabel("Number of candies")
plt.title("Distribution of the 1000 candies in the bag(simulation)")
plt.show()