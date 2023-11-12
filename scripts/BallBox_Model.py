import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from Segment import Segment 
from Label import Label_box1, Label_box2, Label_ball1, Label_ball2
from joblib import dump, load
from data_processing import data_processing
import pandas as pd
from math import sqrt, atan2


class BallBox_Detector():

    def __init__(self):
        
        # self.model = AdaBoostClassifier(n_estimators=50, random_state=42)
        self.model = GradientBoostingClassifier(n_estimators=50, random_state=42)
        self.label = {'box1': Label_box1, 'box2': Label_box2, 'ball1': Label_ball1, 'ball2': Label_ball2}

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
                    if 'box' in filename and PN[i]==1: Y_train.extend([1] * n)
                    elif 'ball' in filename and PN[i]==1: Y_train.extend([2] * n)
                    else: Y_train.extend([0] * n)

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

                    if 'box' in filename and PN[i]==1:
                        Y_test.append(1)
                        # print(f'  Segment {i+1}: {1}')
                    elif 'ball' in filename and PN[i]==1:
                        Y_test.append(2)
                        # print(f'  Segment {i+1}: {2}')
                    else:
                        Y_test.append(0)
                        # print(f'  Segment {i+1}: {0}')
                    Y_pred_all.extend(Y_pred)
                    
                    # print(f'  Segment {i+1}: {Y_pred}')

                    
                    if draw:
                        color = 'royalblue' if Y_pred == 0 else ('salmon' if Y_pred == 1 else 'yellowgreen')
                        plt.plot(segment_data[:, 0], segment_data[:, 1], 'o', color=color, markersize=3)
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
    def realtime_predict(self,file_path):
        
        data = pd.read_csv(file_path, header=None, names=['Angle', 'Distance', 'Counter'])
        grouped_data = [group[['Angle', 'Distance']].values for _, group in data.groupby('Counter')]
        data = np.array(grouped_data).transpose(1, 2, 0)

        coordinates = []
        Seg, Si_n, S_n = Segment(data[:,:,0])
        for i in range(S_n):
            segment_data = data[Seg[:Si_n[i], i], :, 0]
            features,n = data_processing(segment_data)
            Y_pred = self.model.predict(features.reshape(1, -1))
            if Y_pred == 2: #ball 
                coordinates.append(('ball',segment_data))
            elif Y_pred == 1: #box
                coordinates.append(('box',segment_data))

        if coordinates == []: return -1        
        
        circle_centers = []
        rect_centers = []
        for label,coordinate in coordinates:
            if circle_centers != [] and rect_centers != []:
                break
            if label == 'ball' and circle_centers == []:
                coordinate = np.array(coordinate)
                squared_distances = np.sum(coordinate**2, axis=1)
                std_dev_center = np.mean(squared_distances)
                closest_indices = np.argsort(abs(squared_distances - std_dev_center))[:3]
                closest_points = coordinate[closest_indices]
                circle_center = self.calculate_circle(*closest_points)
                if circle_center is not False: #WTF is this? is not False?
                    circle_centers.append(circle_center)
            if label == 'box' and rect_centers == []:
                average_point = np.mean(coordinate, axis=0)
                rect_centers.append(average_point)
        if circle_centers == []: ball_center = -1    
        else:
            ball_center = {
                'x':circle_centers[0][0],
                'y':circle_centers[0][1],
                'z':0,
                'r':sqrt(circle_centers[0][0]**2+circle_centers[0][1]**2),
                'degree': atan2(circle_centers[0][0],circle_centers[0][1]),
            }
        if rect_centers == []: box_center = -1
        else:
            box_center = { 
                'x':rect_centers[0][0],
                'y':rect_centers[0][1],
                'z':0,
                'r':sqrt(rect_centers[0][0]**2+rect_centers[0][1]**2),
                'degree': atan2(rect_centers[0][0],rect_centers[0][1]),
            }
        return ball_center, box_center

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