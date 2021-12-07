import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

#set for simpler printing
np.set_printoptions(precision=4)

# runs the simulation using the Friedkin and Johnsen model
# returns: the itaterted opinion list x
def run_sim(A, Lambda, x0, n, sim_length=200):

    # initialize the list of the state of the system
    x = [x0]

    # simulation on a for loop
    for i in range(0,sim_length):
        temp1 = Lambda@A@x[i]
        # print(np.identity(n))
        # print(Lambda)
        # print(x0)
        temp2 = (np.identity(n)-Lambda)@x0
        x.append(temp1 + temp2)
    #     print(temp1)
    #     print(temp2)

    # print(Lambda@A@x0)

    # print(np.array(x))
    # print(A)
    # print(x)
    
    return x

# plots the opinion list over time and an insert for the initial opinions x0
def plot_results(x,x0,title):
    plot_data = np.array(x).T

    for row in plot_data:
        plt.plot(row, alpha=0.7)

    plt.xlabel("number of iterations")
    plt.ylabel("opinion")
    plt.title(title)

    np.set_printoptions(precision=2)
    plt.text(11,0.1,x0,fontsize=6)

    plt.show()

def plot_results_n(xlist,legend_list=['no intervention', 'emails', 'friendship']):
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

    plt.legend(lines, legend_list)

    # np.set_printoptions(precision=2)
    # plt.text(11,0.1,A,fontsize=6)

    plt.show()

def plot_network(A,x0,title):
    colors = ["pink"]*len(x0)
    # for i,opinion in enumerate(x0):
    #     print(opinion)
    #     if opinion>0.5:
    #         colors[i]='green'
    #     elif opinion<0.5:
    #         colors[i]='red'
    rows, cols = np.where(A != 0)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    x0 = np.round_(x0,decimals=2)
    mylabels={v: k for v, k in enumerate(x0)}
    plt.title(title)
    nx.draw(gr, node_size=600,node_color=colors, alpha=0.7,labels=mylabels, with_labels=True)    
    plt.show()