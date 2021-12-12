import numpy as np
import matplotlib.pyplot as plt

#set for simpler printing
np.set_printoptions(precision=4)

# runs the simulation using the Friedkin and Johnsen model
# returns: the itaterted opinion list x
def run_sim(A, x0, sim_length=200):

    # initialize the list of the state of the system
    x = [x0]

    # simulation on a for loop
    for i in range(0,sim_length):
        ids = weighted_median(x[i],A)
        x_temp = x[i][ids]
        # print(x_temp)
        x.append(x_temp)
    
    return x

# data = x[i], weights = A
# only issue right now is that the argmin returns the first value, which has no real meaning
def weighted_median(data, weights):
    # take the argsort of the opinions which will be used to order the weights for cumsum
    id_sort = np.argsort(data)
    # rearrange the weights by column
    weights = weights[id_sort,:]
    # find the cumulative sum of the weights
    cs_weights = np.cumsum(weights,axis=0)
    # subtract 0.5 from each value
    cs_weights -= 0.5
    # then take the abs so that the minimum value is the one closest to 0.5
    cs_weights = np.abs(cs_weights)
    # finally, take the argmin, double check the axis
    id = np.argmin(cs_weights,axis=0)
    return id

# plots the opinion list over time and an insert for the adjacency matrix, A
def plot_results(x):
    plot_data = np.array(x).T

    for row in plot_data:
        plt.plot(row, alpha=0.5)

    plt.xlabel("number of iterations")
    plt.ylabel("opinion")
    plt.title("Opinion Dynamics")

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)

    plt.show()

def plot_results_n(xlist):
    colorlist = ['blue', 'orange', 'green']
    linelist = []
    
    for i in range(len(xlist)):
        x=xlist[i]
        c=colorlist[i]
        plot_data = np.array(x).T

        for row in plot_data:
            line, = plt.plot(row, alpha=0.3, color=c)
            linelist.append(line)

    plt.xlabel("number of iterations")
    plt.ylabel("opinion")
    plt.title("Opinion Dynamics")

    lines = [linelist[0],linelist[101],linelist[201]]

    plt.legend(lines, ['no intervention', 'emails', 'friendship'])

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)

    plt.show()