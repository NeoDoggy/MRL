import numpy as np
from scipy.io import loadmat

def Segment(xy):
    x = xy[:, 0]
    y = xy[:, 1]

    threshold = 0.1

    S_i = 1
    S_n = 1

    n0ind = np.nonzero(np.logical_or(x != 0, y != 0))[0]
    n_0 = len(n0ind)

    Seg = np.zeros((len(x), len(x)), dtype=int)
    Seg[0, 0] = n0ind[0]

    for i in range(1, n_0):
        if np.sqrt((x[n0ind[i]] - x[n0ind[i - 1]])**2 + (y[n0ind[i]] - y[n0ind[i - 1]])**2) < threshold:
            Seg[S_i, S_n - 1] = n0ind[i]
            S_i += 1
        else:
            S_n += 1
            S_i = 1
            Seg[S_i - 1, S_n - 1] = n0ind[i]

    Seg = Seg[:np.max(np.nonzero(Seg)) + 1, :S_n]

    Si_n = np.sum(Seg != 0, axis=0)
    Si_n[0]+=1
    return Seg, Si_n, S_n