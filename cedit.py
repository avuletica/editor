from PyQt5 import QtCore, QtGui, QtWidgets 
from mydialog import *
import sys
import os
import threading
import subprocess

class TitleBar(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		titleBarStyle = """
	 
		QWidget {
		background-color: #rgb(222, 222, 222);
		color:black;
		font:13px;
		border: 0px;
		height: 11px;
		}
		QToolButton:hover {
		background-color: #263238;
		border-radius: 12px;
		}"""

		self.setStyleSheet(titleBarStyle)
		self.minimize=QtWidgets.QToolButton(self)
		self.minimize.setIcon(QtGui.QIcon('Resources/minimize.png'))
		self.maximize=QtWidgets.QToolButton(self)
		self.maximize.setIcon(QtGui.QIcon('Resources/maximize.png'))
		close=QtWidgets.QToolButton(self)
		close.setIcon(QtGui.QIcon('Resources/close.png'))

		self.minimize.setMinimumHeight(24)
		self.minimize.setMinimumWidth(24)
		close.setMinimumHeight(24)
		close.setMinimumWidth(24)
		self.maximize.setMinimumHeight(24)
		self.maximize.setMinimumWidth(24)

		label=QtWidgets.QLabel(self)
		label.setText("NoName")
		label.setToolTip("Author: Josip Vuletić Antić")
		self.setWindowTitle("Window Title")
		hbox=QtWidgets.QHBoxLayout(self)
		hbox.addWidget(label)
		hbox.addWidget(self.minimize)
		hbox.addWidget(self.maximize)
		hbox.addWidget(close)
		hbox.insertStretch(1,500)
		hbox.setSpacing(0)
		self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed) 

		close.clicked.connect(self.close)
		self.minimize.clicked.connect(self.showSmall)
		self.maximize.clicked.connect(self.showMaxRestore)
   
	def showSmall(self):
		cwindow.showMinimized()

	def showMaxRestore(self):
		if(cwindow.isMaximized() or cwindow.isFullScreen()):
			cwindow.showNormal()
			#self.maximize.setIcon(QtGui.QIcon('data/img/min-max.png'))
		else:
			cwindow.showMaximized()
			#self.maximize.setIcon(QtGui.QIcon('data/img/max-min.png'))
	
	def close(self):
		try:
			f = open("Settings.txt","a")
			location = ceditor.statusbarLocationLabel.text()
			f.write("\nLast sesion = ")
			f.write(location)
			f.close()
		except:
			pass

		os._exit(1)

	def mousePressEvent(self,event):
		if event.button() == QtCore.Qt.LeftButton:
			cwindow.moving = True; cwindow.offset = event.pos()

	def mouseMoveEvent(self,event):
		if cwindow.moving: cwindow.move(event.globalPos()-cwindow.offset) 


