import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) #defines the publisher's topic, message type and ammount of queued messages
    rospy.Subscriber('chatter', String, callback) #defines the subscriber's topic, message type and calls the function "callback" which displays the data received
    rospy.init_node('talker', anonymous=True) #initialize the node (each python script has only one node, so we don't have to make one for the subscriber (they use the same node))
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	for x in range(10):
		y = x+1 #as x begins in 0 and goes to 9 and we want it from 1 to 10, y=x+1
		talk_str = str(y)
        	pub.publish(talk_str)
        	rate.sleep()


def callback(data): #gets the data that was sent
    x = int(data.data) #since we want to see the rest of the division of data by 2, we need to convert it from a string to an int otherwise the operation wouldn't work
    if x%2 == 0:
        print(x)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass #this allows the code to be stopped when we press Ctrl-C in the terminal

