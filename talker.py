#!/usr/bin/env python


import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) #defines the publisher's topic, message type and ammount of queued messages
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	for x in range(10):
		y = x+1 #as x begins in 0 and goes to 9 and we want it from 1 to 			10, y=x+1
		talk_str = str(y)
        	rospy.loginfo(talk_str)
        	pub.publish(talk_str)
        	rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass #this allows the code to be stopped when we press Ctrl-C in the terminal
