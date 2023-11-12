from Box_model import Box_Detector
import os
# box_data = ['box1','box2']
# model3 = Box_Detector()
# model3.fit(filenames = box_data)
# model3.save('./model/box_model.joblib')
# print('aaa')
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