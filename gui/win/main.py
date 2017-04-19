# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_win_main(object):
    def setupUi(self, win_main):
        win_main.setObjectName(_fromUtf8("win_main"))
        win_main.resize(480, 320)
        win_main.setMaximumSize(QtCore.QSize(480, 320))
        self.btn_close = QtGui.QPushButton(win_main)
        self.btn_close.setGeometry(QtCore.QRect(10, 280, 88, 34))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.img_escudo = QtGui.QLabel(win_main)
        self.img_escudo.setGeometry(QtCore.QRect(367, 0, 113, 87))
        self.img_escudo.setMaximumSize(QtCore.QSize(113, 87))
        self.img_escudo.setText(_fromUtf8(""))
        self.img_escudo.setPixmap(QtGui.QPixmap(_fromUtf8("gui/img/escudo.png")))
        self.img_escudo.setScaledContents(True)
        self.img_escudo.setIndent(-1)
        self.img_escudo.setObjectName(_fromUtf8("img_escudo"))
        self.lbl_nombres = QtGui.QLabel(win_main)
        self.lbl_nombres.setGeometry(QtCore.QRect(20, 50, 350, 18))
        self.lbl_nombres.setObjectName(_fromUtf8("lbl_nombres"))
        self.img_status = QtGui.QLabel(win_main)
        self.img_status.setGeometry(QtCore.QRect(190, 200, 64, 64))
        self.img_status.setText(_fromUtf8(""))
        self.img_status.setPixmap(QtGui.QPixmap(_fromUtf8("gui/img/check_icon.png")))
        self.img_status.setScaledContents(True)
        self.img_status.setObjectName(_fromUtf8("img_status"))
        self.lbl_institucion = QtGui.QLabel(win_main)
        self.lbl_institucion.setGeometry(QtCore.QRect(20, 70, 350, 18))
        self.lbl_institucion.setObjectName(_fromUtf8("lbl_institucion"))
        self.lbl_info = QtGui.QLabel(win_main)
        self.lbl_info.setGeometry(QtCore.QRect(20, 90, 350, 18))
        self.lbl_info.setObjectName(_fromUtf8("lbl_info"))

        self.retranslateUi(win_main)
        QtCore.QMetaObject.connectSlotsByName(win_main)

    def retranslateUi(self, win_main):
        win_main.setWindowTitle(_translate("win_main", "Form", None))
        self.btn_close.setText(_translate("win_main", "Cerrar", None))
        self.lbl_nombres.setText(_translate("win_main", "ACA QUEDARIA EL NOMBRE DEL ESTUDIANTE", None))
        self.lbl_institucion.setText(_translate("win_main", "ACA QUEDARIA EL NOMBRE DEL COLEGIO", None))
        self.lbl_info.setText(_translate("win_main", "ACA QUEDARIA ALGUNA INFORMACION EXTRA", None))

