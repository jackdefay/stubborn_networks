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

# n is the size of the matrix
# cs is the cluster size
# returns: an ajacency matrix of uniformly connected individuals with one stubborn influencer,
# influence values,
# initial opinions of the sytem
def generate_influencer_matrix(n=10, cs=5):

    # list of openness values
    lambda_list = np.array([0.9]*(n-1)+[0.1])

    Lambda = lambda_list*np.identity(n)

    # adjacency matrix, must be row stochastic
    # uniformly connected
    # A11 = (np.ones((n,n)) - np.identity(n))*0.1
    A11 = np.zeros((n,n))
    # print(A11)
    # print(A11[n-1,:]+np.array([0.9]*(n-1)+[0]))

    # concatentate together
    A = A11
    # TODO: check if this should be rows or columns to have one individual influence many others
    A[:,n-1] = A11[:,n-1]+np.array([1]*(n-1)+[0])
    A[n-1,:] = np.array([1]*(n-1)+[0])
    # print(A)


    # and rescale to be row stochastic
    row_sums = A@np.ones(n)
    inv_row_sums = np.divide(np.ones(n),row_sums)
    A = A.T*inv_row_sums
    A = A.T

    # print(A)

    # the initial opinions of the system
    x0 = np.concatenate((np.random.sample(n-1)*0.5,np.random.sample(1)*0.5+0.5),axis=0)
    # print(A)
    return [A,Lambda,x0]


# n is the size of the matrix
# cs is the cluster size
# returns: an ajacency matrix of two groups: strongly connected cluster and uniformly connected individuals,
# influence values,
# initial opinions of the sytem
def generate_cluster(n=10, cs=5):

    A=0
    Lambda=0
    x0=0

    return [A,Lambda,x0]

def generate_uniform(n=10,cs=5):
    A = np.ones((n,n))
    A=normalize(A)

    x0 = np.random.sample(n)
    return [A,x0]