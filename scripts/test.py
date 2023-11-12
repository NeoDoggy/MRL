import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from Segment import Segment 
from Label import Label_ball1, Label_ball2
from joblib import dump, load
from data_processing import data_processing
import pandas as pd
from math import sqrt, atan2

class test():

    def __init__(self):
        
        self.model = AdaBoostClassifier(n_estimators=100, random_state=42)
        self.label = {'ball1': Label_ball1, 'ball2': Label_ball2}
        self.T = np.array([[0.93, 0.07], [0.25, 0.75]])
        self.Z = np.array([[0.3, 0.7], [0.8, 0.2]])
        self.state = np.array([0.5, 0.5]) 


    def fit(self, filenames):
        X_train, Y_train = [], []
        for filename in filenames:
            
            data = loadmat('./dataset/'+filename+'.mat')[filename]
            data_shape = data.shape
            duration = data_shape[2]

            for sec in range(duration):
                Seg, Si_n, S_n = Segment(data[:, :, sec])
                PN = self.label[filename](sec+1, S_n)

                for i in range(S_n):
                    segment_data = data[Seg[:Si_n[i], i], :, sec]
                    features,n = data_processing(segment_data)
                    X_train.append(np.tile(features, (n, 1)))
                    Y_train.extend([PN[i]] * n)

        X_train = np.vstack(X_train)
        Y_train = np.array(Y_train)
        self.model.fit(X_train, Y_train)

    def predict(self, filenames, draw=True):

        Y_test, Y_pred_all = [], []
        
        for filename in filenames:

            data = loadmat('./dataset/'+filename+'.mat')[filename]
            data_shape = data.shape
            duration = data_shape[2]

            for sec in range(duration):
                if draw:
                    plt.clf()
                    plt.title(f'{filename} {sec+1} sec.')
                    plt.xlim(-4, 4)
                    plt.ylim(-4, 4)
                
                Seg, Si_n, S_n = Segment(data[:, :, sec])
                PN = self.label[filename](sec+1, S_n)
                print(f' There are {S_n} segments at {sec+1} sec')

                if draw: plt.plot(data[:, 0, sec], data[:, 1, sec], '.')
                
                for i in range(S_n):
                    segment_data = data[Seg[:Si_n[i], i], :, sec]
                    features,n = data_processing(segment_data)
                    Y_pred = self.model.predict(features.reshape(1, -1))

                    Y_test.append(PN[i])
                    Y_pred_all.extend(Y_pred)
                    
                    if draw and Y_pred == 1: 
                        plt.plot(segment_data[:, 0], segment_data[:, 1], color='yellowgreen', marker='o', markeredgecolor='yellowgreen', markersize=3)
                if draw: plt.pause(0.1)
        Y_test = np.array(Y_test)
        Y_pred_all = np.array(Y_pred_all)
        confusion_table = confusion_matrix(Y_test, Y_pred_all)
        acc = accuracy_score(Y_test, Y_pred_all)
        print('Confusion table:')
        print(confusion_table)
        print(f'Accuracy: {acc*100:.2f}%')

    def save(self, model_path):
        dump(self.model, model_path)
        
    def load(self, model_path):
        self.model = load(model_path)

    def realtime_predict(self,data):

        coordinates = []
        Seg, Si_n, S_n = Segment(data[:,:])
        for i in range(S_n):
            segment_data = data[Seg[:Si_n[i], i], :]
            features,n = data_processing(segment_data)
            Y_pred = self.model.predict(features.reshape(1, -1))
            if Y_pred == 1: coordinates.append(segment_data)
        if coordinates == []: return -1        
        
        circle_centers = []
        for coordinate in coordinates:
            coordinate = np.array(coordinate)

            squared_distances = np.sum(coordinate**2, axis=1)
            std_dev_center = np.mean(squared_distances)
            closest_indices = np.argsort(abs(squared_distances - std_dev_center))[:3]
            closest_points = coordinate[closest_indices]
            circle_center = self.calculate_circle(*closest_points)
            if circle_center is not False: #WTF is this? is not False?
                circle_centers.append(circle_center)
                break
        center = {
            'x':circle_centers[0][0],
            'y':circle_centers[0][1],
            'z':0,
            'r':sqrt(circle_centers[0][0]**2+circle_centers[0][1]**2),
            'degree': atan2(circle_centers[0][0],circle_centers[0][1]),
        }

        return center

    def calculate_circle(self,p1, p2, p3):
        A = np.array([
            [2 * (p2[0] - p1[0]), 2 * (p2[1] - p1[1])],
            [2 * (p3[0] - p2[0]), 2 * (p3[1] - p2[1])]
        ])
        B = np.array([
            [p2[0]**2 - p1[0]**2 + p2[1]**2 - p1[1]**2],
            [p3[0]**2 - p2[0]**2 + p3[1]**2 - p2[1]**2]
        ])
        try:
            center = np.linalg.solve(A, B)
            return center.flatten()
        except np.linalg.LinAlgError:
            return False
    
    def Bayes_Filter_initial(self):
        self.state = np.array([0.5, 0.5])
    
    def Bayes_Filter_run(self,measurement):
        predicted_state = np.dot(self.T.T, self.state)
        self.state = predicted_state * self.Z[:, measurement]
        self.state /= np.sum(self.state)
        return self.state