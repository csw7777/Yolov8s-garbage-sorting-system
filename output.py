# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1264, 896)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon2/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#centralwidget {background-image: url(\"D:/lg/BaiduSyncdisk/project/person_code/project_self/pyqt/det/icon/background.jpg\");}\n"
"\n"
"")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(310, 22, 661, 61))
        self.label_title.setMinimumSize(QtCore.QSize(0, 0))
        self.label_title.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, 100, 698, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setAcceptDrops(True)
        self.frame.setToolTipDuration(-2)
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(20, 170, 891, 481))
        self.label_img.setStyleSheet("background-color: rgba(122, 135, 154, 150);\n"
"border-radius: 15px;\n"
"")
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("icon/zhutu2.png"))
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setWordWrap(False)
        self.label_img.setIndent(-1)
        self.label_img.setOpenExternalLinks(False)
        self.label_img.setObjectName("label_img")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(950, 730, 30, 30))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("icon/weizhi.png"))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(990, 736, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_xmin = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin.setGeometry(QtCore.QRect(950, 780, 71, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_xmin.setFont(font)
        self.label_xmin.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_xmin.setObjectName("label_xmin")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1120, 780, 71, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(950, 830, 71, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1120, 830, 71, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1160, 197, 50, 27))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("icon2/mubiaojiance.png"))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(1170, 240, 30, 30))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("icon2/mubiaogenzong.png"))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(940, 360, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(940, 570, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(2)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(1)
        self.frame_6.setMidLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(950, 395, 30, 30))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("icon/suoyoumubiao.png"))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1000, 390, 221, 31))
        self.comboBox.setStyleSheet("\n"
"QComboBox {\n"
"    background-color: rgb(98, 105, 111);\n"
"    color: rgb(151, 155, 158);\n"
"    font-size: 14px; /* 设置字体大小为12像素 */\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(1020, 450, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("background-color: rgb(58,146,254);\n"
"\n"
"border-radius: 15px;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_start.setObjectName("pushButton_start")
        self.label_xmin_v = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin_v.setGeometry(QtCore.QRect(1020, 780, 51, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_xmin_v.setFont(font)
        self.label_xmin_v.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_xmin_v.setObjectName("label_xmin_v")
        self.label_xmax_v = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax_v.setGeometry(QtCore.QRect(1020, 830, 51, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_xmax_v.setFont(font)
        self.label_xmax_v.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_xmax_v.setObjectName("label_xmax_v")
        self.label_ymin_v = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin_v.setGeometry(QtCore.QRect(1190, 780, 51, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_ymin_v.setFont(font)
        self.label_ymin_v.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_ymin_v.setObjectName("label_ymin_v")
        self.label_ymax_v = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax_v.setGeometry(QtCore.QRect(1190, 830, 51, 27))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_ymax_v.setFont(font)
        self.label_ymax_v.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_ymax_v.setObjectName("label_ymax_v")
        self.label_score = QtWidgets.QLabel(self.centralwidget)
        self.label_score.setGeometry(QtCore.QRect(1120, 610, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_score.setFont(font)
        self.label_score.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_score.setText("")
        self.label_score.setObjectName("label_score")
        self.label_classes = QtWidgets.QLabel(self.centralwidget)
        self.label_classes.setGeometry(QtCore.QRect(800, 690, 41, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_classes.setFont(font)
        self.label_classes.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_classes.setText("")
        self.label_classes.setObjectName("label_classes")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 120, 255, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(29)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_csdn = QtWidgets.QLabel(self.layoutWidget)
        self.label_csdn.setText("")
        self.label_csdn.setPixmap(QtGui.QPixmap("icon/CSDN.png"))
        self.label_csdn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_csdn.setObjectName("label_csdn")
        self.horizontalLayout.addWidget(self.label_csdn)
        self.label_mbd = QtWidgets.QLabel(self.layoutWidget)
        self.label_mbd.setText("")
        self.label_mbd.setPixmap(QtGui.QPixmap("icon/mianbaoduo.png"))
        self.label_mbd.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mbd.setObjectName("label_mbd")
        self.horizontalLayout.addWidget(self.label_mbd)
        self.label_tb = QtWidgets.QLabel(self.layoutWidget)
        self.label_tb.setText("")
        self.label_tb.setPixmap(QtGui.QPixmap("icon/taobao.png"))
        self.label_tb.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tb.setObjectName("label_tb")
        self.horizontalLayout.addWidget(self.label_tb)
        self.label_img_path = QtWidgets.QLabel(self.centralwidget)
        self.label_img_path.setGeometry(QtCore.QRect(1000, 190, 221, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_img_path.setFont(font)
        self.label_img_path.setToolTipDuration(-1)
        self.label_img_path.setStyleSheet("background-color: rgb(98, 105, 111);\n"
"\n"
"border-radius: 7px;\n"
"\n"
"color: rgb(151, 155, 158);")
        self.label_img_path.setTextFormat(QtCore.Qt.AutoText)
        self.label_img_path.setObjectName("label_img_path")
        self.pushButton_img = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_img.setGeometry(QtCore.QRect(940, 180, 45, 45))
        self.pushButton_img.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 10px; /* 设置圆角半径为10像素 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(98, 105, 111);\n"
"}")
        self.pushButton_img.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/dirs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_img.setIcon(icon1)
        self.pushButton_img.setIconSize(QtCore.QSize(40, 27))
        self.pushButton_img.setObjectName("pushButton_img")
        self.pushButton_dir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dir.setGeometry(QtCore.QRect(940, 242, 45, 45))
        self.pushButton_dir.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 10px; /* 设置圆角半径为10像素 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(98, 105, 111);\n"
"}")
        self.pushButton_dir.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/dir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dir.setIcon(icon2)
        self.pushButton_dir.setIconSize(QtCore.QSize(40, 27))
        self.pushButton_dir.setObjectName("pushButton_dir")
        self.label_dir_path = QtWidgets.QLabel(self.centralwidget)
        self.label_dir_path.setGeometry(QtCore.QRect(1000, 250, 221, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_dir_path.setFont(font)
        self.label_dir_path.setToolTipDuration(-1)
        self.label_dir_path.setStyleSheet("background-color: rgb(98, 105, 111);\n"
"\n"
"border-radius: 7px;\n"
"\n"
"color: rgb(151, 155, 158);\n"
"\n"
"QLabel {\n"
"    padding-left: 10px; /* 设置左边距为10像素 */\n"
"}")
        self.label_dir_path.setTextFormat(QtCore.Qt.AutoText)
        self.label_dir_path.setObjectName("label_dir_path")
        self.pushButton_video = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_video.setGeometry(QtCore.QRect(940, 300, 45, 45))
        self.pushButton_video.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 10px; /* 设置圆角半径为10像素 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(98, 105, 111);\n"
"}")
        self.pushButton_video.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/shipinwenjian.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_video.setIcon(icon3)
        self.pushButton_video.setIconSize(QtCore.QSize(40, 27))
        self.pushButton_video.setObjectName("pushButton_video")
        self.label_video_path = QtWidgets.QLabel(self.centralwidget)
        self.label_video_path.setGeometry(QtCore.QRect(1000, 308, 221, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_video_path.setFont(font)
        self.label_video_path.setToolTipDuration(-1)
        self.label_video_path.setStyleSheet("background-color: rgb(98, 105, 111);\n"
"\n"
"border-radius: 7px;\n"
"\n"
"color: rgb(151, 155, 158);\n"
"\n"
"QLabel {\n"
"    padding-left: 10px; /* 设置左边距为10像素 */\n"
"}")
        self.label_video_path.setTextFormat(QtCore.Qt.AutoText)
        self.label_video_path.setObjectName("label_video_path")
        self.pushButton_export = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export.setGeometry(QtCore.QRect(1020, 510, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_export.setFont(font)
        self.pushButton_export.setStyleSheet("background-color: rgb(58,146,254);\n"
"\n"
"border-radius: 15px;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_export.setObjectName("pushButton_export")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(950, 675, 30, 30))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("icon/leibie.png"))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(990, 675, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(989, 605, 111, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(950, 610, 29, 34))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("icon/zhixindu.png"))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.tableWidget_info = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_info.setGeometry(QtCore.QRect(20, 670, 891, 211))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.tableWidget_info.setFont(font)
        self.tableWidget_info.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(93, 98, 194);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(54, 63, 70);\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover{\n"
"    background-color:rgb(152,155,232);\n"
"}\n"
"QTableView::item:selected{\n"
"    background-color:rgb(255,249,150);\n"
"}\n"
"QTableView::item:selected:!active{\n"
"    background-color:#f0f0f2;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget_info.setLineWidth(0)
        self.tableWidget_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_info.setAutoScroll(False)
        self.tableWidget_info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_info.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_info.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_info.setShowGrid(True)
        self.tableWidget_info.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget_info.setWordWrap(True)
        self.tableWidget_info.setCornerButtonEnabled(True)
        self.tableWidget_info.setRowCount(6)
        self.tableWidget_info.setColumnCount(7)
        self.tableWidget_info.setObjectName("tableWidget_info")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(6, item)
        self.tableWidget_info.horizontalHeader().setVisible(True)
        self.tableWidget_info.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_info.horizontalHeader().setDefaultSectionSize(128)
        self.tableWidget_info.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_info.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_info.verticalHeader().setVisible(False)
        self.tableWidget_info.verticalHeader().setCascadingSectionResizes(False)
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setGeometry(QtCore.QRect(1120, 670, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_class.setFont(font)
        self.label_class.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_class.setText("")
        self.label_class.setObjectName("label_class")
        self.label_control = QtWidgets.QLabel(self.centralwidget)
        self.label_control.setGeometry(QtCore.QRect(927, 170, 321, 711))
        self.label_control.setStyleSheet("background-color: rgba(122, 135, 154, 100);\n"
"border-radius: 15px;\n"
"")
        self.label_control.setText("")
        self.label_control.setObjectName("label_control")
        self.label_control.raise_()
        self.label_title.raise_()
        self.frame.raise_()
        self.label_img.raise_()
        self.label_17.raise_()
        self.label_9.raise_()
        self.label_xmin.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.frame_3.raise_()
        self.frame_6.raise_()
        self.label_25.raise_()
        self.comboBox.raise_()
        self.pushButton_start.raise_()
        self.label_xmin_v.raise_()
        self.label_xmax_v.raise_()
        self.label_ymin_v.raise_()
        self.label_ymax_v.raise_()
        self.label_score.raise_()
        self.label_classes.raise_()
        self.layoutWidget.raise_()
        self.label_img_path.raise_()
        self.pushButton_img.raise_()
        self.pushButton_dir.raise_()
        self.label_dir_path.raise_()
        self.pushButton_video.raise_()
        self.label_video_path.raise_()
        self.pushButton_export.raise_()
        self.label_15.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_14.raise_()
        self.tableWidget_info.raise_()
        self.label_class.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "钢铁表面缺陷检测系统"))
        MainWindow.setProperty("setWindowFlags", _translate("MainWindow", "QtCore.Qt.FramelessWindowHint"))
        MainWindow.setProperty("setAttribute", _translate("MainWindow", "QtCore.Qt.WA_TranslucentBackground"))
        self.label_title.setText(_translate("MainWindow", "钢铁表面缺陷检测系统"))
        self.label_9.setText(_translate("MainWindow", "位置:"))
        self.label_xmin.setText(_translate("MainWindow", "xmin: "))
        self.label_19.setText(_translate("MainWindow", "ymin:"))
        self.label_20.setText(_translate("MainWindow", "xmax:"))
        self.label_21.setText(_translate("MainWindow", "ymax:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "所有目标"))
        self.pushButton_start.setText(_translate("MainWindow", "开始运行 >"))
        self.label_xmin_v.setText(_translate("MainWindow", "0"))
        self.label_xmax_v.setText(_translate("MainWindow", "0"))
        self.label_ymin_v.setText(_translate("MainWindow", "0"))
        self.label_ymax_v.setText(_translate("MainWindow", "0"))
        self.label_img_path.setText(_translate("MainWindow", " 选择图片文件"))
        self.label_dir_path.setText(_translate("MainWindow", " 选择图片文件夹"))
        self.label_video_path.setText(_translate("MainWindow", " 选择视频文件"))
        self.pushButton_export.setText(_translate("MainWindow", "导出数据 >"))
        self.label_7.setText(_translate("MainWindow", "类别:"))
        self.label_6.setText(_translate("MainWindow", "置信度:"))
        self.tableWidget_info.setSortingEnabled(False)
        self.tableWidget_info.setProperty("sectionResizeMode", _translate("MainWindow", "QHeaderView::ResizeToContents"))
        item = self.tableWidget_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "图片名称"))
        item = self.tableWidget_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "录入时间"))
        item = self.tableWidget_info.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "识别结果"))
        item = self.tableWidget_info.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "目标数目"))
        item = self.tableWidget_info.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "用时"))
        item = self.tableWidget_info.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "保存路径"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
