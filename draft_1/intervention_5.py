import numpy as np

from  generate_cluster import generate_influencer_matrix, generate_uniform, generate_2_cluster
from post_process import email_blast, friendship
from bulk_wm_sim import bulk_sim_influencer, plot_std, bulk_sim_2_cluster

#set for simpler printing
np.set_printoptions(precision=4)

# length of the simulation in iterations
sim_length = 50

# size of the population
n = 10
# cluster size
cs = 5

# A, Lambda, x0 = generate_influencer_matrix(n, cs)
A, Lambda, x0 = generate_2_cluster(n)

A = friendship(A)
# print(A)

x = bulk_sim_2_cluster(A, Lambda, n, 200, 1000)

plot_std(x)