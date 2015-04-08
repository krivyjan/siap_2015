#encoding: utf-8
__author__ = 'Ján Krivý'

#import execjs
import win32com.client

#from test_data import Data
from test_data2 import Data
data = Data()
oXMLPlugin = win32com.client.Dispatch('DSig.XmlPluginAtl')
oXML = win32com.client.Dispatch("DSig.XadesSigAtl")


#print oXMLPlugin
#print oXML
#print data.xml[830:839]
#print data.xml.decode(encoding='UTF-8')
#('objectId', 'Daòové priznanie', xml, xsd, '', xsdURI, xsl, xslURI);
obj = oXMLPlugin.CreateObject('objectId','Danove priznanie',data.xml.decode(encoding='UTF-8'),data.schema.decode(encoding='UTF-8'),'','http://dis-major/dppo.xsd',data.transformation.decode(encoding='UTF-8'),'http://dis-major/dppo.xslt');
#a = execjs.eval("var oXMLPlugin = new ActiveXObject('DSig.XmlPluginAtl');")
addObj = oXML.AddObject(obj)
# print addObj

res = oXML.Sign('signatureId', 'sha256', 'urn:oid:1.3.158.36061701.1.2.1')
#print res
#print '---------------------------------------'
aaa = oXML.SignedXMLWithEnvelope
#print type(aaa)
text =  aaa.encode('utf-8','ignore')
file = open("Output.xml", "w")
file.write(text)
file.close()
'''
ctx = execjs.compile("""
     function add(x, y) {
         var oXMLPlugin = new ActiveXObject('C:\Ditec\DSigXades\Ditec.Zep.DSigXades.XmlPluginAtl.dll')
         //var oXMLPlugin = new ActiveXObject('DSig.XmlPluginAl');
         var daco = new Array();
         return x + y;

     }
 """)

#Ditec.Zep.DSigXades.XmlPluginAtl.dll
#C:\Ditec\DSigXades
print ctx.call("add", 1, 2)
'''
#jscript = execjs.get("var oXMLPlugin = new ActiveXObject('DSig.XmlPluginAtl');")
#print jscript.eval("1+1")


