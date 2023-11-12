#!/usr/bin/env python

import rospy
import time
from visualization_msgs.msg import Marker
from tf.transformations import quaternion_from_euler

def main():
    rospy.init_node("ball", anonymous=True)
    rate = rospy.Rate(60)
    pub = rospy.Publisher("/capy", Marker, queue_size=1)
    nowROL=0
    while not rospy.is_shutdown():
        marker = Marker()
        marker.header.frame_id = "base_scan"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "robo"
        marker.id = 0
        marker.type = 10
        marker.action = 0
        marker.mesh_resource="file:///home/hypharos/catkin_ws/src/display_my_ballz/capy/capybara_low_poly.stl"
        marker.mesh_use_embedded_materials = True
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.05
        quat=quaternion_from_euler(1.57,0,nowROL)
        marker.pose.orientation.x = quat[0]
        marker.pose.orientation.y = quat[1]
        marker.pose.orientation.z = quat[2]
        marker.pose.orientation.w = quat[3]
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.r = 1.0
        marker.color.g = 148/255
        marker.color.b = 112/255
        marker.color.a = 1.0

        marker.lifetime = rospy.Duration()

        while pub.get_num_connections() < 1: 
            if rospy.is_shutdown():
                exit(1)
            rospy.loginfo("Please create a subscriber to the marker!")
            time.sleep(1)
        pub.publish(marker)
 		
        # 每次发布的消息不同，从而让rviz绘制不同的marker
        # if shape == Marker.CUBE:
        #     shape = Marker.SPHERE
        # elif shape == Marker.SPHERE:
        #     shape = Marker.ARROW
        # elif shape == Marker.ARROW:
        #     shape = Marker.CYLINDER
        # elif shape == Marker.CYLINDER:
        #     shape = Marker.CUBE

        if nowROL<360:
            nowROL+=1
        else:
            nowROL=0
        rate.sleep()  # 指定频率刷新

if __name__== "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
