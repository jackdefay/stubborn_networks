import numpy as np

from  generate_cluster import generate_influencer_matrix, generate_uniform
from post_process import email_blast
from weighted_median_sim import run_sim, plot_results

#set for simpler printing
np.set_printoptions(precision=4)

# length of the simulation in iterations
sim_length = 50

# size of the population
n = 10
# cluster size
cs = 5

A, x0 = generate_uniform(n, cs)
# print(A)

# print(A)
Lambda = 0

x = run_sim(A, Lambda, x0, n, sim_length)

plot_results(x, A)

# A = email_blast(A)

# x = run_sim(A, Lambda, x0, n, sim_length)

# plot_results(x, A)