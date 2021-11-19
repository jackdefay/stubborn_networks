import numpy as np
import matplotlib.pyplot as plt

#set for simpler printing
np.set_printoptions(precision=4)

# runs the simulation using the Friedkin and Johnsen model
# returns: the itaterted opinion list x
def run_sim(A, Lambda, x0, n, sim_length=200):

    # initialize the list of the state of the system
    x = [x0]

    # simulation on a for loop
    for i in range(0,sim_length):
        x_temp = np.zeros(len(x0))
        for row in range(n):
            # print(A[row])
            # print(x0)
            w = np.random.choice(x[i], size=1, p=A[row])
            # print(w)
            x_temp[row] = w
        x.append(x_temp)
    
    return x

# plots the opinion list over time and an insert for the adjacency matrix, A
def plot_results(x,A):
    plot_data = np.array(x).T

    for row in plot_data:
        plt.plot(row, alpha=0.7)

    plt.xlabel("number of iterations")
    plt.ylabel("opinion")
    plt.title("Opinion Dynamics")

    np.set_printoptions(precision=2)
    plt.text(11,0.1,A,fontsize=6)

    plt.show()
