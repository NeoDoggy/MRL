import numpy as np

def Label_ball1(t, num_segments):
    labels = -np.ones(num_segments, dtype=int)
    index_mapping = {
        1: 8, 2: 10, 3: 6, 4: 2, 5: 55, 6: 51, 7: 53, 8: 46, 9: 32, 10: 31,
        11: 32, 12: 48, 13: 51, 14: 51, 15: 54, 16: 1, 17: 3, 18: 6, 19: 19, 20: 23,
        21: 18, 22: 17, 23: 24, 24: 44, 25: 50, 26: 45, 27: 48, 28: 48, 29: 48, 30: 1,
        31: 4, 32: 11, 33: 7, 34: 5, 35: 15, 36: 13, 37: 13, 38: 22, 39: 16, 40: 10
    }
    
    if t in index_mapping:
        index_to_label = index_mapping[t] - 1 # -1 because of 0-indexing
        if index_to_label < num_segments:
            labels[index_to_label] = 1

    return labels

def Label_ball2(t, num_segments):
    labels = -np.ones(num_segments, dtype=int)
    index_mapping = {
        1: 0, 2: 0, 3: 44, 4: 39, 5: 43, 6: 44, 7: 39, 8: 30, 9: 34, 10: 45,
        11: 46, 12: 49, 13: 45, 14: 1, 15: 11, 16: 10, 17: 19, 18: 39, 19: 51, 20: 46,
        21: 47, 22: 4, 23: 8, 24: 7, 25: 6, 26: 47, 27: 43, 28: 40, 29: 21, 30: 17,
        31: 25, 32: 38, 33: 47, 34: 5, 35: 8, 36: 8, 37: 14, 38: 20, 39: 25, 40: 23
    }
    if t in index_mapping:
        index_to_label = index_mapping[t]
        if index_to_label < num_segments:
            labels[index_to_label] = 1

    return labels


def Label_box1(t, num_segments):
    labels = -np.ones(num_segments, dtype=int)
    index_mapping = {
        1: 36, 2: 33, 3: 34, 4: 34, 5: 33, 6: 35, 7: 33, 8: 38, 9: 22, 10: 17,
        11: 13, 12: 8, 13: 7, 14: 7, 15: 4, 16: 9, 17: 13, 18: 21, 19: 32, 20: 38,
        21: 39, 22: 38, 23: 43, 24: 46, 25: 40, 26: 48, 27: 43, 28: 47, 29: 49, 30: 51,
        31: 49, 32: 54, 33: 48, 34: 45, 35: 44, 36: 45, 37: 44, 38: 42, 39: 36, 40: 35
    }
    

    if t in index_mapping:
        index_to_label = index_mapping[t] - 1 
        if index_to_label < num_segments:
            labels[index_to_label] = 1
    
    return labels

def Label_box2(t, num_segments):
    labels = -np.ones(num_segments, dtype=int)
    index_mapping = {
        1: 23, 2: 21, 3: 25, 4: 26, 5: 20, 6: 15, 7: 12, 8: 12, 9: 8, 10: 6,
        11: 5, 12: 4, 13: 6, 14: 3, 15: 3, 16: 2, 17: 51, 18: 48, 19: 50, 20: 49,
        21: 48, 22: 50, 23: 49, 24: 39, 25: 37, 26: 32, 27: 41, 28: 44, 29: 56, 30: 48,
        31: 1, 32: 2, 33: 5, 34: 8, 35: 8, 36: 8, 37: 11, 38: 10, 39: 12, 40: 9
    }

    if t in index_mapping:
        index_to_label = index_mapping[t] - 1 
        if index_to_label < num_segments:
            labels[index_to_label] = 1
    
    return labels