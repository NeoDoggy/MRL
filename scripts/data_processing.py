import numpy as np
from scipy.linalg import pinv

def data_processing(segment_data):
    segment_data = segment_data.reshape(-1, 2)

    n = segment_data.shape[0]

    mean_x = np.mean(segment_data[:, 0])
    mean_y = np.mean(segment_data[:, 1])
    distances = np.sqrt((segment_data[:, 0] - mean_x)**2 + (segment_data[:, 1] - mean_y)**2)
    std_deviation = np.std(distances)

    width = np.max(segment_data) - np.min(segment_data)
    
    A = np.column_stack((-2*segment_data[:, 0], -2*segment_data[:, 1], np.ones(n)))
    b = -(segment_data[:, 0]**2 + segment_data[:, 1]**2)
    x_prime = pinv(A.T @ A) @ A.T @ b
    xc, yc = x_prime[0], x_prime[1]
    rc = np.sqrt(abs(xc**2 + yc**2 + x_prime[2]))
    distances_to_center = np.sqrt((segment_data[:, 0] - xc)**2 + (segment_data[:, 1] - yc)**2)
    sc = np.sum(abs(rc - distances_to_center))
    
    features = np.array([n, std_deviation, width, sc, rc])
    return features, n