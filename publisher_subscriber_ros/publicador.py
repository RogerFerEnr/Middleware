#!/usr/bin/env python

import rospy
from std_msgs.msg import String

#Creamos el nodo de nombre mi_publicador
rospy.init_node('mi_publicador',anonymous=False)

#Definimos la transmision de datos (nos referimos al nombre del tópico)
# 'mi_topico' se refiere al nombre del topico en el que se va a publicar
#String es el tipo de dato que se publica
#queue_size indica el tamaño de buffer de los mensajes (en nuestro caso 10 mensajes)

pub = rospy.Publisher('mi_topico', String, queue_size = 10)

#Definimos la frecuencia de publicacion 2 Hz 
rate = rospy.Rate(2)

if __name__=='__main__':
	try:
		while not rospy.is_shutdown():
			mensaje = 'Hola'
			pub.publish(mensaje)
			rospy.loginfo(mensaje)
			rate.sleep()
	except rospy.ROSInterruptException:
		pass 
