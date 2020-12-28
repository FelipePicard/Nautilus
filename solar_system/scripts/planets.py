#!/usr/bin/python

import rospy
import tf
import tf2_ros
import geometry_msgs.msg
import math
rospy.init_node("node", anonymous=True)
rate = rospy.Rate(10)


def transform(name, orbit): 



    theta = (2*(math.pi)*(rospy.Time.now().to_sec()))/60*orbit

    broadcaster = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "Sun"
    t.child_frame_id = name

    t.transform.translation.x = orbit * math.sin(theta)
    t.transform.translation.y = orbit * math.cos(theta)
    t.transform.translation.z = 0

    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    t.transform.rotation.w = 1

    broadcaster.sendTransform(t)

while not rospy.is_shutdown():
    planet = rospy.get_param("planets")
    for i in range(len(planet)):
        name = planet[i]["name"]
        orbit = planet[i]["orbitRadius"]
        print(orbit)
        print(name)
        transform(name, orbit)
    rate.sleep()
rospy.spin()