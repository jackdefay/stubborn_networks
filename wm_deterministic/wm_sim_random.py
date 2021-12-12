import numpy as np
import matplotlib.pyplot as plt

#set for simpler printing
np.set_printoptions(precision=4)

# runs the simulation using the Friedkin and Johnsen model
# returns: the itaterted opinion list x
def run_sim(A, x0, n, sim_length=200):

    # initialize the list of the state of the system
    x = [x0]

    # simulation on a for loop
    for i in range(0,sim_length):
        x_temp = np.zeros(len(x0))
        for row in range(n):
            w = np.random.choice(x[i], size=1, p=A[row])
            x_temp[row] = w
        x.append(x_temp)
    
    return x

# plots the opinion list over time and an insert for the adjacency matrix, A
def plot_results(x,A):
    plot_data = np.array(x).T

    for row in plot_data:
        plt.plot(row, alpha=0.5)

    plt.xlabel("number of iterations")
    plt.ylabel("opinion")
    plt.title("Opinion Dynamics")

    np.set_printoptions(precision=2)
    plt.text(11,0.1,A,fontsize=6)

    plt.show()

def plot_results_n(xlist):
    colorlist = ['blue', 'orange', 'green']
    linelist = []
    
    for i in range(len(xlist)):
        x=xlist[i]
        c=colorlist[i]
        plot_data = np.array(x).T

        for row in plot_data:
            line, = plt.plot(row, alpha=0.5, color=c)
            linelist.append(line)

    plt.xlabel("number of iterations")
    plt.ylabel("opinion")
    plt.title("Opinion Dynamics")

    lines = [linelist[0],linelist[11],linelist[21]]

    plt.legend(lines, ['no intervention', 'emails', 'friendship'])

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)

    plt.show()