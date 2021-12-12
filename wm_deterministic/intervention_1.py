import numpy as np
import matplotlib.pyplot as plt
from generate_cluster import *
from wm_sim_determinisitic import *

A, Lambda, x0 = generate_2_cluster(100)

# x0 = np.array([0.1]*10)

# A = np.arange(10).tolist()
# A = np.array([A]*10).T
# print(A)

# weighted_median(x0,A)
x = run_sim(A,x0,100)

plot_results(x)