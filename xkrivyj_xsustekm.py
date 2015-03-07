# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Fri Mar  6 22:26:16 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def __init__(self):
        self.xml = 'aa'

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setFixedSize(726, 636)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 451, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 50, 701, 41))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(11, 11, 30, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(220, 11, 46, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(445, 11, 72, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(47, 11, 167, 20))
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(272, 11, 167, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(523, 11, 167, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.frame_6 = QtGui.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(10, 100, 701, 41))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.label_19 = QtGui.QLabel(self.frame_6)
        self.label_19.setGeometry(QtCore.QRect(11, 11, 41, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.frame_6)
        self.label_20.setGeometry(QtCore.QRect(220, 11, 71, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.frame_6)
        self.label_21.setGeometry(QtCore.QRect(445, 11, 72, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_18 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_18.setGeometry(QtCore.QRect(60, 10, 161, 20))
        self.lineEdit_18.setMaxLength(32767)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_19 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_19.setGeometry(QtCore.QRect(288, 11, 151, 20))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(self.frame_6)
        self.lineEdit_20.setGeometry(QtCore.QRect(509, 11, 181, 20))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 701, 41))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(11, 11, 41, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(58, 11, 281, 22))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 98, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(457, 10, 231, 22))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.frame_3 = QtGui.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 200, 701, 41))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(11, 11, 30, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(47, 11, 180, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_8 = QtGui.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(233, 11, 44, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_7 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(283, 11, 179, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_9 = QtGui.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(468, 11, 36, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_8 = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(510, 11, 180, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))

        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 701, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.scrollArea_2 = QtGui.QScrollArea(self.groupBox)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 19, 701, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))



        self.pushButton_2 = QtGui.QPushButton(self.scrollArea_2)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 10, 80, 22))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.addWidget)




        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 480, 611, 141))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.scrollArea = QtGui.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 611, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 119))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 500, 81, 22))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.validate)

        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 530, 81, 22))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.show)

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(630, 560, 81, 22))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.clear)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def create_row(self):
        self.list_scrollAreas=list()


        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 699, 199))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))


        self.frame_5 = QtGui.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 681, 41))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.label_13 = QtGui.QLabel(self.frame_5)
        self.label_13.setGeometry(QtCore.QRect(11, 10, 40, 22))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_13 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_13.setGeometry(QtCore.QRect(57, 10, 231, 22))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_12 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_12.setGeometry(QtCore.QRect(350, 10, 51, 22))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_14 = QtGui.QLineEdit(self.frame_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(460, 10, 121, 22))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))

        self.label_14 = QtGui.QLabel(self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(400, 10, 54, 22))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(290, 10, 57, 22))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.label_13.setText(QtGui.QApplication.translate("Form", "Názov:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "  Priorita:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "  Termín:", None, QtGui.QApplication.UnicodeUTF8))

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Krivý & Šustek - SIVPAVS 2015", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Registrácia účastníka školenia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Titul:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "  Meno:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "  Priezvisko:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Form", "Firma:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Form", "  Pobočka:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Form", "  Pozícia:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "E-mail:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Telefónne číslo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Štát:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "  Obec:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "  PSČ:", None, QtGui.QApplication.UnicodeUTF8))

        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Vybrané školenia", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Pridať", None, QtGui.QApplication.UnicodeUTF8))




        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Chybový výstup:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Validovať", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Zobraziť", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Vyčistiť", None, QtGui.QApplication.UnicodeUTF8))

    def addWidget(self):
        self.create_row()

    def validate(self):
        print self.xml
        #titul
        print self.lineEdit.text()
        #meno
        print self.lineEdit_2.text()
        #priezvysko
        print self.lineEdit_3.text()
        #email
        print self.lineEdit_4.text()
        #cislo
        print self.lineEdit_5.text()
        #stat
        print self.lineEdit_6.text()
        #obec
        print self.lineEdit_7.text()


    def show(self):
        self.groupBox.hide()

    def clear(self):
        self.groupBox.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

