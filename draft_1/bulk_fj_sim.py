import numpy as np
import matplotlib.pyplot as plt
from friedkin_johnsen_sim import run_sim

# runs iteration number of trials of the weighted median simulation of an influencer matrix
# returns: x, the list of the final opinions of each trial. size (n,iterations)
# on the plots iterations is labeled repetitions
def bulk_sim_influencer(A, Lambda, n, sim_length=200, iterations=100):
    x = []
    for i in range(iterations):
        #new random initial opinions for influencer model
        x0 = np.concatenate((np.random.sample(n-1)*0.5,np.random.sample(1)*0.5+0.5),axis=0)
        xi = run_sim(A,Lambda,x0,n,sim_length)
        x.append(xi[-1])

    return x

# runs iteration number of trials of the weighted median simulation of the 2 cluster influencer matrix
# returns: x, the list of the final opinions of each trial. size (n,iterations)
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
    plt.xlabel("Standard Dev Final Opinions")
    plt.ylabel("Number of Repetitions")
    plt.title("Opinion Dynamics")

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)

    plt.show()

# plots the opinion list over time and an insert for the adjacency matrix, A
def plot_std2(x,x2):
    # print(x)

    std = np.std(x,axis=1)
    std2 = np.std(x2,axis=1)
    # print(std)

    plt.hist(std,rwidth=0.9,alpha=0.5)
    plt.hist(std2,rwidth=0.9,alpha=0.5)

    plt.xlabel("std of sim after 200 iterations")
    plt.ylabel("number of repetitions")
    plt.title("Opinion Dynamics")

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)
    plt.legend(["email","friendship"])

    plt.show()

# plots the opinion list over time and an insert for the adjacency matrix, A
def plot_std_n(xlist,legend_list=["no intervention","email","friendship"]):
    # print(x)

    for x in xlist:
        std = np.std(x,axis=1)
        plt.hist(std,rwidth=0.9,alpha=0.5)

    plt.xlabel("std of sim after 200 iterations")
    plt.ylabel("number of repetitions")
    plt.title("Opinion Dynamics")

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)
    plt.legend(legend_list)

    plt.show()