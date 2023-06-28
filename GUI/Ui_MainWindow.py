# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Desktop\工具开发\Inkjet_Printing_System\GUI\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 742)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_show1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_show1.setMinimumSize(QtCore.QSize(500, 300))
        self.frame_show1.setAutoFillBackground(False)
        self.frame_show1.setStyleSheet("QFrame {background-color:rgb(198, 227, 255);}")
        self.frame_show1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_show1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_show1.setObjectName("frame_show1")
        self.PathDisplay = QtWidgets.QVBoxLayout(self.frame_show1)
        self.PathDisplay.setObjectName("PathDisplay")
        self.label = QtWidgets.QLabel(self.frame_show1)
        self.label.setObjectName("label")
        self.PathDisplay.addWidget(self.label)
        self.gridLayout.addWidget(self.frame_show1, 0, 1, 1, 1)
        self.frame_show2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_show2.setMinimumSize(QtCore.QSize(500, 200))
        self.frame_show2.setStyleSheet("QFrame {background-color:rgb(255, 255, 255);}")
        self.frame_show2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_show2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_show2.setObjectName("frame_show2")
        self.WaveformDisplay = QtWidgets.QVBoxLayout(self.frame_show2)
        self.WaveformDisplay.setObjectName("WaveformDisplay")
        self.label_2 = QtWidgets.QLabel(self.frame_show2)
        self.label_2.setObjectName("label_2")
        self.WaveformDisplay.addWidget(self.label_2)
        self.graphicsView_WaveformDisplay = QtWidgets.QGraphicsView(self.frame_show2)
        self.graphicsView_WaveformDisplay.setObjectName("graphicsView_WaveformDisplay")
        self.WaveformDisplay.addWidget(self.graphicsView_WaveformDisplay)
        self.gridLayout.addWidget(self.frame_show2, 1, 1, 1, 1)
        self.frame_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu.setMinimumSize(QtCore.QSize(200, 200))
        self.frame_menu.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_menu.setAutoFillBackground(False)
        self.frame_menu.setStyleSheet("QFrame {background-color:rgb(227, 227, 227);}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.Menu = QtWidgets.QGridLayout(self.frame_menu)
        self.Menu.setContentsMargins(-1, 9, 9, -1)
        self.Menu.setVerticalSpacing(15)
        self.Menu.setObjectName("Menu")
        self.Button_FileRead = QtWidgets.QPushButton(self.frame_menu)
        self.Button_FileRead.setMouseTracking(False)
        self.Button_FileRead.setStyleSheet("")
        self.Button_FileRead.setObjectName("Button_FileRead")
        self.Menu.addWidget(self.Button_FileRead, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.Menu.addItem(spacerItem, 7, 0, 1, 1)
        self.Button_Quit = QtWidgets.QPushButton(self.frame_menu)
        self.Button_Quit.setObjectName("Button_Quit")
        self.Menu.addWidget(self.Button_Quit, 6, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_menu)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Menu.addWidget(self.line, 4, 0, 1, 2)
        self.Button_InkjetSetting = QtWidgets.QPushButton(self.frame_menu)
        self.Button_InkjetSetting.setObjectName("Button_InkjetSetting")
        self.Menu.addWidget(self.Button_InkjetSetting, 3, 0, 1, 2)
        self.Button_TrajectoryPreview = QtWidgets.QPushButton(self.frame_menu)
        self.Button_TrajectoryPreview.setEnabled(False)
        self.Button_TrajectoryPreview.setCheckable(False)
        self.Button_TrajectoryPreview.setChecked(False)
        self.Button_TrajectoryPreview.setAutoRepeat(False)
        self.Button_TrajectoryPreview.setAutoExclusive(False)
        self.Button_TrajectoryPreview.setAutoDefault(False)
        self.Button_TrajectoryPreview.setDefault(False)
        self.Button_TrajectoryPreview.setFlat(False)
        self.Button_TrajectoryPreview.setObjectName("Button_TrajectoryPreview")
        self.Menu.addWidget(self.Button_TrajectoryPreview, 2, 0, 1, 2)
        self.Button_FileExport = QtWidgets.QPushButton(self.frame_menu)
        self.Button_FileExport.setEnabled(False)
        self.Button_FileExport.setObjectName("Button_FileExport")
        self.Menu.addWidget(self.Button_FileExport, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 120, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.Menu.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Menu.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_menu, 0, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D喷墨打印系统"))
        self.label.setText(_translate("MainWindow", "轨迹显示："))
        self.label_2.setText(_translate("MainWindow", "波形显示："))
        self.Button_FileRead.setText(_translate("MainWindow", "读取文件"))
        self.Button_Quit.setText(_translate("MainWindow", "退出"))
        self.Button_InkjetSetting.setText(_translate("MainWindow", "喷墨设置"))
        self.Button_TrajectoryPreview.setText(_translate("MainWindow", "轨迹预览"))
        self.Button_FileExport.setText(_translate("MainWindow", "导出"))
