from Ball_model import Ball_Detector # TODO Bayes filter
from Box_model import Box_Detector # TODO Bayes filter
from BallBox_Model import BallBox_Detector # TODO Bayes filter
from test import test
import os


# ball_data = ['ball2','ball1']
# model1 = Ball_Detector()
# model1.fit(filenames = ball_data)
# model1.save('./model/ball_model.joblib')
# model2 = Ball_Detector()
# model2.load('./model/ball_model.joblib')
# model2.predict(filenames = ['ball2','ball1'], draw=False)
# while True:
#     try:
#         if not os.stat("/home/hypharos/catkin_ws/laser_data.dat").st_size==0:
#             circle = model2.realtime_predict(file_path='/home/hypharos/catkin_ws/laser_data.dat')
#             if circle ==-2:
#                 continue
#             elif circle == -1:
#                 f = open("ball.txt", "w")
#                 f.write("-1")
#                 f.close()
#             else:
#                 f = open("ball.txt", "w")
#                 f.write(f"{circle['x']} {circle['y']}")
#                 f.close()

#             if circle == -1 or circle ==-2:
#                 print("No ball detected")
#                 # updated_state = filter.update(0)
#                 updated_state = model2.Bayes_Filter_run(0)
#             else:
#                 print('Ball detected')
#                 # updated_state = filter.update(1)
#                 updated_state = model2.Bayes_Filter_run(1)
#             print(f"Updated state probabilities: ball = {updated_state[0]:.4f}, no_ball = {updated_state[1]:.4f}")
#     except EOFError:
#         break
#     except:
#         continue

box_data = ['box1','box2']
model3 = Box_Detector()
model3.fit(filenames = box_data)
model3.save('./model/box_model.joblib')

model4 = Box_Detector()
model4.load('./model/box_model.joblib')
# model4.predict(filenames = ['box1','box2'], draw=False)
while True:
    try:
        if not os.stat("/home/hypharos/catkin_ws/laser_data.dat").st_size==0:
            rect = model4.realtime_predict(file_path='/home/hypharos/catkin_ws/laser_data.dat')
            print(rect)
            if rect ==-2:
                continue
            elif rect == -1:
                f = open("box.txt", "w")
                f.write("-1")
                f.close()
            else:
                f = open("box.txt", "w")
                f.write(f"{rect['x']} {rect['y']}")
                f.close()

            if rect == -1 or rect ==-2:
                print("No box detected")
                # updated_state = filter.update(0)
                updated_state = model4.Bayes_Filter_run(0)
            else:
                print('Box detected')
                # updated_state = filter.update(1)
                updated_state = model4.Bayes_Filter_run(1)
            print(f"Updated state probabilities: Box = {updated_state[0]:.4f}, no_box = {updated_state[1]:.4f}")
    except EOFError:
        break
    except:
        continue


# boxball_data = ['box1','ball1','box2','ball2']
# model5 = BallBox_Detector()
# model5.fit(filenames = boxball_data)
# model5.save('./model/ballbox_model.joblib')

# model6 = BallBox_Detector()
# model6.load('./model/ballbox_model.joblib')
# model6.predict(filenames = ['box2','ball2'], draw=True)
# circle_center, box_center = model6.realtime_predict(file_path='./dataset/box1.dat')
# print(circle_center)
# print(box_center)


# model = test()
# model.load('./model/ball_model.joblib')
# model.predict(filenames = ['ball1','ball2'], draw=False)

# data = pd.read_csv('./dataset/ball1.dat', header=None, names=['Angle', 'Distance', 'Counter'])
# grouped_data = [group[['Angle', 'Distance']].values for _, group in data.groupby('Counter')]
# data = np.array(grouped_data).transpose(1, 2, 0)
# model.Bayes_Filter_initial()
# for i in range(len(data)):
#     circle = model.realtime_predict(data=data[:,:,i])
#     if circle == -1:
#         print("No ball detected")
#         # updated_state = filter.update(0)
#         updated_state = model.Bayes_Filter_run(0)
#     else:
#         print('Ball detected')
#         # updated_state = filter.update(1)
#         updated_state = model.Bayes_Filter_run(1)
#     print(f"Updated state probabilities: ball = {updated_state[0]:.4f}, no_ball = {updated_state[1]:.4f}")
#     print()