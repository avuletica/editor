# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydialogCedit.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self): 
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 247)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 361, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.tabWidget.addTab(self.tab, "") 
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayout = QtWidgets.QFormLayout(self.tab_3)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_3)
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(12)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_3)
        self.lcdNumber.setMaximumSize(QtCore.QSize(50, 25))
        self.lcdNumber.setStyleSheet("background: #555555")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 2.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_3.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_2.addWidget(self.checkBox_6)
        self.spinBox = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox.setMaximumSize(QtCore.QSize(40, 25))
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(120)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.spinBox_2.setMinimum(10)
        self.spinBox_2.setMaximum(20)
        self.spinBox_2.setProperty("value", 15)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.listWidget = QtWidgets.QListWidget(self.tab_4)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.listWidget)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget_5.setGeometry(QtCore.QRect(9, 9, 361, 141))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Display line numbers"))
        self.checkBox_2.setText(_translate("Dialog", "Display status bar"))
        self.checkBox_3.setText(_translate("Dialog", "Remember current session for next launch"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "General"))
        self.label.setText(_translate("Dialog", "Tab width:"))
        self.checkBox_4.setText(_translate("Dialog", "Insert spaces insted of tabs"))
        self.checkBox_5.setText(_translate("Dialog", "Highlight current line"))
        self.checkBox_6.setText(_translate("Dialog", "Autosave files every"))
        self.label_4.setText(_translate("Dialog", "minutes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Editor"))
        self.label_2.setText(_translate("Dialog", "Font size:"))
        self.label_3.setText(_translate("Dialog", "Color Scheme:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "Classic - Classic colour scheme"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "Oblivion - Dark colour scheme"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "Cobalt - Blue-based colour scheme"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "Solarized Light - Solarized light color palette"))
        item = self.listWidget.item(4)
        item.setText(_translate("Dialog", "Solarized Dark - Solarized dark color palette"))
        item = self.listWidget.item(5)
        item.setText(_translate("Dialog", "Azura"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Font"))
        self.radioButton.setText(_translate("Dialog", "Launch in fullscreen"))
        self.radioButton_2.setText(_translate("Dialog", "Launch maximized"))
        self.radioButton_3.setText(_translate("Dialog", "Launch in window mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Startup"))


    def SaveSettings(self):
        f = open("Settings.txt", "w")
        settings = ["Display line numbers = ",self.checkBox.checkState(),"\nDisplay status Bar = ",self.checkBox_2.checkState(),
        "\nRemember sesion = ",self.checkBox_3.checkState(),"\nTab width = ",self.horizontalSlider.value(),
        "\nInsert space insted = ",self.checkBox_4.checkState(),"\nHighlight current line = ",self.checkBox_5.checkState(),
        "\nAutosave = ",self.checkBox_6.checkState(),"\nAutosave minutes = ",self.spinBox.value(),
        "\nFont size = ",self.spinBox_2.value(),"\nLaunch in fullscreen = ",self.radioButton.isChecked(),
        "\nLaunch maximized = ",self.radioButton_2.isChecked(),"\nLaunch in window mode = ",self.radioButton_3.isChecked()
        ]
        
        for item in settings:
            f.write("%s" % item)
        f.close()

    def LoadSettings(self):
        try:
            f = open("Settings.txt","r")
            items = []
        
            for line in f:
                item = line.split("=")
                items.append(item[1].strip())
            
            if(items):
                if(int(items[0])):
                    self.checkBox.setCheckState(QtCore.Qt.Checked)
                if(int(items[1])):
                    self.checkBox_2.setCheckState(QtCore.Qt.Checked)
                if(int(items[2])):
                    self.checkBox_3.setCheckState(QtCore.Qt.Checked)
                if(int(items[3])):
                   self.horizontalSlider.setValue(int(items[3]))
                if(int(items[4])):
                    self.checkBox_4.setCheckState(QtCore.Qt.Checked)
                if(int(items[5])):
                    self.checkBox_5.setCheckState(QtCore.Qt.Checked)
                if(int(items[6])):
                    self.checkBox_6.setCheckState(QtCore.Qt.Checked)
                if(int(items[7])):
                     self.spinBox.setValue(int(items[7]))
                if(int(items[8])):
                     self.spinBox_2.setValue(int(items[8]))
                
                if(items[9] == "True"):
                    self.radioButton.setChecked(True)
                elif(items[10] == "True"):
                    self.radioButton_2.setChecked(True)
                elif(items[11] == "True"):
                    self.radioButton_3.setChecked(True)                          

            f.close()
        except:
            pass
                

if __name__ == '__main__':
    cdialog = Ui_Dialog()
    cdialog.show()
    exit = dialog.exec_()
    sys.exit(exit)