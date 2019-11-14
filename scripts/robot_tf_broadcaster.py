#!/usr/bin/env python
#coding=utf-8

import rospy

import tf
import nav_msgs.msg


def handle_robot_pose(msg, robotname):
    br = tf.TransformBroadcaster() #将坐标变换广播出去
    #向/tf发布消息
                      #robot距离原点的坐标
    br.sendTransform((msg.pose.pose.position.x, msg.pose.pose.position.y, 0), #平移
                     (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w), #旋转  quaternion_from_euler:欧拉角变四元数
                     rospy.Time.now(), #打上时间戳
                     '/%s/odom' % robotname,  #发布 robotname 到 "map" 的平移和翻转   
                     "map")

if __name__ == '__main__':
    rospy.init_node('item')
    robotname = rospy.get_param('~robot')    #取参数服务器robot的值
    rospy.Subscriber('/%s/odom' % robotname, #要接收的topic名  /turtle1/pose或者/turtle2/pose
                     nav_msgs.msg.Odometry,  #接收的数据类型
                     handle_robot_pose,      #回调函数
                     robotname)              #回调函数参数
    rospy.spin() #保持节点运行，直到节点关闭
    
    
    