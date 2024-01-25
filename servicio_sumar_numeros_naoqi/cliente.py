import qi
import sys

def onBangCb(i):
  print ("La suma de los números es: ", + i)

app = qi.Application()
app.start()
s = app.session
foo = s.service("foo")

#register a callback on 'onBang'
foo.onBang.connect(onBangCb)
#call bang
foo.bang()
