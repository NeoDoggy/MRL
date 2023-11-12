#!/usr/bin/env python

import rospy
import time
from visualization_msgs.msg import Marker 

def main():
    rospy.init_node("ball", anonymous=True)
    rate = rospy.Rate(30)
    pub = rospy.Publisher("visualization_marker", Marker, queue_size=1)
    shape = Marker.SPHERE
    last=[]
    # nowy=0
    while not rospy.is_shutdown():
        data = open("./ball.txt", "r")
        datas=data.readlines()
        if datas==[]:
            print(last)
            datas=last
        last=datas
        datas=datas[0].split(' ')
        marker = Marker()
        marker.header.frame_id = "base_scan"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "ball"
        marker.id = 0
        marker.type = shape
        marker.action = Marker.ADD
        marker.pose.position.x = float(datas[0])
        marker.pose.position.y = float(datas[1])
        marker.pose.position.z = float(datas[2])
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 1.0
        marker.color.a = 1.0
        marker.lifetime = rospy.Duration()
        while pub.get_num_connections() < 1: 
            if rospy.is_shutdown():
                exit(1)
            rospy.loginfo("Please create a subscriber to the marker!")
            time.sleep(1)
        pub.publish(marker)

        # if nowy<1:
        #     nowy=nowy+0.1
        # else:
        #     nowy=0
        data.close
        rate.sleep()

if __name__== "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
