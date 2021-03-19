import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

#function to calculate factorial
def fact(a):
  ans = 1
  for x in range(1 , a + 1):
    ans = ans * x
  return ans

#function to calculate binomial coefficient
def ncr(n , r):
  ans = fact_func(n) / (fact_func(r) * fact_func(n - r))
  return ans

n = 2
p = 1 / 3
q = 2 / 3

print("Let the random variable X_1, X_2 = {0,1} represent the outcome of the colour of the ball drawn in the first, second attempts.")
print("X_i=0, X_i=1 denote a white ball, red ball being drawn respectively, in the i-th attempt.")
print("The random variable X={0,1,2} denotes the number of red balls drawn in both the attempts.")

k = 9000
sample_space = np.random.binomial(n,p,k)
count_0 = 0
for i in sample_space:
  if i == 0:
    count_0 = count_0 + 1
prob_0 = count_0 / k

count_1 = 0
for i in sample_space:
  if i == 1:
    count_1 = count_1 + 1
prob_1 = count_1 / k

count_2 = 0
for i in sample_space:
  if i == 2:
    count_2 = count_2 + 1
prob_2 = count_2 / k

print("\nWhen we conduct the experiment 9000 times, the distribution of X is as follows : ")
print("Theoretical : \nn(X=0) : %d\nn(X=1) : %d\nn(X=2) : %d"%(4000,4000,1000))
print("\nSimulation : \nn(X=0) : %d\nn(X=1) : %d\nn(X=2) : %d"%(count_0,count_1,count_2))
print('\nAlso, the probabilities are :')
print("Theoretical : \nPr(X=0) : %lf\nPr(X=1) : %lf\nPr(X=2) : %lf"%(4.0/9,4.0/9,1.0/9))
print("\nSimulation : \nn(X=0) : %lf\nn(X=1) : %lf\nn(X=2) : %lf"%(prob_0,prob_1,prob_2))

#plotting

cases_1 = ["X=0","X=1","X=2"]

count_theo = [4000,4000,1000]
count_sim = [count_0,count_1,count_2]

x = np.arange(len(cases_1))
plt.bar(x + 0.00, count_theo, color = 'skyblue', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, count_sim, color = 'yellow', width = 0.25, label = 'Simulation')
plt.xlabel('Number of red balls in one experiment')
plt.ylabel('Frequencies')
plt.title('Frequency distribution of X, after the experiment is conducted 9000 times')
plt.xticks(x  + 0.25/2,["X=0","X=1","X=2"])
plt.legend()
plt.show()

cases_2 = ["X=0","X=1","X=2"]

prob_theo = [4.0/9,4.0/9,1.0/9]
prob_sim = [prob_0,prob_1,prob_2]

x = np.arange(len(cases_2))
plt.bar(x + 0.00, prob_theo, color = 'skyblue', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, prob_sim, color = 'yellow', width = 0.25, label = 'Simulation')
plt.xlabel('Number of red balls in one experiment')
plt.ylabel('Probabilties')
plt.title('Probabilitiy distribution of X, after the experiment is conducted 9000 times')
plt.xticks(x  + 0.25/2,["X=0","X=1","X=2"])
plt.legend()
plt.show()