from Ball_model import Ball_Detector # TODO Bayes filter
import os

# ball_data = ['ball2','ball1']
# model1 = Ball_Detector()
# model1.fit(filenames = ball_data)
# model1.save('./model/ball_model.joblib')
model2 = Ball_Detector()
model2.load('./model/ball_model.joblib')
# model2.predict(filenames = ['ball2','ball1'], draw=False)
while True:
    try:
        if not os.stat("/home/hypharos/catkin_ws/laser_data.dat").st_size==0:
            circle = model2.realtime_predict(file_path='/home/hypharos/catkin_ws/laser_data.dat')
            if circle ==-2:
                continue
            elif circle == -1:
                f = open("ball.txt", "w")
                f.write("-1")
                f.close()
            else:
                f = open("ball.txt", "w")
                f.write(f"{circle['x']} {circle['y']}")
                f.close()

            if circle == -1 or circle ==-2:
                print("No ball detected")
                updated_state = model2.Bayes_Filter_run(0)
            else:
                print('Ball detected')
                updated_state = model2.Bayes_Filter_run(1)
            print(f"Updated state probabilities: ball = {updated_state[0]:.4f}, no_ball = {updated_state[1]:.4f}")
    except EOFError:
        break
    except:
        continue
