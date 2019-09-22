from test1.srv import *
import rospy

def send_pos(req):
    resp = testResponse()
    print test
    if req == True:
        resp.x = 1.0
        resp.y = 1.0
        resp.z = 1.0
        resp.d = 1.0
        print resp.x
        return resp
    else:
        resp.x = 0.0
        resp.y = 1.0
        resp.z = 1.0
        resp.d = 0.0
        print resp.y
        return resp

def send_pos_server():
    rospy.init_node('test1')
    s = rospy.Service('service', test, send_pos)
    rospy.spin()
