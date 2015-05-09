#encoding: utf-8
__author__ = 'Ján Krivý'

import py4j
from py4j.java_gateway import JavaGateway
import uuid


a = uuid.getnode()
b = uuid.uuid4()
print b
print a

#gateway = JavaGateway()
#java_object = gateway.jvm.default.TimeStampFactory()  # invoke constructor
#other_object = java_object.doThat()
#other_object.doThis(1,'abc')


#from py4j.java_gateway import JavaGateway
#from py4j.java_gateway import java_import
#gateway = JavaGateway()
#jList1 = gateway.jvm.java.util.ArrayList()
#java_import(gateway.jvm,'java.util.*')
#jList2 = gateway.jvm.ArrayList()
#gateway.jvm.java.lang.String("a")
