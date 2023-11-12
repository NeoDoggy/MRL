#!/usr/bin/env python

import rospy
import time  # 主要是调用了sleep函数
from visualization_msgs.msg import Marker  # 可以通过rosmsg show visualization_msgs/Marker查看marker的内容

def main():
    rospy.init_node("ball", anonymous=True)  # 创建node， 命名basic_shapes
    rate = rospy.Rate(5)  # 消息发布的刷新频率
    pub = rospy.Publisher("visualization_marker", Marker, queue_size=1)
    # pub定义了一个发布器， 名称visualization_marker, 注意这个topic的名称是固定的，因为rviz中对应marker的订阅器订阅的topic就是visualization_marker,消息类型Marker
    shape = Marker.SPHERE  # 形状参数，python直接通过类的属性默认值访问
    # nowy=0
    
    while not rospy.is_shutdown():  # 当node没被杀掉时，执行循环
        data = open("./ball.txt", "r")
        datas=data.readlines()
        datas=datas[0].split(' ')
        marker = Marker()  # 定义Marker类型的变量
        marker.header.frame_id = "base_scan"  # 设置header的frame——id和stamp属性值
        marker.header.stamp = rospy.Time.now()  # 这里应该是一个浮点值，对应cpp版本 ros::Time::now()
        # 下面两个量定义了该marker的命名空间和id， 通过这两个量能够确定marker的身份，如果身份相同，那么则刷新rviz中对应目标。后面我们会讲到marker是什么
        marker.ns = "ball"
        marker.id = 0
		
        marker.type = shape  # marker的类型
        marker.action = Marker.ADD # marker action

        # 初始化了marker的位置和初始的角度
        marker.pose.position.x = float(datas[0])
        marker.pose.position.y = float(datas[1])
        marker.pose.position.z = float(datas[2])
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 1.0
        # marker的尺寸大小，这里1.0对应于现实地图的1m
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        # marker的颜色定义， 注意透明度a的设置，为0就看不到了
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 1.0
        marker.color.a = 1.0

        marker.lifetime = rospy.Duration()

        while pub.get_num_connections() < 1: 
            # get_num_connections()是python版本查阅当前topic的订阅器数目， cpp版本对应函数：
            # marker_pub.getNumScribers()
            # 用来判断当前是否有订阅器，也就是说rviz是否打开，如果没有订阅器没必要发布消息。当然没有订阅器情况下发布消息也是没问题的。
            if rospy.is_shutdown():
                exit(1)
            rospy.loginfo("Please create a subscriber to the marker!")
            time.sleep(1)  # 休眠等待，不断查询有没有订阅器

        pub.publish(marker)  # 发布消息
 		
        # 每次发布的消息不同，从而让rviz绘制不同的marker
        # if shape == Marker.CUBE:
        #     shape = Marker.SPHERE
        # elif shape == Marker.SPHERE:
        #     shape = Marker.ARROW
        # elif shape == Marker.ARROW:
        #     shape = Marker.CYLINDER
        # elif shape == Marker.CYLINDER:
        #     shape = Marker.CUBE

        # if nowy<1:
        #     nowy=nowy+0.1
        # else:
        #     nowy=0
        data.close
        rate.sleep()  # 指定频率刷新

if __name__== "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
