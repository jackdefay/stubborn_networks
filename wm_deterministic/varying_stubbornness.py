from matplotlib.pyplot import title
import numpy as np
from friedkin_johnsen_sim import plot_network

from generate_cluster import generate_influencer_matrix, generate_uniform, generate_2_cluster
from post_process import email_blast, friendship
# from bulk_wm_sim import bulk_sim_influencer, plot_std, plot_std_n, bulk_sim_2_cluster
# from weighted_median_sim import run_sim, plot_results, plot_results_n
from friedkin_johnsen_sim import run_sim, plot_results_n, plot_results
from bulk_fj_sim import plot_std_n
#set for simpler printing
np.set_printoptions(precision=4)

# length of the simulation in iterations
sim_length = 100

# size of the population
n = 100

A, Lambda, x0 = generate_influencer_matrix(n)
A1, Lambda1, x1 = generate_influencer_matrix(n,num_extremist=10)
A2, Lambda2, x2 = generate_influencer_matrix(n,num_extremist=20)
A3, Lambda3, x3 = generate_influencer_matrix(n,num_extremist=30)
A4, Lambda4, x4 = generate_influencer_matrix(n,num_extremist=40)
A5, Lambda5, x5 = generate_influencer_matrix(n,num_extremist=50)
A6, Lambda6, x6 = generate_influencer_matrix(n,num_extremist=60)



# A, Lambda, x0 = generate_2_cluster(n,0.1)
# print("x0: ", x0)
# print(A)
# Lambda = 0


# print(A)

x = run_sim(A, Lambda, x0, n, sim_length)
xx1 = run_sim(A,Lambda1,x1, n, sim_length)
xx2 = run_sim(A,Lambda2,x2, n, sim_length)
xx3 = run_sim(A,Lambda3,x3, n, sim_length)
xx4 = run_sim(A,Lambda4,x4, n, sim_length)
xx5 = run_sim(A,Lambda5,x5, n, sim_length)
xx6 = run_sim(A,Lambda6,x6, n, sim_length)

plot_results(x,x0,"Stubborn Percentage=1%")
plot_results(xx1,x1,"Stubborn Percentage=10%")
plot_results(xx2,x2,"Stubborn Percentage=20%")
plot_results(xx3,x3,"Stubborn Percentage=30%")
plot_results(xx4,x4,"Stubborn Percentage=40%")
plot_results(xx5,x5,"Stubborn Percentage=50%")
plot_results(xx6,x6,"Stubborn Percentage=60%")

# plot_results(x1,x0,"Opinion Openness=0.1")
# plot_results(x2,x0,"Opinion Openness=0.9")

# plot_results_n([x,x1,x2],["Open 0.5","Open 0.1","Open 0.9"])

# plot_network(A,x0,"1 Stubborn Influencer")
# plot_std_n([x1,x,x2],["Open 0.1","Open 0.5","Open 0.9"])
plot_std_n([x,xx1,xx2,xx3,xx4,xx5,xx6],["1","10","20","30","40","50","60"])