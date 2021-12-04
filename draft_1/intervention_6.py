import numpy as np

from  generate_cluster import generate_influencer_matrix, generate_uniform, generate_2_cluster
from post_process import email_blast, friendship
from bulk_fj_sim import bulk_sim_influencer, plot_std, plot_std2, plot_std_n, bulk_sim_2_cluster

#set for simpler printing
np.set_printoptions(precision=4)

# length of the simulation in iterations
sim_length = 50

# size of the population
n = 100
# cluster size
cs = 5

# A, Lambda, x0 = generate_influencer_matrix(n, cs)
A, Lambda, x0 = generate_2_cluster(n)
# print(A)

# print(A)
# Lambda = 0

# A = email_blast(A)

A2 = email_blast(A,50)
A3 = friendship(A,50)
# print(A)

x = bulk_sim_2_cluster(A, Lambda, n, sim_length, 1000)
x2 = bulk_sim_2_cluster(A2, Lambda, n, sim_length, 1000)
x3 = bulk_sim_2_cluster(A3, Lambda, n, sim_length, 1000)

plot_std_n([x,x2,x3])