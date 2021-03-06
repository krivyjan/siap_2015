﻿#coding: utf-8
from PyQt4 import QtCore, QtGui
from data.registracia import application
from data.skolenie import courses,course
import lxml.etree as ET
from parsers.xmlParser import XmlParser
from lxml import etree
import win32com.client
from xml.dom.minidom import parse, parseString
import httplib,urllib
import urllib2
from base64 import b64decode
from subprocess import check_output
import uuid


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s



class Riadok(QtGui.QWidget):
  def __init__( self, parent=None):
        super(Riadok, self).__init__(parent)
        self.label_nazov = QtGui.QLabel()
        self.label_nazov.setText(QtGui.QApplication.translate("Form", "  Nazov:", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_nazov = QtGui.QLineEdit()
        self.edit_nazov.setText('Skolenie')

        self.label_priorita = QtGui.QLabel()
        self.label_priorita.setText(QtGui.QApplication.translate("Form", "  Priorita:", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_priorita = QtGui.QLineEdit()
        self.edit_priorita.setText('1')

        self.label_termin = QtGui.QLabel()
        self.label_termin.setText(QtGui.QApplication.translate("Form", "  Termin:", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_termin = QtGui.QLineEdit()
        self.edit_termin.setText('20.10.2015')
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.label_nazov)
        layout.addWidget(self.edit_nazov)
        layout.addWidget(self.label_priorita)
        layout.addWidget(self.edit_priorita)
        layout.addWidget(self.label_termin)
        layout.addWidget(self.edit_termin)
        self.setLayout(layout)

class Ui_Form(object):
    def __init__(self):
        self.riadky= list()
        self.xml = None
        self.xml_string = None
        self.podpisane_xml = None
        self.xml_Parser = XmlParser(xsl_file='C:\\siap_2015\\transformation.xslt',xsd_file='C:\\siap_2015\\schema.xsd')

    def setupUi(self, Form):
        #main form
        Form.setObjectName(_fromUtf8("Form"))
        Form.setFixedSize(1426, 936)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Krivý & Šustek - SIVPAVS 2015", None, QtGui.QApplication.UnicodeUTF8))

        #font
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        
        #nazov formulara label
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 451, 31))
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Form", "Registrácia účastníka školenia", None, QtGui.QApplication.UnicodeUTF8))

        #frame - titul meno priezvysko
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 50, 701, 41))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)

        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(11, 11, 30, 16))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Titul:", None, QtGui.QApplication.UnicodeUTF8))

        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(220, 11, 46, 16))
        self.label_3.setText(QtGui.QApplication.translate("Form", "  Meno:", None, QtGui.QApplication.UnicodeUTF8))
        
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(445, 11, 72, 16))
        self.label_4.setText(QtGui.QApplication.translate("Form", "  Priezvisko:", None, QtGui.QApplication.UnicodeUTF8))

        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(47, 11, 167, 20))
        self.lineEdit.setText('Ing.')
        
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(272, 11, 167, 20))
        self.lineEdit_2.setText('Jozko')
        
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(523, 11, 167, 20))
        self.lineEdit_3.setText('Mrkvicka')
        
        #frame firma
        self.frame_6 = QtGui.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(10, 100, 701, 41))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        
        self.label_19 = QtGui.QLabel(self.frame_6)
        self.label_19.setGeometry(QtCore.QRect(11, 11, 41, 16))
        self.label_19.setText(QtGui.QApplication.translate("Form", "Firma:", None, QtGui.QApplication.UnicodeUTF8))
        
        self.label_20 = QtGui.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(220, 11, 71, 16))
        self.label_20.setText(QtGui.QApplication.translate("Form", "  Pobočka:", None, QtGui.QApplication.UnicodeUTF8))
        
        self.label_21 = QtGui.QLabel(self.frame_6)
        self.label_21.setGeometry(QtCore.QRect(445, 11, 72, 16))
        self.label_21.setText(QtGui.QApplication.translate("Form", "  Pozícia:", None, QtGui.QApplication.UnicodeUTF8))
        
        self.lineEdit_18 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_18.setGeometry(QtCore.QRect(60, 10, 161, 20))
        self.lineEdit_18.setText('Firma')
        
        self.lineEdit_19 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_19.setGeometry(QtCore.QRect(288, 11, 151, 20))
        self.lineEdit_19.setText('Pobocka')

        self.lineEdit_20 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_20.setGeometry(QtCore.QRect(509, 11, 181, 20))
        self.lineEdit_20.setText('Pozicia')

        #frame email,telefonne cislo
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 701, 41))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)

        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(11, 11, 41, 16))
        self.label_5.setText(QtGui.QApplication.translate("Form", "E-mail:", None, QtGui.QApplication.UnicodeUTF8))
        
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 98, 16))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Telefónne číslo:", None, QtGui.QApplication.UnicodeUTF8))
    
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(58, 11, 281, 22))
        self.lineEdit_4.setText('mail@mail.com')

        self.lineEdit_5 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(457, 10, 231, 22))
        self.lineEdit_5.setText('+421 911 111 111')

        #frame stat,obec psc
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 200, 701, 41))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)

        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(11, 11, 30, 16))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Štát:", None, QtGui.QApplication.UnicodeUTF8))
        
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(47, 11, 180, 20))
        self.lineEdit_6.setText('Stat')
        
        self.label_8 = QtGui.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(233, 11, 44, 16))
        self.label_8.setText(QtGui.QApplication.translate("Form", "  Obec:", None, QtGui.QApplication.UnicodeUTF8))
        
        
        self.lineEdit_7 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(283, 11, 179, 20))
        self.lineEdit_7.setText('Obec')
        
        self.label_9 = QtGui.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(468, 11, 36, 16))
        self.label_9.setText(QtGui.QApplication.translate("Form", "  PSČ:", None, QtGui.QApplication.UnicodeUTF8))
        
        self.lineEdit_8 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(510, 11, 180, 20))
        self.lineEdit_8.setText('111 11')
        
        # skolenia
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 701, 221))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Vybrané školenia", None, QtGui.QApplication.UnicodeUTF8))
        
        #scrollarea2
        self.scrollArea_2 = QtGui.QScrollArea(self.groupBox)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 18, 701, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))

        #main Layout pre skolenia
        self.mainLayout = QtGui.QVBoxLayout(self.scrollArea_2)
        self.mainLayout.setGeometry(QtCore.QRect(0, 0, 701, 700))
        # scroll area widget contents - layout
        self.scrollLayout = QtGui.QFormLayout()
        # scroll area widget contents
        self.scrollWidget = QtGui.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        self.scrollArea_skolenia = QtGui.QScrollArea()
        self.scrollArea_skolenia.setWidgetResizable(True)
        self.scrollArea_skolenia.setWidget(self.scrollWidget)
        self.mainLayout.addWidget(self.scrollArea_skolenia)

        #pridaj button
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 30, 80, 22))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Pridať", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.clicked.connect(self.addWidget)

        #chybovy vystup
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 480, 611, 441))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Chybový výstup:", None, QtGui.QApplication.UnicodeUTF8))

        self.scrollArea = QtGui.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 611, 441))
        self.scrollArea.setWidgetResizable(True)

        self.outError = QtGui.QTextEdit(self.scrollArea)
        self.outError.setReadOnly(True)
        #self.outPut.setLineWrapMode
        self.outError.setGeometry(QtCore.QRect(0, 0, 611, 2210))
        self.outError.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 119))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 500, 81, 22))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Validovať", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.clicked.connect(self.validate)

        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 530, 81, 22))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Zobraziť", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.clicked.connect(self.show)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(630, 560, 81, 22))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Vyčistiť", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.clicked.connect(self.clear)

        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 590, 81, 22))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Podpisat", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.clicked.connect(self.podpis)

        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 620, 81, 22))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "Peciatka", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.clicked.connect(self.peciatka)

        self.frame_out = QtGui.QFrame(Form)
        self.frame_out.setGeometry(QtCore.QRect(730, 10, 701, 810))
        self.frame_out.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_out.setFrameShadow(QtGui.QFrame.Raised)

        self.label_30 = QtGui.QLabel(self.frame_out)
        self.label_30.setGeometry(QtCore.QRect(10, 5, 360, 16))
        self.label_30.setText(QtGui.QApplication.translate("Form", "  Vystup:", None, QtGui.QApplication.UnicodeUTF8))

        self.outPut = QtGui.QTextEdit(self.frame_out)
        self.outPut.setReadOnly(True)
        #self.outPut.setLineWrapMode
        self.outPut.setGeometry(QtCore.QRect(0, 20, 685, 810))
        self.outPut.setLineWrapMode(QtGui.QTextEdit.NoWrap)

        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def addWidget(self):
        riadok = Riadok()
        self.riadky.append(riadok)
        self.scrollLayout.addRow(riadok)

 

    def validate(self):
        registracia = application(
                          titul = unicode(self.lineEdit.text()),
                          meno = unicode(self.lineEdit_2.text()),
                          priezvysko = unicode(self.lineEdit_3.text()),
                          firma = unicode(self.lineEdit_18.text()),
                          pobocka = unicode(self.lineEdit_19.text()),
                          pozicia = unicode(self.lineEdit_20.text()),
                          email = unicode(self.lineEdit_4.text()),
                          cislo = unicode(self.lineEdit_5.text()),
                          stat = unicode(self.lineEdit_6.text()),
                          obec = unicode(self.lineEdit_7.text()),
                          psc = unicode(self.lineEdit_8.text())
                        )
        skolenia = courses()

        for riadok in self.riadky:
            skolenie = course(
                nazov=unicode(riadok.edit_nazov.text()),
                priorita=riadok.edit_priorita.text(),
                termin=riadok.edit_termin.text())
            skolenia.skolenie.append(skolenie)

        registracia.skolenia.append(skolenia)
        string_xml = registracia.render(encoding="UTF-8")
        validation = self.xml_Parser.validate(string_xml)
        output_xml = registracia.render(encoding="UTF-8",pretty=True)
        self.outPut.clear()
        self.outPut.insertPlainText(output_xml.decode("utf-8"))
        self.xml = etree.fromstring(string_xml)
        if validation == True:
            self.xml_string = string_xml
            self.outError.insertPlainText('Validacia uspesna \n')
        else:
            self.outError.insertPlainText(str(validation) + '\n')


    def show(self):
        #print ("+ľšťščžčťž").decode("utf-8")
        #self.outError.insertHtml(('+ľš+ľšščťščžťýáíýáí').decode("utf-8"))
        if self.xml:
            transformation = self.xml_Parser.transform(self.xml)
            self.outPut.clear()
            self.outPut.insertPlainText(transformation.decode("utf-8"))
            #print transformation
        else:
            self.outError.insertPlainText("Nezvalidovane xml")




    def clear(self):
        for item in self.riadky:
            item.deleteLater()

        self.riadky = list()

        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()
        self.lineEdit_20.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()

        self.outPut.clear()
        self.xml=None

    def podpis(self):
        oXMLPlugin = win32com.client.Dispatch('DSig.XmlPluginAtl')
        oXML = win32com.client.Dispatch("DSig.XadesSigAtl")

        obj = oXMLPlugin.CreateObject('Id','Registracny formular',self.xml_string.decode(encoding='UTF-8'),self.xml_Parser.string_schema().decode(encoding='UTF-8'),'','http://dis-major/dppo.xsd',self.xml_Parser.string_transformation().decode(encoding='UTF-8'),'http://dis-major/dppo.xsd');
        #obj1 = oXMLPlugin.CreateObject('Id2','Registracny formular2',self.xml_string.decode(encoding='UTF-8'),self.xml_Parser.string_schema().decode(encoding='UTF-8'),'','http://dis-major/dppo.xsd',self.xml_Parser.string_transformation().decode(encoding='UTF-8'),'http://dis-major/dppo.xsd');

        if obj == None:
            self.outError.insertPlainText('Chyba pri vytvarani objektu oXMLPlugin \n')
            self.outError.insertPlainText(oXMLPlugin.ErrorMessage)
            return

        addObj = oXML.AddObject(obj)
        #addObj1 = oXML.AddObject(obj1)

        if addObj != 0:
            self.outError.insertPlainText('Chyba pri pridavani objektu do oXML \n')
            self.outError.insertPlainText(oXML.ErrorMessage)

        #if addObj1 != 0:
            #self.outError.insertPlainText('Chyba pri pridavani objektu do oXML \n')
            #self.outError.insertPlainText(oXML.ErrorMessage)


        res = oXML.Sign('signatureId', 'sha256', 'urn:oid:1.3.158.36061701.1.2.1')
        if res == 0:
            aaa = oXML.SignedXMLWithEnvelope

            self.outError.setPlainText(str(type(aaa)))
            text =  aaa.encode('utf-8','ignore')

            self.podpisane_xml = parseString(text)
            text =  self.podpisane_xml.toprettyxml().encode('utf-8','ignore')
            file = open("Output.xml", "w")
            file.write(text)
            file.close()

            self.outPut.clear()
            self.outPut.insertPlainText(self.podpisane_xml.toprettyxml().encode('utf-8','ignore'))
            self.outError.insertPlainText('Podpis uspesny \n')
        else:
            self.outError.insertPlainText('Chyba pro podpise, res nebol 0 \n')
            self.outError.insertPlainText(oXML.ErrorMessage)

    def peciatka(self):
        #ds:SignatureValue
        if self.podpisane_xml:
            value = self.podpisane_xml.getElementsByTagName('ds:SignatureValue')
            for item in value:
                sigValue  = item.firstChild.nodeValue
                self.outPut.setPlainText(sigValue)

            xmlDopyt = "<?xml version=\"1.0\" encoding=\"utf-8\"?> <soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">"\
                + "<soap:Body>"\
                + " <GetTimestamp xmlns=\"http://www.ditec.sk/\"> "\
                + "    <dataB64>"\
                + sigValue\
                + "</dataB64> "\
                + " </GetTimestamp> " + " </soap:Body> " + "</soap:Envelope>"

            headers = {"Host": "test.ditec.sk","Content-type": "text/xml; charset=utf-8", "Content-Length": len(xmlDopyt),"SOAPAction": "http://www.ditec.sk/GetTimestamp"}
            req = urllib2.Request(url="http://test.ditec.sk/timestampws/TS.asmx",data=xmlDopyt,
                      headers=headers)

            response = urllib2.urlopen(req).read()

            response_xml = parseString(response)
            timestamp_result = response_xml.getElementsByTagName("GetTimestampResult")
            timestamp_result = timestamp_result[0].firstChild.nodeValue
            print timestamp_result

            command = "java -jar TimestampFactory.jar " + str(timestamp_result)
            new_timestamp = check_output(command, shell=True)
            print timestamp_result
            print timestamp_result[-1]
            print timestamp_result[-2]
            element = self.podpisane_xml.getElementsByTagName("xades:QualifyingProperties")
            element = element[0]

            unsign_prop = self.podpisane_xml.createElement("xades:UnsignedProperties")
            element.appendChild(unsign_prop)

            unsigned_sig_prop = self.podpisane_xml.createElement("xades:UnsignedSignatureProperties")
            unsign_prop.appendChild(unsigned_sig_prop)

            id = uuid.uuid4()
            id = str(id)
            element = self.podpisane_xml.createElement("xades:SignatureTimeStamp")
            element.setAttribute("Id",id)
            unsigned_sig_prop.appendChild(element)

            novy_element = self.podpisane_xml.createElement("xades:EncapsulatedTimeStamp")


            novy_element.appendChild(self.podpisane_xml.createTextNode(new_timestamp))
            element.appendChild(novy_element)

            text =  self.podpisane_xml.toprettyxml().encode('utf-8','ignore')
            #text2 = self.podpisane_xml.encode('utf-8')
            file = open("Output_signed.xml", "w")
            print self.podpisane_xml.toxml()
            print type(self.podpisane_xml)
            file.write(text)
            file.close()

            self.outError.insertPlainText('Peciatka uspesna')
            self.outPut.clear()
            self.outPut.insertPlainText(text)
        else:
            self.outError.insertPlainText('Dokument este nebol podpisany \n')











if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

