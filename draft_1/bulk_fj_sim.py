import numpy as np
import matplotlib.pyplot as plt
from weighted_median_sim import run_sim

def bulk_sim_influencer(A, Lambda, n, sim_length=200, iterations=100):
    x = []
    for i in range(iterations):
        #new random initial opinions for influencer model
        x0 = np.concatenate((np.random.sample(n-1)*0.5,np.random.sample(1)*0.5+0.5),axis=0)
        xi = run_sim(A,Lambda,x0,n,sim_length)
        x.append(xi[-1])

    return x

def bulk_sim_2_cluster(A, Lambda, n, sim_length=200, iterations=100):
    m= int(n/2)
    x = []
    for i in range(iterations):
        #new random initial opinions for influencer model
        x0 = np.concatenate((np.random.sample(m)*0.1+0.9,np.random.sample(m)*0.1),axis=0)
        xi = run_sim(A,Lambda,x0,n,sim_length)
        x.append(xi[-1])

    return x


# plots the opinion list over time and an insert for the adjacency matrix, A
def plot_std(x):
    # print(x)

    std = np.std(x,axis=1)
    # print(std)

    plt.hist(std,rwidth=0.9)

    plt.xlabel("std of sim after 200 iterations")
    plt.ylabel("number of iterations")
    plt.title("Opinion Dynamics")

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)

    plt.show()