import numpy as np

# re-normalizes the matrix to be row stochastic
def normalize(A):
    np.fill_diagonal(A,0)
    n=A.shape[0]
    row_sums = A@np.ones(n)
    inv_row_sums = np.divide(np.ones(n),row_sums)
    A = A.T*inv_row_sums
    A = A.T
    return A

# Post processes the clustered network to add uniformly small random connections across the graph
# returns: the post processed graph A
def add_noise(A):
    return A


# Simulates an email blast or other low impact wide spread interractions
# returns: the post-intervention graph A
def email_blast(A):
    augment = np.ones(A.shape)/(A.shape[0])

    A = A + augment

    A = normalize(A)

    return A


# Simulates a targetted workshop, speech, or other low yield high impact intervention
# returns: the post-intervention graph A
def friendship(A):
    augment = np.random.choice([0, 1], size=A.shape, p=[.7, .3])

    A = A + augment

    A = normalize(A)
    print(A)

    return A