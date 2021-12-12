from matplotlib.pyplot import title
import numpy as np

from generate_cluster import generate_influencer_matrix, generate_uniform, generate_2_cluster
from post_process import email_blast, friendship
# from bulk_wm_sim_det import bulk_sim_influencer, plot_std, plot_std_n, bulk_sim_2_cluster
from bulk_wm_sim_rand import bulk_sim_influencer, plot_std, plot_std_n, bulk_sim_2_cluster
# from wm_sim_determinisitic import run_sim, plot_results, plot_results_n

#set for simpler printing
np.set_printoptions(precision=4)

# length of the simulation in iterations
sim_length = 200

# size of the population
n = 100
# cluster size
# cs = 5

# A, Lambda, x0 = generate_influencer_matrix(n, cs)
A, Lambda, x0 = generate_2_cluster(n,0.5)
# print("x0: ", x0)
# print(A)
# Lambda = 0

A2 = email_blast(A,100)
A3 = friendship(A,100)
# print(A)

x = bulk_sim_2_cluster(A, n)
x2 = bulk_sim_2_cluster(A2, n)
x3 = bulk_sim_2_cluster(A3, n)

# plot_results(x)
plot_std_n([x,x2,x3])