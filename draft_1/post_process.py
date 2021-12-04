import numpy as np
from generate_cluster import normalize

# Post processes the clustered network to add uniformly small random connections across the graph
# returns: the post processed graph A
# TODO: implement this
def add_noise(A):
    return A


# Simulates an email blast or other low impact wide spread interractions
# evenly spreads val amount of influence over each connection, no self loops
# returns: the post-intervention graph A
def email_blast(A, val):
    #create a matrix full of ones except on self loops
    augment = np.ones(A.shape)
    np.fill_diagonal(augment,0)
    #then scale it such that the entire matrix sums to val
    augment = val*augment/((A.shape[0]-1)*(A.shape[1]-1))

    A = A + augment

    A = normalize(A)

    return A


# Simulates a targetted workshop, speech, or other low yield high impact intervention
# directional friendship, not necessarily symmetric
# returns: the post-intervention graph A
def friendship(A, val):
    # augment = np.random.choice([0, 1], size=A.shape, p=[.7, .3])

    # len+val is the total number of elements in the matrix
    len = A.shape[0]*A.shape[1]-val
    # to account for the diagonal of zeros we are going to add
    len = len-A.shape[0]
    # create val number of ones randomly placed on the matrix
    augment = np.array([1]*val+[0]*len)
    np.random.shuffle(augment)
    # this step must be done last because shuffle only shuffles along a single axis
    augment = augment.reshape(A.shape[0],A.shape[1]-1)
    # print(augment)
    # then, add the zeros
    augment = add_zero_diagonal(augment)
    # print(augment)

    A = A + augment

    A = normalize(A)
    # print(A)

    return A

# helper function that takes an (n,n-1) matrix and adds a diagonal of zeros so it becomes (n,n)
# used to make sure that there are exactly val number of 1's in the augment matrix, without any self loops
# currenly somewhat innefficient, if this could be done with a vectorized function instead...
def add_zero_diagonal(M):
    new_M = []
    for i in range(len(M)):
        new_M.append(np.insert(M[i],i,0))

    return np.array(new_M)