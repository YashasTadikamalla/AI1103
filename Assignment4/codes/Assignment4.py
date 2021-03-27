import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

simlen = int(10000)
count =0
prob_th=1 

for i in range (0,1000):
#Let 1=[X_i=2], 0=[X_i=1]
    data_bern = bernoulli.rvs(size = simlen, p = 0.75) 

    err_ind = np.nonzero(data_bern == 1)
    err_n = np.size(err_ind)

    X_n=(err_n*(2.0)+(simlen-err_n))/simlen

    if(X_n<=1.8):
        count+=1
print("The experimental probability is : ",(count/1000))
print("The theoretical probability is : ",prob_th)