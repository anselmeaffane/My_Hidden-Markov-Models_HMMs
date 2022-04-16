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


def forward(V, A, B, initial_distribution):
    #We create an empty Alpha array 10 (lines) x 4 (cols)
    alpha = np.zeros((V.shape[0], A.shape[0]))
    alpha[0, :] = initial_distribution * B[:, V[0]]

    for t in range(1, V.shape[0]):
        for j in range(A.shape[0]):
            # Matrix Computation Steps
            #                  ((1x2) . (1x2))      *     (1)
            #                        (1)            *     (1)
            alpha[t, j] = alpha[t - 1].dot(A[:, j]) * B[j, V[t]]

    return alpha


alpha = forward(V, A, B, initial_distribution)
print(alpha)
