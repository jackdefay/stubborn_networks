from matplotlib.pyplot import title
import numpy as np
from friedkin_johnsen_sim import plot_network

from generate_cluster import generate_influencer_matrix, generate_uniform, generate_2_cluster
from post_process import email_blast, friendship
# from bulk_wm_sim import bulk_sim_influencer, plot_std, plot_std_n, bulk_sim_2_cluster
# from weighted_median_sim import run_sim, plot_results, plot_results_n
from friedkin_johnsen_sim import run_sim, plot_results_n

#set for simpler printing
np.set_printoptions(precision=4)

# length of the simulation in iterations
sim_length = 200

# size of the population
n = 10
# cluster size
cs = 5

# A, Lambda, x0 = generate_influencer_matrix(n, cs)
A, Lambda, x0 = generate_2_cluster(n,0.1)
# print("x0: ", x0)
# print(A)
# Lambda = 0

A2 = email_blast(A,5)
A3 = friendship(A,5)
# print(A)

x = run_sim(A, Lambda, x0, n, sim_length)
x2 = run_sim(A2, Lambda, x0, n, sim_length)
x3 = run_sim(A3, Lambda, x0, n, sim_length)

# plot_results(x)
# plot_results_n([x,x2,x3])
plot_network(A,x0,"No Intervention")
plot_network(A2,x0,"Email Blast")
plot_network(A3,x0,"Friendship")