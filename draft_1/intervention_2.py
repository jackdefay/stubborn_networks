import numpy as npA

from  generate_cluster import generate_influencer_matrix
from post_process import friendship
from friedkin_johnsen_sim import run_sim, plot_results

#set for simpler printing
np.set_printoptions(precision=4)

# length of the simulation in iterations
sim_length = 200

# size of the population
n = 10
# cluster size
cs = 5

A, Lambda, x0 = generate_influencer_matrix(n, cs)
# print(A)

# print(A)

x = run_sim(A, Lambda, x0, n, sim_length)

plot_results(x, A)

A = friendship(A)

x = run_sim(A, Lambda, x0, n, sim_length)

plot_results(x, A)