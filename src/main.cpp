#include <stdio.h>
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sensor_msgs/LaserScan.h"
#include <fstream>
#include <math.h>
#define RAD2DEG(x) ((x)*180./M_PI)
FILE* pFile2 ;

std::ofstream data("laser_data.dat");
void scanCallback(const sensor_msgs::LaserScan::ConstPtr&);

int counter=0;
//int hehe=0;

void callback(const ros::TimerEvent&){
  counter++;
  ROS_INFO("sample file called : %d\t times",counter);
  if(counter==1){
    //data.flush();
    data.close();
    counter=0;
    data.open("laser_data.dat");
  }
}

void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan){
  for(int i=0;i<720;i++){
    float degree=scan->angle_min+scan->angle_increment*i;
    data<<scan->ranges[i]*cos(degree)<<", "<<scan->ranges[i]*sin(degree)<<", "<<counter<<std::endl;
    //if(scan->ranges[i]>0.000){
      //fprintf(pFile2,"%f, %f, %d\n", degree,scan->ranges[i], counter) ;
    //}
  }
}


int main(int argc, char **argv){
  //pFile2 = fopen("laser_data.dat","w");
  ros::init(argc,argv,"listener");

  ros::NodeHandle n;

  ros::Timer timer1 = n.createTimer(ros::Duration(0.1),callback);
  
  ros::Subscriber sub=n.subscribe<sensor_msgs::LaserScan>("/scan",1000,scanCallback);

  ros::spin();


  return 0;
}
