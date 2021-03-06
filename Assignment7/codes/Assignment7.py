import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

simlen = int(10000)

#probabilities
prob_m= prob_f= 0.5
prob_emp_m = 0.8      #Probability that the person is employed, given that its a male
prob_emp_f = 0.5      #Probability that the person is employed, given that its a female
prob_th=0.65

#Using Bernoulli Random Variable
data_bern_m = bernoulli.rvs(size = simlen, p = prob_emp_m)      #A bernoulli distribution simulating employement of male
data_bern_f = bernoulli.rvs(size = simlen, p = prob_emp_f)      #A bernoulli distribution simulating employement of female

#Calculating the number of favourable outcomes
err_ind_m = np.nonzero(data_bern_m == 1)
err_ind_f = np.nonzero(data_bern_f == 1)

#Calculating the probabilities
err_n_m = np.size(err_ind_m)/simlen
err_n_f = np.size(err_ind_f)/simlen

exp_prob = err_n_m*(0.5)+err_n_f*(0.5)      #experimental probability

print("The Experimental Probability is : ",exp_prob)
print("The Theoretical Probability is : ",prob_th)