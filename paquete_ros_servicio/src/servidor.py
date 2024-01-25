#!/usr/bin/env python

import rospy
from paquete_servicio.srv import my_srv, my_srvResponse

def callback(req):
    return my_srvResponse(req.a+req.b)

#Creamos el nodo
rospy.init_node('my_server',anonymous=True)

#Se define el streaming (el servicio)
rospy.Service('my_service',my_srv,callback)

if __name__=='__main__':
    try:
        print('Se ha iniciado el servicio')
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

