import os
while True:
    if not os.stat("/home/hypharos/catkin_ws/laser_data.dat").st_size==0:
        os.system("cp /home/hypharos/catkin_ws/laser_data.dat /home/hypharos/catkin_ws/src/display_my_ballz/scripts")