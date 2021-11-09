import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io
import igraph as ig

# for this simulation I will use the Friedkin and Johnsen opinion dynamics model
# this is referenced in hw 2 from class

# size of the population
n = 10
# cluster size
cs = 5

# length of the simulation in iterations
sim_length = 20

# list of openness values
lambda_list = np.array([0.9]*n)

Lambda = lambda_list*np.identity(n)

# adjacency matrix, must be row stochastic
# uniformly connected
A11 = (np.ones((cs,cs)) - np.identity(cs))*0.9
A21 = np.ones((n-cs,cs))*0.1
A12 = np.ones((cs,n-cs))*0.1
A22 = (np.ones((n-cs,n-cs)) - np.identity(n-cs))*0.1

# concatentate together
A = np.concatenate((np.concatenate((A11,A12),axis=1),np.concatenate((A21,A22),axis=1)),axis=0)


# and rescale to be row stochastic
row_sums = A@np.ones(n)
inv_row_sums = np.divide(np.ones(n),row_sums)
A = A.T*inv_row_sums
A = A.T

# print(A)

# the initial opinions of the system
# x0 = np.array([0.8]*cs+[0.2]*(n-cs))
x0 = np.concatenate((np.random.sample(cs)*0.5+0.5,np.random.sample(n-cs)*0.5),axis=0)
print(x0)

# initialize the list of the state of the system
x = [x0]

# simulation on a for loop
for i in range(0,sim_length):
    temp1 = Lambda@A@x[i]
    temp2 = (np.identity(n)-Lambda)@x0
    x.append(temp1 + temp2)
#     print(temp1)
#     print(temp2)

# print(Lambda@A@x0)

print(np.array(x))
# print(A)

plot_data = np.array(x).T

for row in plot_data:
    plt.plot(row, alpha=0.7)

plt.xlabel("number of iterations")
plt.ylabel("opinion")
plt.title("Opinion Dynamics")

plt.show()
