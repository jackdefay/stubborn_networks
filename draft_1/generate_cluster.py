import numpy as np

# re-normalizes the matrix to be row stochastic
def normalize(A):
    # zero out the self loops because fj doesn't allow them
    np.fill_diagonal(A,0)
    n=A.shape[0]
    # divide each row by its sum to make it row-stochastic
    row_sums = A@np.ones(n)
    inv_row_sums = np.divide(np.ones(n),row_sums)
    # must transpose for the shape to line up
    A = A.T*inv_row_sums
    # then un-transpose
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

    A11 = np.zeros((n,n))

    # concatentate together
    A = A11
    A[:,n-1] = A11[:,n-1]+np.array([1]*(n-1)+[0])
    A[n-1,:] = np.array([1]*(n-1)+[0])

    # and rescale to be row stochastic
    A=normalize(A)

    # the initial opinions of the system
    x0 = np.concatenate((np.random.sample(n-1)*0.5,np.random.sample(1)*0.5+0.5),axis=0)

    # print(A)
    return [A,Lambda,x0]


# n is the size of the matrix
# cs is the cluster size
# returns: an ajacency matrix of two groups: strongly connected cluster and uniformly connected individuals,
# influence values,
# initial opinions of the sytem
# TODO: implement this function
def generate_cluster(n=10, cs=5):

    A=0
    Lambda=0
    x0=0

    return [A,Lambda,x0]

# generates a uniformly distributed adjacency matrix
# returns: the matrix and a randomly initialized set of initial opinions between [0,1]
def generate_uniform(n=10,cs=5):
    A = np.ones((n,n))
    A=normalize(A)

    x0 = np.random.sample(n)
    return [A,x0]

# generates the adjacency matrix for two completely separate clusters as a starting point for experiments
# n must be an even number
# returns: the adjacency matrix, the influence matrix, and the randomized initial opinions (group 1 [0,0.5], group 2 [0.5,1])
def generate_2_cluster(n=10):
    # list of openness values
    lambda_list = np.array([0.3]*n)

    Lambda = lambda_list*np.identity(n)

    # adjacency matrix, must be row stochastic
    # uniformly connected
    m = int(n/2)
    A11 = (np.ones((m,m)) - np.identity(m))
    A21 = np.zeros((m,m))

    # concatentate together
    A = np.concatenate((np.concatenate((A11,A21),axis=1),np.concatenate((A21,A11),axis=1)),axis=0)

    A = normalize(A)

    x0 = np.concatenate((np.random.sample(m)*0.1+0.9,np.random.sample(m)*0.1),axis=0)

    return [A,Lambda,x0]