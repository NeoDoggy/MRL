#!/usr/bin/env python
import rospy
import time
from visualization_msgs.msg import Marker
import math
from tf.transformations import quaternion_from_euler

def toPOL(x,y):
    return math.atan2(y,x)

def main():
    rospy.init_node("box", anonymous=True)
    rate = rospy.Rate(30)
    pub = rospy.Publisher("visualization_marker", Marker, queue_size=1)
    shape = Marker.CUBE
    nowx=0
    last=[]
    while not rospy.is_shutdown():
        data = open("./box.txt", "r")
        datas=data.readlines()
        if datas==[]:
            print(last)
            datas=last
        last=datas
        datas=datas[0].split(' ')
        marker = Marker()
        marker.header.frame_id = "base_scan"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "box"
        marker.id = 1
        marker.type = shape
        marker.action = Marker.ADD
        marker.pose.position.x = float(datas[0])
        marker.pose.position.y = float(datas[1])
        marker.pose.position.z = float(datas[2])
        quat=quaternion_from_euler(0,0,toPOL(float(datas[0]),float(datas[1])))
        marker.pose.orientation.x = quat[0]
        marker.pose.orientation.y = quat[1]
        marker.pose.orientation.z = quat[2]
        marker.pose.orientation.w = quat[3]
        marker.scale.x = 0.1
        marker.scale.y = 0.3
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

        # if nowx<360:
        #     nowx=nowx+1
        # else:
        #     nowx=0
        
        rate.sleep()  # 指定频率刷新

if __name__== "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
