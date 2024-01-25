import qi
import sys

class MyFooService:
  def __init__(self, *args, **kwargs):
    #define a signal 'onBang'
    self.onBang = qi.Signal()

  #define a bang method that will trigger the onBang signal
  def bang (self):
    #trigger the signal with 42 as value
    self.onBang(42)
    print ("Servicio funcionando")

#create an application
app = qi.Application()
app.start()

#create an instance of MyFooService
myfoo = MyFooService()

s = app.session
#let's register our service with the name "foo"
id = s.registerService("foo", myfoo)

#let the application run
app.run()


