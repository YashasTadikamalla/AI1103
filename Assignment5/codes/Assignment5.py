import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

simlen = int(10000)

#probabilities
prob_t1= prob_t2= 0.5
prob_lasts_t1 = 0.7      #Probability that the bulb lasts more than 100hrs, given that its of type1
prob_lasts_t2 = 0.4      #Probability that the bulb lasts more than 100hrs, given that its of type2
prob_th=0.55

#Using Bernoulli Random Variable
data_bern_t1 = bernoulli.rvs(size = simlen, p = prob_lasts_t1)      #A bernoulli distribution simulating number of bulbs of type1 which last more than 100hrs
data_bern_t2 = bernoulli.rvs(size = simlen, p = prob_lasts_t2)      #A bernoulli distribution simulating number of bulbs of type1 which last more than 100hrs

#Calculating the number of favourable outcomes
err_ind_t1 = np.nonzero(data_bern_t1 == 1)
err_ind_t2 = np.nonzero(data_bern_t2 == 1)

#Calculating the probabilities
err_n_t1 = np.size(err_ind_t1)/simlen
err_n_t2 = np.size(err_ind_t2)/simlen

exp_prob = err_n_t1*(0.5)+err_n_t2*(0.5)      #experimental probability

print("The Experimental Probability is : ",exp_prob)
print("The Theoretical Probability is : ",prob_th)