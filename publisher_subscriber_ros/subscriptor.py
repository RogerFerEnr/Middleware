#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(mensaje)
	rospy.loginfo(mensaje.data)

#Damos de alta el nodo

rospy.init_node('mi_subscriptor')

#Definimos la transmisión de datos
rospy.Subscriber("mi_topico", String, callback)

if __name__=='__main__':
	try:
		#Estamos a la espera (el nodo no hace nada)
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
	
