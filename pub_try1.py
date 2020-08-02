#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher' )
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = JointState()
        hello_str.header = Header()
        hello_str.header.stamp = rospy.Time.now()
        hello_str.name = ['joint1', 'joint2', 'joint3']
        hello_str.position = [0.8 , 0.8 , 0.54]
        hello_str.velocity = []
        hello_str.effort = []
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
