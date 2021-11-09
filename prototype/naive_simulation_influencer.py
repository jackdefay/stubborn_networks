import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io
import igraph as ig

# for this simulation I will use the Friedkin and Johnsen opinion dynamics model
# this is referenced in hw 2 from class

#set for simpler printing
np.set_printoptions(precision=4)

# size of the population
n = 10
# cluster size
cs = 5

# length of the simulation in iterations
sim_length = 200

# list of openness values
lambda_list = np.array([0.9]*(n-1)+[0.1])

Lambda = lambda_list*np.identity(n)

# adjacency matrix, must be row stochastic
# uniformly connected
# A11 = (np.ones((n,n)) - np.identity(n))*0.1
A11 = np.zeros((n,n))
print(A11)
# print(A11[n-1,:]+np.array([0.9]*(n-1)+[0]))

# concatentate together
A = A11
# TODO: check if this should be rows or columns to have one individual influence many others
A[:,n-1] = A11[:,n-1]+np.array([1]*(n-1)+[0])
A[n-1,:] = np.array([1]*(n-1)+[0])
print(A)


# and rescale to be row stochastic
row_sums = A@np.ones(n)
inv_row_sums = np.divide(np.ones(n),row_sums)
A = A.T*inv_row_sums
A = A.T

# print(A)

# the initial opinions of the system
# x0 = np.array([0.8]*cs+[0.2]*(n-cs))
# x0 = np.concatenate((np.random.sample(cs)*0.5+0.5,np.random.sample(n-cs)*0.5),axis=0)
# TODO: replace this with a randomized version
# x0 = np.array([0.1]*(n-1)+[0.9])
x0 = np.concatenate((np.random.sample(n-1)*0.5,np.random.sample(1)*0.5+0.5),axis=0)
print(A)

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

np.set_printoptions(precision=2)
plt.text(11,0.1,A,fontsize=6)

plt.show()