class Ui_MainWindow(QtWidgets.QMainWindow):
	def __init__(self): 
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)

	#----- Static based -----
	i=0 # used for LineNumberArea
	word="yo" #used for Find
	found=False  #used for Find
	#---------------------------

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setSpacing(0)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.splitter = QtWidgets.QSplitter(self.centralwidget)
		self.splitter.setAutoFillBackground(False)
		self.splitter.setStyleSheet(" border-color: #555555;")
		self.splitter.setOrientation(QtCore.Qt.Vertical)
		self.splitter.setObjectName("splitter")
		self.splitter.setStyleSheet(" background-color: #555555;")
		self.layoutWidget = QtWidgets.QWidget(self.splitter)
		self.layoutWidget.setObjectName("layoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.lineTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
		self.lineTextEdit.setMaximumSize(QtCore.QSize(70, 16777215))
		self.lineTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.lineTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.lineTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.lineTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.lineTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.lineTextEdit.setReadOnly(True)
		self.lineTextEdit.setObjectName("lineTextEdit")
		self.horizontalLayout.addWidget(self.lineTextEdit)
		self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
		self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
		self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
		self.plainTextEdit.setObjectName("plainTextEdit")
		self.horizontalLayout.addWidget(self.plainTextEdit)
		self.BuildTextEdit = QtWidgets.QTextEdit(self.splitter)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.BuildTextEdit.sizePolicy().hasHeightForWidth())
		self.BuildTextEdit.setSizePolicy(sizePolicy)
		self.BuildTextEdit.setMaximumSize(QtCore.QSize(16777215, 170))
		self.BuildTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.BuildTextEdit.setObjectName("BuildTextEdit")
		self.BuildTextEdit.setReadOnly(True)
		self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setSpacing(0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.SearchTextEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.SearchTextEdit.setMaximumSize(QtCore.QSize(16777215, 20))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.SearchTextEdit.setFont(font)
		self.SearchTextEdit.setText("")
		self.SearchTextEdit.setObjectName("SearchTextEdit")
		self.horizontalLayout_2.addWidget(self.SearchTextEdit)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setMaximumSize(QtCore.QSize(16777215, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_2.addWidget(self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_2.addWidget(self.pushButton_2)
		self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_3.setFont(font)
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout_2.addWidget(self.pushButton_3)
		self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_4.setMaximumSize(QtCore.QSize(20, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_4.setFont(font)
		self.pushButton_4.setObjectName("pushButton_4")
		self.horizontalLayout_2.addWidget(self.pushButton_4)
		self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuEdit = QtWidgets.QMenu(self.menubar)
		self.menuEdit.setObjectName("menuEdit")
		self.menuText = QtWidgets.QMenu(self.menuEdit)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("Resources/1426905721_internt_web_technology-05-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.menuText.setIcon(icon)
		self.menuText.setObjectName("menuText")
		self.menuView = QtWidgets.QMenu(self.menubar)
		self.menuView.setObjectName("menuView")
		self.menuSettings = QtWidgets.QMenu(self.menubar)
		self.menuSettings.setObjectName("menuSettings")
		self.menuHelp = QtWidgets.QMenu(self.menubar)
		self.menuHelp.setObjectName("menuHelp")
		self.menuTools = QtWidgets.QMenu(self.menubar)
		self.menuTools.setObjectName("menuTools")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionNew_File = QtWidgets.QAction(MainWindow)
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("Resources/1426907527_file-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionNew_File.setIcon(icon1)
		self.actionNew_File.setObjectName("actionNew_File")
		self.actionOpen_File = QtWidgets.QAction(MainWindow)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("Resources/1426906755_opened_folder-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionOpen_File.setIcon(icon2)
		self.actionOpen_File.setObjectName("actionOpen_File")
		self.actionSave_As = QtWidgets.QAction(MainWindow)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("Resources/1426907380_editor_floopy-dish_save-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSave_As.setIcon(icon3)
		self.actionSave_As.setObjectName("actionSave_As")
		self.actionSave = QtWidgets.QAction(MainWindow)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap("Resources/1426907164_Noun_Project_100Icon_10px_grid-38-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionSave.setIcon(icon4)
		self.actionSave.setObjectName("actionSave")
		self.actionFind = QtWidgets.QAction(MainWindow)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap("Resources/magnify_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionFind.setIcon(icon5)
		self.actionFind.setObjectName("actionFind")
		self.actionUndo = QtWidgets.QAction(MainWindow)
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap("Resources/1426904528_back-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionUndo.setIcon(icon6)
		self.actionUndo.setObjectName("actionUndo")
		self.actionRedo = QtWidgets.QAction(MainWindow)
		icon7 = QtGui.QIcon()
		icon7.addPixmap(QtGui.QPixmap("Resources/1426904525_icon-ios7-redo-outline-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionRedo.setIcon(icon7)
		self.actionRedo.setObjectName("actionRedo")
		self.actionCut = QtWidgets.QAction(MainWindow)
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap("Resources/1426904563_cut-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionCut.setIcon(icon8)
		self.actionCut.setObjectName("actionCut")
		self.actionCopy = QtWidgets.QAction(MainWindow)
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap("Resources/1426904573_copy-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionCopy.setIcon(icon9)
		self.actionCopy.setObjectName("actionCopy")
		self.actionPaste = QtWidgets.QAction(MainWindow)
		icon10 = QtGui.QIcon()
		icon10.addPixmap(QtGui.QPixmap("Resources/icon_print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionPaste.setIcon(icon10)
		self.actionPaste.setObjectName("actionPaste")
		self.actionInsert_After = QtWidgets.QAction(MainWindow)
		self.actionInsert_After.setObjectName("actionInsert_After")
		self.actionInsert_Before = QtWidgets.QAction(MainWindow)
		self.actionInsert_Before.setObjectName("actionInsert_Before")
		self.actionDelete_Line = QtWidgets.QAction(MainWindow)
		self.actionDelete_Line.setObjectName("actionDelete_Line")
		self.actionDelete_To_Start = QtWidgets.QAction(MainWindow)
		self.actionDelete_To_Start.setObjectName("actionDelete_To_Start")
		self.actionDelete_To_ENd = QtWidgets.QAction(MainWindow)
		self.actionDelete_To_ENd.setObjectName("actionDelete_To_ENd")
		self.actionEnter_Fullscreen = QtWidgets.QAction(MainWindow)
		icon11 = QtGui.QIcon()
		icon11.addPixmap(QtGui.QPixmap("Resources/sc-fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionEnter_Fullscreen.setIcon(icon11)
		self.actionEnter_Fullscreen.setObjectName("actionEnter_Fullscreen")
		self.actionMaximize = QtWidgets.QAction(MainWindow)
		icon12 = QtGui.QIcon()
		icon12.addPixmap(QtGui.QPixmap("Resources/aiwWorkflowMaximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionMaximize.setIcon(icon12)
		self.actionMaximize.setObjectName("actionMaximize")
		self.actionPreferences = QtWidgets.QAction(MainWindow)
		icon13 = QtGui.QIcon()
		icon13.addPixmap(QtGui.QPixmap("Resources/1426903823_handrawn_tool_doodle_Settings-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionPreferences.setIcon(icon13)
		self.actionPreferences.setObjectName("actionPreferences")
		self.actionAbout = QtWidgets.QAction(MainWindow)
		icon14 = QtGui.QIcon()
		icon14.addPixmap(QtGui.QPixmap("Resources/about-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionAbout.setIcon(icon14)
		self.actionAbout.setObjectName("actionAbout")
		self.actionBuild = QtWidgets.QAction(MainWindow)
		icon15 = QtGui.QIcon()
		icon15.addPixmap(QtGui.QPixmap("Resources/1426903750_handrawn_Settings_user-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionBuild.setIcon(icon15)
		self.actionBuild.setObjectName("actionBuild")
		self.actionRun = QtWidgets.QAction(MainWindow)
		icon16 = QtGui.QIcon()
		icon16.addPixmap(QtGui.QPixmap("Resources/Crystal_Clear_app_terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionRun.setIcon(icon16)
		self.actionRun.setObjectName("actionRun")
		self.actionMinimize = QtWidgets.QAction(MainWindow)
		icon17 = QtGui.QIcon()
		icon17.addPixmap(QtGui.QPixmap("Resources/Restore_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.actionMinimize.setIcon(icon17)
		self.actionMinimize.setObjectName("actionMinimize")
		self.menuFile.addAction(self.actionNew_File)
		self.menuFile.addAction(self.actionOpen_File)
		self.menuFile.addAction(self.actionSave_As)
		self.menuFile.addAction(self.actionSave)
		self.menuText.addAction(self.actionInsert_After)
		self.menuText.addAction(self.actionInsert_Before)
		self.menuText.addSeparator()
		self.menuText.addAction(self.actionDelete_Line)
		self.menuText.addAction(self.actionDelete_To_Start)
		self.menuText.addAction(self.actionDelete_To_ENd)
		self.menuEdit.addAction(self.actionUndo)
		self.menuEdit.addAction(self.actionRedo)
		self.menuEdit.addSeparator()
		self.menuEdit.addAction(self.actionCut)
		self.menuEdit.addAction(self.actionCopy)
		self.menuEdit.addAction(self.actionPaste)
		self.menuEdit.addSeparator()
		self.menuEdit.addAction(self.actionFind)
		self.menuEdit.addAction(self.menuText.menuAction())
		self.menuView.addAction(self.actionMaximize)
		self.menuView.addAction(self.actionMinimize)
		self.menuView.addAction(self.actionEnter_Fullscreen)
		self.menuSettings.addAction(self.actionPreferences)
		self.menuHelp.addAction(self.actionAbout)
		self.menuTools.addAction(self.actionBuild)
		self.menuTools.addAction(self.actionRun)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuEdit.menuAction())
		self.menubar.addAction(self.menuView.menuAction())
		self.menubar.addAction(self.menuSettings.menuAction())
		self.menubar.addAction(self.menuTools.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())
			   
		#----------------A D D E D----------------
		#self.lineTextEdit.setReadOnly(1)
		#self.lineTextEdit.setMaximumWidth(70)
		style = '''
		font: 15pt; 
		selection-background-color: rgba(191, 191, 191, 189);
		background: #272822;color: rgb(255, 255, 255);'''

		self.setStyleSheet("QStatusBar::item { border: 0px;};   ")
		#self.statusbar.setAlignment(QtCore.Qt.AlignVCenter)

		self.plainTextEdit.setStyleSheet(style)
		self.lineTextEdit.setStyleSheet(style)
		self.SearchTextEdit.setStyleSheet(style)
		self.BuildTextEdit.setStyleSheet(style)
		self.BuildTextEdit.verticalScrollBar().setStyleSheet("background: #272822")
		self.pushButton.setStyleSheet("background: #272822;color: rgb(255, 255, 255)")
		self.pushButton_2.setStyleSheet("background: #272822;color: rgb(255, 255, 255)")
		self.pushButton_3.setStyleSheet("background: #272822;color: rgb(255, 255, 255)")
		self.pushButton_4.setStyleSheet("background: #272822;color: rgb(255, 255, 255)")
		self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.lineTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.lineTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.lineTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.SearchTextEdit.hide()
		self.pushButton.hide()
		self.pushButton_2.hide()
		self.pushButton_3.hide()
		self.pushButton_4.hide()
		self.BuildTextEdit.hide()
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		self.statusbar.setStyleSheet("background: #555555;color: white")

		self.statusbarLocationLabel = QtWidgets.QLabel(MainWindow)
		self.statusbarLocationLabel.setGeometry(QtCore.QRect(180, 90, 68, 20))
		self.statusbarLocationLabel.setObjectName("statusbarLocationLabel")
		self.statusbar.insertPermanentWidget(2,self.statusbarLocationLabel,0)
		self.statusbarLocationLabel.setStyleSheet("color: rgb(255, 255, 255);")
		


		self.statusbarLineLabel = QtWidgets.QLabel(MainWindow)
		self.statusbarLineLabel.setAlignment(QtCore.Qt.AlignVCenter)
		self.statusbarLineLabel.setGeometry(QtCore.QRect(180, 90, 68, 20))
		self.statusbarLineLabel.setObjectName("statusbarLineLabel")

		self.statusbar.insertPermanentWidget(0,self.statusbarLineLabel,0)
		self.statusbarLineLabel.setStyleSheet("color: rgb(255, 255, 255);")
		
		

		self.statusbarColumnLabel = QtWidgets.QLabel(MainWindow)
		self.statusbarColumnLabel.setGeometry(QtCore.QRect(180, 90, 68, 20))
		self.statusbarColumnLabel.setObjectName("statusbarColumnLabel")
		self.statusbar.insertPermanentWidget(1,self.statusbarColumnLabel,50)
		self.statusbarColumnLabel.setStyleSheet("color: rgb(255, 255, 255);")
		
		

		
	   
		MainWindow.setStatusBar(self.statusbar)
		self.plainTextEdit.textChanged.connect(self.LineNumberArea)
		self.plainTextEdit.cursorPositionChanged.connect(self.HighlightLine)
		self.plainTextEdit.cursorPositionChanged.connect(self.ShowColumn)
		self.plainTextEdit.verticalScrollBar().valueChanged.connect(self.SyncScrollBar)
		MainWindow.setCentralWidget(self.centralwidget)

		self.actionNew_File.triggered.connect(self.NewFile)
		self.actionOpen_File.triggered.connect(self.OpenFile)
		self.actionSave_As.triggered.connect(self.SaveFileAs)
		self.actionSave.triggered.connect(self.SaveFile)

		self.actionUndo.triggered.connect(self.Undo)
		self.actionRedo.triggered.connect(self.Redo)
		self.actionCut.triggered.connect(self.Cut)
		self.actionCopy.triggered.connect(self.Copy)
		self.actionPaste.triggered.connect(self.Paste)
		self.actionFind.triggered.connect(self.ShowFind)
		self.actionInsert_After.triggered.connect(self.InsertAfter)
		self.actionInsert_Before.triggered.connect(self.InsertBefore)
		self.actionDelete_Line.triggered.connect(self.DeleteLine)
		self.actionDelete_To_Start.triggered.connect(self.DeleteToStart)
		self.actionDelete_To_ENd.triggered.connect(self.DeleteToEnd)
		
		self.actionMaximize.triggered.connect(self.Maximize)
		self.actionMinimize.triggered.connect(self.Minimize)
		self.actionEnter_Fullscreen.triggered.connect(self.EnterFullscreen)
		
		self.actionPreferences.triggered.connect(self.SettingsDialog) 
		self.pushButton_4.clicked.connect(self.CloseFind)
		self.pushButton_2.clicked.connect(self.FindPrevious)
		self.pushButton.clicked.connect(self.Find)
		self.pushButton_3.clicked.connect(self.FindAll)
		self.actionBuild.triggered.connect(self.ShowBuild)
		self.actionRun.triggered.connect(self.Run)

		cdialog.listWidget.currentRowChanged.connect(self.ColorSheme)		
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)      
		#------------------------------------------------------------------------------
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Find"))
		self.pushButton_2.setText(_translate("MainWindow", "Find Previous"))
		self.pushButton_3.setText(_translate("MainWindow", "Find All"))
		self.pushButton_4.setText(_translate("MainWindow", "X"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
		self.menuText.setTitle(_translate("MainWindow", "Text"))
		self.menuView.setTitle(_translate("MainWindow", "View"))
		self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
		self.menuHelp.setTitle(_translate("MainWindow", "Help"))
		self.menuTools.setTitle(_translate("MainWindow", "Tools"))
		self.actionNew_File.setText(_translate("MainWindow", "New File"))
		self.actionNew_File.setShortcut(_translate("MainWindow", "Ctrl+N"))
		self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
		self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
		self.actionSave_As.setText(_translate("MainWindow", "Save As"))
		self.actionSave_As.setShortcut(_translate("MainWindow", "Alt+S"))
		self.actionSave.setText(_translate("MainWindow", "Save"))
		self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
		self.actionFind.setText(_translate("MainWindow", "Find"))
		self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F"))
		self.actionUndo.setText(_translate("MainWindow", "Undo"))
		self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
		self.actionRedo.setText(_translate("MainWindow", "Redo"))
		self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
		self.actionCut.setText(_translate("MainWindow", "Cut"))
		self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
		self.actionCopy.setText(_translate("MainWindow", "Copy"))
		self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
		self.actionPaste.setText(_translate("MainWindow", "Paste"))
		self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
		self.actionInsert_After.setText(_translate("MainWindow", "Insert Line After"))
		self.actionInsert_After.setShortcut(_translate("MainWindow", "Ctrl+Return"))
		self.actionInsert_Before.setText(_translate("MainWindow", "Insert Line Before"))
		self.actionInsert_Before.setShortcut(_translate("MainWindow", "Ctrl+Shift+Return"))
		self.actionDelete_Line.setText(_translate("MainWindow", "Delete Line"))
		self.actionDelete_Line.setShortcut(_translate("MainWindow", "Ctrl+Del"))
		self.actionDelete_To_Start.setText(_translate("MainWindow", "Delete To Start"))
		self.actionDelete_To_Start.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
		self.actionDelete_To_ENd.setText(_translate("MainWindow", "Delete To End"))
		self.actionDelete_To_ENd.setShortcut(_translate("MainWindow", "Alt+Backspace"))
		self.actionEnter_Fullscreen.setText(_translate("MainWindow", "Fullscreen"))
		self.actionEnter_Fullscreen.setShortcut(_translate("MainWindow", "F3"))
		self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
		self.actionMaximize.setShortcut(_translate("MainWindow", "F1"))
		self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
		self.actionPreferences.setShortcut(_translate("MainWindow", "Alt+O"))
		self.actionAbout.setText(_translate("MainWindow", "About"))
		self.actionBuild.setText(_translate("MainWindow", "Build"))
		self.actionBuild.setShortcut(_translate("MainWindow", "Ctrl+B"))
		self.actionRun.setText(_translate("MainWindow", "Run"))
		self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R"))
		self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
		self.actionMinimize.setShortcut(_translate("MainWindow", "F2"))

	'''
	QtCore.Qt.Key_Return is a value that equates to what the operating system passes to python from
	the keyboard when the return key is pressed.
	'''
	def keyPressEvent(self, e):
		if(e.key() == QtCore.Qt.Key_Return):
			self.pushButton.click()

	def NewFile(self):
		check = QtWidgets.QMessageBox.information(self,"Warrning",
		"Do you wish to save current file?",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
		exists = self.statusbarLocationLabel.text() #checking for location of file
		
		if(check == QtWidgets.QMessageBox.Yes): 
			if(exists):
				self.SaveFile()
			else:
				self.SaveFileAs()  
	   
		self.plainTextEdit.clear()
		self.statusbarLocationLabel.clear()

	def OpenFile(self):   
		filename = QtWidgets.QFileDialog.getOpenFileName(self,"Open File","")
		filename = filename[0]  
		if(filename): # checks if string is empty
			self.statusbarLocationLabel.setText(filename)      
			f = open(filename, 'r')
			filedata = f.read()
			self.plainTextEdit.setPlainText(filedata)
			position = self.plainTextEdit.verticalScrollBar().sliderPosition()
			self.lineTextEdit.verticalScrollBar().setValue(position) 
			f.close()

	def SaveFileAs(self):
		filename = QtWidgets.QFileDialog.getSaveFileName(self,"Save File","")
		filename = filename[0]
		self.statusbarLocationLabel.setText(filename)
		f = open(filename, 'w')
		filedata = self.plainTextEdit.toPlainText()
		f.write(filedata)
		f.close()

	def SaveFile(self):
		filename = self.statusbarLocationLabel.text()
		try:
			f = open(filename, 'w')
			filedata = self.plainTextEdit.toPlainText()
			f.write(filedata)
			f.close()
		except:
			pass
	def Undo(self):
		self.plainTextEdit.undo()

	def Redo(self):
		self.plainTextEdit.redo()        

	def Cut(self):
		self.plainTextEdit.cut()

	def Copy(self):
		self.plainTextEdit.copy()

	def Paste(self):
		self.plainTextEdit.paste()

	def Find(self):
		word = self.SearchTextEdit.text()
		
		if(self.word != word):
			self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start)
			self.plainTextEdit.find(word)
		elif(self.word == word):
			self.plainTextEdit.moveCursor(QtGui.QTextCursor.NextCharacter)
			self.found=self.plainTextEdit.find(word)
		
		if(not self.found):
			self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start)
			self.plainTextEdit.find(word)       

		self.word=word
		self.SearchTextEdit.setFocus()
		
	def FindPrevious(self):
		word = self.SearchTextEdit.text()
		self.plainTextEdit.find(word,QtGui.QTextDocument.FindBackward)  

	def FindAll(self):
		word = self.SearchTextEdit.text()
		extraSelections = [] 

		self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start)
		while(self.plainTextEdit.find(word,QtGui.QTextDocument.FindWholeWords)):
			Color = QtGui.QColor(0,255,45)            
			selection = QtWidgets.QTextEdit.ExtraSelection()
			selection.format.setForeground(Color)
			selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, QtCore.QVariant(True))
			selection.cursor = self.plainTextEdit.textCursor()
			#selection.cursor.clearSelection()
			extraSelections.append(selection)

		self.plainTextEdit.setExtraSelections(extraSelections)
		self.plainTextEdit.setFocus()  

	def ShowFind(self):
		self.SearchTextEdit.show()
		self.pushButton.show()
		self.pushButton_2.show()
		self.pushButton_3.show()
		self.pushButton_4.show()
		self.SearchTextEdit.setFocus()

	def CloseFind(self):
		self.SearchTextEdit.clear()
		self.SearchTextEdit.hide()
		self.pushButton.hide()
		self.pushButton_2.hide()
		self.pushButton_3.hide()
		self.pushButton_4.hide()

	def InsertAfter(self):
		self.plainTextEdit.insertPlainText("\n")

	def InsertBefore(self):
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.Up)
		self.plainTextEdit.insertPlainText("\n")

	def DeleteLine(self):
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.StartOfLine,QtGui.QTextCursor.MoveAnchor)
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.EndOfLine,QtGui.QTextCursor.KeepAnchor)
		self.plainTextEdit.textCursor().removeSelectedText()
	
	def DeleteToStart(self):
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start,QtGui.QTextCursor.KeepAnchor)
		self.plainTextEdit.textCursor().removeSelectedText()

	def DeleteToEnd(self):
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.StartOfLine,QtGui.QTextCursor.MoveAnchor)
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.End,QtGui.QTextCursor.KeepAnchor)
		self.plainTextEdit.textCursor().removeSelectedText()

	def Maximize(self):
		if(cwindow.isMaximized() or cwindow.isFullScreen()):
			cwindow.showNormal()
		else:
			cwindow.showMaximized()

	def Minimize(self):
		cwindow.showMinimized()

	def EnterFullscreen(self):
		if(cwindow.isFullScreen()):
			cwindow.showNormal() 
		else:
			cwindow.showFullScreen()    

	def SettingsDialog(self):
		cdialog.show()
		cdialog.move(QtWidgets.QApplication.desktop().screen().rect().center() - cdialog.rect().center());
		cdialog.buttonBox.accepted.connect(self.CallSettings)
		cdialog.buttonBox.accepted.connect(self.FontSettings)
		cdialog.buttonBox.accepted.connect(self.ShowLineNumbering)
		cdialog.buttonBox.accepted.connect(self.ShowStatusBar)
		cdialog.buttonBox.accepted.connect(self.SetTabWidth)
		cdialog.buttonBox.accepted.connect(self.SpaceInsted)
		cdialog.buttonBox.rejected.connect(self.ClassicStyle)   

	def ClassicStyle(self):
		fontsize = cdialog.spinBox_2.value()
		fontsize = "font: "+ str(fontsize)+"pt;"
		classic = '''
		selection-background-color: rgba(191, 191, 191, 189);
		background: #272822; color: rgb(255, 255, 255);'''
		classic = classic + fontsize
		self.lineTextEdit.setStyleSheet(classic)
		self.plainTextEdit.setStyleSheet(classic)
		self.BuildTextEdit.setStyleSheet(classic)
		#self.statusbar.setStyleSheet('''
		#selection-background-color: rgba(191, 191, 191, 189);
		#color: rgb(255, 255, 255);background: #555555;''')

	def CallSettings(self):
		position = self.plainTextEdit.verticalScrollBar().sliderPosition() #scroll-bar position reset on last session
		self.lineTextEdit.verticalScrollBar().setSliderPosition(position)
		cdialog.SaveSettings()

	def ShowLineNumbering(self):
		if(cdialog.checkBox.isChecked()):
			self.lineTextEdit.show()
		else:
			self.lineTextEdit.hide()

	def ShowStatusBar(self):
		if(cdialog.checkBox_2.isChecked()):
			self.statusbar.show()
		else:
			self.statusbar.hide() 

	#-------- Needs adjustment -------- 
	def SetTabWidth(self):
		check = cdialog.horizontalSlider.value()
		self.plainTextEdit.setTabStopWidth(check*10)

	def SpaceInsted(self):
		if(cdialog.checkBox_4.isChecked()):
			self.plainTextEdit.setTabStopWidth(10)
		else:
			check = cdialog.horizontalSlider.value()
			self.plainTextEdit.setTabStopWidth(check*10)
	#-------------------------------------------   

	def FontSettings(self):    
		fontsize = cdialog.spinBox_2.value()
		fontsize = "font: "+ str(fontsize)+"pt;"
		classic = '''
		selection-background-color: rgba(191, 191, 191, 189);
		background: #272822; color: rgb(255, 255, 255);'''
		oblivion = '''
		selection-background-color: rgba(191, 191, 191, 189);
		background: #2E3436 ;color: rgb(255, 255, 255);'''
		cobalt = '''
		selection-background-color: rgba(191, 191, 191, 189);
		background: #001B33; color: rgb(255, 255, 255);'''
		SolorizedL ='''
		selection-background-color: rgba(191, 191, 191, 189);
		background: #FDF6E3; color: rgb(0, 0, 0);'''
		SolorizedD ='''
		selection-background-color: rgba(191, 191, 191, 189);
		background: #002B36; color: rgb(255, 255, 255);'''
		Azura = '''
		selection-background-color: rgba(191, 191, 191, 189);
		background: #181D26; color: rgb(255, 255, 255);'''

		if(cdialog.listWidget.currentRow() == 0):
			classic = classic + fontsize
			self.lineTextEdit.setStyleSheet(classic)
			self.plainTextEdit.setStyleSheet(classic)
		elif(cdialog.listWidget.currentRow() == 1):
			oblivion = oblivion + fontsize
			self.lineTextEdit.setStyleSheet(oblivion)
			self.plainTextEdit.setStyleSheet(oblivion)
		elif(cdialog.listWidget.currentRow() == 2):
			cobalt = cobalt + fontsize
			self.lineTextEdit.setStyleSheet(cobalt)
			self.plainTextEdit.setStyleSheet(cobalt)
		elif(cdialog.listWidget.currentRow() == 3):
			SolorizedL = SolorizedL + fontsize
			self.lineTextEdit.setStyleSheet(SolorizedL)
			self.plainTextEdit.setStyleSheet(SolorizedL)
		elif(cdialog.listWidget.currentRow() == 4):
			SolorizedD = SolorizedD + fontsize
			self.lineTextEdit.setStyleSheet(SolorizedD)
			self.plainTextEdit.setStyleSheet(SolorizedD)
		elif(cdialog.listWidget.currentRow() == 5):
			Azura = Azura + fontsize
			self.lineTextEdit.setStyleSheet(Azura)
			self.plainTextEdit.setStyleSheet(Azura)
		
	def SyncScrollBar(self):
		position = self.plainTextEdit.verticalScrollBar().sliderPosition()
		self.lineTextEdit.verticalScrollBar().setValue(position)

	def HighlightLine(self):
		if(cdialog.checkBox_5.isChecked()):
			extraSelections = []   
			selection = QtWidgets.QTextEdit.ExtraSelection()
			lineColor = QtGui.QColor(191, 191, 191, 189)

			selection.format.setBackground(lineColor)
			selection.format.setProperty(QtGui.QTextFormat.FullWidthSelection, QtCore.QVariant(True))
			selection.cursor = self.lineTextEdit.textCursor()
			selection.cursor.clearSelection()
			extraSelections.append(selection)

			self.lineTextEdit.setExtraSelections(extraSelections)
			#self.plainTextEdit.textCursor().blockNumber()+1
		else:
			empty = []
			selection = QtWidgets.QTextEdit.ExtraSelection()
			empty.append(selection)
			self.lineTextEdit.setExtraSelections(empty)

	#---- Algorithm for printing line numbers ----
	def LineNumberArea(self):  
		self.SyntaxHighlight()
		text = self.plainTextEdit.toPlainText()
		count = 1+sum(item.count('\n') for item in text)

		if(count > int(self.i)):
			while(count > int(self.i)):
				self.i = (int(self.i)+1) 
				self.lineTextEdit.appendPlainText(str(self.i))        
		elif(int(count) < int(self.i)):
			while(count < int(self.i)):
				self.i = (int(self.i)-1) 
				self.lineTextEdit.setFocus()
				self.lineTextEdit.moveCursor(QtGui.QTextCursor.End,QtGui.QTextCursor.MoveAnchor)
				self.lineTextEdit.moveCursor(QtGui.QTextCursor.StartOfLine,QtGui.QTextCursor.MoveAnchor)
				self.lineTextEdit.moveCursor(QtGui.QTextCursor.End,QtGui.QTextCursor.KeepAnchor)
				self.lineTextEdit.textCursor().removeSelectedText()
				self.lineTextEdit.textCursor().deletePreviousChar()

		self.plainTextEdit.setFocus()

	def SyntaxHighlight(self):
		extraSelections = []
		resetscroll = self.plainTextEdit.verticalScrollBar().sliderPosition()
		reset = self.plainTextEdit.textCursor()
		basictypes = ["int","float","char","double",
		"long","short","void","struct"
		]

		for item in basictypes:
			word=item
			self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start)
			while(self.plainTextEdit.find(word,QtGui.QTextDocument.FindWholeWords)): 
				cursor = self.plainTextEdit.textCursor()       
				currentWord = QtWidgets.QTextEdit.ExtraSelection()
				blueColor = QtGui.QColor("lightblue")
				currentWord.format.setForeground(blueColor)
				currentWord.cursor = cursor
				extraSelections.append(currentWord)
		
			self.plainTextEdit.setExtraSelections(extraSelections)
			self.plainTextEdit.setTextCursor(reset)  
		
		controltypes = ["if","else","while",
		"do","for","return"
		]

		for item in controltypes:
			word=item
			self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start)
			while(self.plainTextEdit.find(word,QtGui.QTextDocument.FindWholeWords)): 
				cursor = self.plainTextEdit.textCursor()       
				currentWord = QtWidgets.QTextEdit.ExtraSelection()
				redColor = QtGui.QColor("red")
				currentWord.format.setForeground(redColor)
				currentWord.cursor = cursor
				extraSelections.append(currentWord)
		
			self.plainTextEdit.setExtraSelections(extraSelections)
			self.plainTextEdit.setTextCursor(reset)  
		
		format_types = ["%s","%d","%f","%c",
		"%p","%lf","NULL"]

		for item in format_types:
			word=item
			self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start)
			while(self.plainTextEdit.find(word,QtGui.QTextDocument.FindWholeWords)): 
				cursor = self.plainTextEdit.textCursor()       
				currentWord = QtWidgets.QTextEdit.ExtraSelection()
				purpleColor = QtGui.QColor(208, 146, 255)
				currentWord.format.setForeground(purpleColor)
				currentWord.cursor = cursor
				extraSelections.append(currentWord)
		
			self.plainTextEdit.setExtraSelections(extraSelections)
			self.plainTextEdit.setTextCursor(reset)  

		'''
		self.plainTextEdit.moveCursor(QtGui.QTextCursor.Start) 
		try:
			
			self.plainTextEdit.moveCursor(self.plainTextEdit.find("/*"),QtGui.QTextCursor.MoveAnchor)			
			self.plainTextEdit.moveCursor(self.plainTextEdit.find("*/") ,QtGui.QTextCursor.KeepAnchor)
			
			

			
			cursor = self.plainTextEdit.textCursor()       
			currentWord = QtWidgets.QTextEdit.ExtraSelection()
			yellowColor = QtGui.QColor("yellow")
			currentWord.format.setForeground(yellowColor)
			currentWord.cursor = cursor
			
			extraSelections.append(currentWord)

		
		except:
			pass

		self.plainTextEdit.setExtraSelections(extraSelections)
		self.plainTextEdit.setTextCursor(reset)
		
		self.plainTextEdit.verticalScrollBar().setValue(resetscroll) 
		'''
	def LaunchOptions(self):
		if(cdialog.radioButton.isChecked()):
			cwindow.showFullScreen()
		elif(cdialog.radioButton_2.isChecked()):
			cwindow.showMaximized()
		elif(cdialog.radioButton_3.isChecked()):
			cwindow.showNormal() 

	def SetupSettings(self):
		self.LastSesion()
		self.LaunchOptions()
		self.CallSettings()
		self.FontSettings()
		self.ShowLineNumbering()
		self.ShowStatusBar()
		self.SetTabWidth()
		self.SpaceInsted()
		if(cdialog.checkBox_6.isChecked()):
			self.Autosave()  

	def LastSesion(self):
		if(cdialog.checkBox_3.isChecked()):
			try:
				f = open("Settings.txt","r")
				items = []
			
				for line in f:
					item = line.split("=")
					items.append(item[1].strip())

				self.statusbarLocationLabel.setText(items[12])
				f.close()
				filename = self.statusbarLocationLabel.text()
				f = open(filename, 'r')
				filedata = f.read()
				self.plainTextEdit.setPlainText(filedata)           
				f.close()
			except:
				pass         

	def Autosave(self):
		minutes = float(cdialog.spinBox.value())*60
		threading.Timer(minutes, self.Autosave).start()
		self.SaveFile()
	
	def ShowBuild(self):
		self.BuildTextEdit.show()
		old_location = os.getcwd() # Current working directory
		location = self.statusbarLocationLabel.text()

		if(location):
			start = location.rfind('/')
			name=location[start+1:]
			location = location[:start]
			os.chdir(location)
			self.SaveFile()
		else:
			self.SaveFileAs()
			start = location.rfind('/')
			name=location[start+1:]
			location = location[:start]
			os.chdir(location)
		
		output = name.find(".")
		output = name[:output]

		p = subprocess.Popen(["gcc",name,"-o",output],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdout = []
		stderr = []

		while (True): #object representing the string environment
			reads = [p.stderr.fileno()]		
			read = p.stderr.readline()
			read=read.decode(encoding='UTF-8')
			sys.stderr.write(read)
			stderr.append(read)

			if (p.poll() != None):
				break
		
		stderr=''.join(stderr)	
		self.BuildTextEdit.setPlainText(stderr)
		os.chdir(old_location)

	def Run(self):
					
		self.plainTextEdit.setExtraSelections(extraSelections)
		self.plainTextEdit.setTextCursor(reset)
		
		self.BuildTextEdit.show()
		old_location = os.getcwd() # Current working directory
		location = self.statusbarLocationLabel.text()
		start = location.rfind('/')		
		location = location[:start]
		os.chdir(location)		
		os.system('gnome-terminal')
		os.chdir(old_location)

	def ColorSheme(self):
		classic = '''
		font: 15pt; 
		selection-background-color: rgba(191, 191, 191, 189);
		background: #272822; color: rgb(255, 255, 255);'''
		oblivion = '''
		font: 15pt; 
		selection-background-color: rgba(191, 191, 191, 189);
		background: #2E3436 ;color: rgb(255, 255, 255);'''
		cobalt = '''
		font: 15pt; 
		selection-background-color: rgba(191, 191, 191, 189);
		background: #001B33; color: rgb(255, 255, 255);'''
		SolorizedL ='''
		font: 15pt; 
		selection-background-color: rgba(191, 191, 191, 189);
		background: #FDF6E3; color: rgb(0, 0, 0);'''
		SolorizedD ='''
		font: 15pt; 
		selection-background-color: rgba(191, 191, 191, 189);
		background: #002B36; color: rgb(255, 255, 255);'''
		Azura = '''
		font: 15pt; 
		selection-background-color: rgba(191, 191, 191, 189);
		background: #181D26; color: rgb(255, 255, 255);'''
		if(cdialog.listWidget.currentRow() == 0):
			self.lineTextEdit.setStyleSheet(classic)
			self.plainTextEdit.setStyleSheet(classic)
			self.BuildTextEdit.setStyleSheet(classic)
		elif(cdialog.listWidget.currentRow() == 1):
			self.lineTextEdit.setStyleSheet(oblivion)
			self.plainTextEdit.setStyleSheet(oblivion)
			self.BuildTextEdit.setStyleSheet(oblivion)
		elif(cdialog.listWidget.currentRow() == 2):
			self.lineTextEdit.setStyleSheet(cobalt)
			self.plainTextEdit.setStyleSheet(cobalt)
			self.BuildTextEdit.setStyleSheet(cobalt)
		elif(cdialog.listWidget.currentRow() == 3):
			self.lineTextEdit.setStyleSheet(SolorizedL)
			self.plainTextEdit.setStyleSheet(SolorizedL)
			self.BuildTextEdit.setStyleSheet(SolorizedL)
		elif(cdialog.listWidget.currentRow() == 4):
			self.lineTextEdit.setStyleSheet(SolorizedD)
			self.plainTextEdit.setStyleSheet(SolorizedD)
			self.BuildTextEdit.setStyleSheet(SolorizedD)
		elif(cdialog.listWidget.currentRow() == 5):
			self.lineTextEdit.setStyleSheet(Azura)
			self.plainTextEdit.setStyleSheet(Azura)
			self.BuildTextEdit.setStyleSheet(Azura)
	def ShowColumn(self):
		
		
		column = 'Column:' + str(self.plainTextEdit.textCursor().positionInBlock())
		self.statusbarColumnLabel.setText(column)

		line = 'Line:' + str(self.plainTextEdit.textCursor().blockNumber()+1)
		self.statusbarLineLabel.setText(line)
		

class CustomWindow(QtWidgets.QWidget):
	def __init__(self): 
		QtWidgets.QWidget.__init__(self)
		self.setupUi(self)
	def setupUi(self, CustomWindow):
		CustomWindow.setObjectName("CustomWindow")
		CustomWindow.resize(1000, 800)

		self.verticalLayout = QtWidgets.QVBoxLayout(self)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.verticalLayout.addWidget(titleBar)
		self.verticalLayout.addWidget(ceditor)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

			
#-------- M A I N --------
app = QtWidgets.QApplication(sys.argv)
#app.setStyleSheet("QStatusBar::item { border: 0px  }; ");
cdialog = Ui_Dialog()
ceditor = Ui_MainWindow()
titleBar = TitleBar()
cwindow = CustomWindow()
cdialog.LoadSettings()
ceditor.SetupSettings()
cwindow.show()
exit = app.exec_()
sys.exit(exit)
		