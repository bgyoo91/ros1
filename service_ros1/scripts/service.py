import rospy
import sys
from test import *
from test1.srv import *

rospy.init_node('test2')
rospy.wait_for_service('service')
get_pos = rospy.ServiceProxy('service', test)

while not rospy.is_shutdown():
    try:
        ret = get_pos(True)
        # print ret.x, ", ", ret.y, ", ", ret.pos.z, ", ", ret.pos.d
    except rospy.ServiceException as exc:
        print str(exc)

