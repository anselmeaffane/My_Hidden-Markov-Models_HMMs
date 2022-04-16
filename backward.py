import pandas as pd
import numpy as np

#states = PATH1, PATH2, PATH3, PATH4 = 0, 1, 2, 3

V = np.array([3, 3, 2, 1, 2, 2, 1, 2, 3, 0])

# Transition Probabilities
A = np.array(((0.3, 0.2, 0.2, 0.3), (0.2, 0.3, 0.2, 0.3), (0.2, 0.2, 0.3, 0.3), (0.2, 0.2, 0.2, 0.4)))

# Emission Probabilities
B = np.array(((0.3, 0.3, 0.3, 0.1), (0.3, 0.3, 0.3, 0.1), (0.3, 0.3, 0.3, 0.1), (0.1, 0.1, 0.1, 0.7)))

# Equal Probabilities for the initial distribution
initial_distribution = np.array((0.2, 0.2, 0.2, 0.4))


def backward(V, A, B):
    beta = np.zeros((V.shape[0], A.shape[0]))

    # setting beta(T) = 1
    beta[V.shape[0] - 1] = np.ones((A.shape[0]))

    # Loop in backward way from T-1 to
    # Due to python indexing the actual loop will be T-2 to 0
    for t in range(V.shape[0] - 2, -1, -1):
        for j in range(A.shape[0]):
            beta[t, j] = (beta[t + 1] * B[:, V[t + 1]]).dot(A[j, :])

    return beta


beta = backward(V, A, B)
print(beta)
