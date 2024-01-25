#!/usr/bin/env python

import rospy
from paquete_servicio.srv import my_srv

#Creamos el nodo
rospy.init_node('my_client',anonymous=True)

#Esperar al servicio con nombre 'my_service'
rospy.wait_for_service('my_service')

cli = rospy.ServiceProxy('my_service',my_srv)

print('EL cliente está listo')

if __name__=='__main__':
    try:
        a = int(input('Introduzca un entero: '))
        b = int(input('Introduzca otro entero: '))
        resp = cli(a,b)
        print('El resutado del servicio es: ',resp.c)
    except rospy.ROSInterruptException:
        pass
