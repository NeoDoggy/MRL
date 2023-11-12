# import pandas as pd

# file_path = './ball1.dat' 

# data = pd.read_csv(file_path, header=None, names=['Angle', 'Distance', 'Counter'])

# # print(data.head())

from scipy.io import loadmat
data = loadmat('./dataset/box1.mat')['box1']
print(data[:,:,1])

# import pandas as pd

# file_path = './box2.dat'
# data = pd.read_csv(file_path, header=None, names=['Angle', 'Distance', 'Counter'])

# counter_data_count = data.groupby('Counter').size()

# print(counter_data_count.head(30)) 

# Re-import the necessary libraries
import pandas as pd
import numpy as np

# Re-import the necessary libraries
import pandas as pd
import numpy as np

file_path = './dataset/box1.dat'
data = pd.read_csv(file_path, header=None, names=['Angle', 'Distance', 'Counter'])

grouped_data = [group[['Angle', 'Distance']].values for _, group in data.groupby('Counter')]
reshaped_data = np.array(grouped_data)

reshaped_data = reshaped_data.transpose(1, 2, 0)

print(reshaped_data.shape)
print(reshaped_data[:,:,10])