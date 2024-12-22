# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        MainWindow.setToolTipDuration(-2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setToolTipDuration(-2)
        self.centralwidget.setStyleSheet(u"background-color: none;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setMinimumSize(QSize(150, 0))
        self.sidebar.setMaximumSize(QSize(150, 16777215))
        self.sidebar.setStyleSheet(u"border-radius: 0;\n"
"background-color: rgb(50, 66, 79);")
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 10, 8, 0)
        self.pushButton = QPushButton(self.sidebar)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(10)
        font.setWeight(QFont.Black)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"padding: 5px;")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.sidebar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"padding: 5px;")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.sidebar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"padding: 5px;")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #20272C;")
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.page_main.setStyleSheet(u"background-color: #20272C;")
        self.verticalLayout_2 = QVBoxLayout(self.page_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.page_main)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setToolTipDuration(-2)
        self.frame_23.setStyleSheet(u"background: none;")
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_23)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 20, -1, -1)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_24)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Intro Black"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"background-color: #32424F;\n"
"border-radius: 5px;\n"
"padding: 8px 15px;")
        self.pushButton_6.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.pushButton_6)

        self.lineEdit_3 = QLineEdit(self.frame_24)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setStyleSheet(u"background-color: #32424F;\n"
"border-radius: 5px;\n"
"padding: 8px 15px;")

        self.horizontalLayout_12.addWidget(self.lineEdit_3)


        self.verticalLayout_15.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.comboBox_3 = QComboBox(self.frame_25)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(250, 0))
        self.comboBox_3.setMaximumSize(QSize(250, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.comboBox_3.setFont(font3)
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"	background-color: #32424F;\n"
"	border-radius: 5px;\n"
"	padding: 8px 15px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: #373e4e;\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.comboBox_3)

        self.horizontalSpacer_15 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.verticalLayout_15.addWidget(self.frame_25)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)


        self.verticalLayout_2.addWidget(self.frame_23)

        self.frame_10 = QFrame(self.page_main)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 200))
        self.frame_10.setStyleSheet(u"background-color: none;")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.frame_19 = QFrame(self.frame_10)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(500, 110))
        self.frame_20.setMaximumSize(QSize(500, 110))
        self.frame_20.setStyleSheet(u"background: #32424F;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: none;")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_21)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_stage_3 = QLabel(self.frame_21)
        self.label_stage_3.setObjectName(u"label_stage_3")
        self.label_stage_3.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setFamilies([u"JetBrains Mono"])
        font4.setPointSize(12)
        font4.setItalic(False)
        self.label_stage_3.setFont(font4)
        self.label_stage_3.setStyleSheet(u"")
        self.label_stage_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_stage_3)

        self.label_specific_stage_3 = QLabel(self.frame_21)
        self.label_specific_stage_3.setObjectName(u"label_specific_stage_3")
        self.label_specific_stage_3.setMinimumSize(QSize(150, 0))
        font5 = QFont()
        font5.setFamilies([u"JetBrains Mono"])
        font5.setPointSize(10)
        font5.setItalic(False)
        self.label_specific_stage_3.setFont(font5)
        self.label_specific_stage_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_specific_stage_3)


        self.verticalLayout_13.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_12 = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.progressBar_stage = QProgressBar(self.frame_22)
        self.progressBar_stage.setObjectName(u"progressBar_stage")
        self.progressBar_stage.setMinimumSize(QSize(440, 0))
        self.progressBar_stage.setMaximumSize(QSize(440, 16777215))
        self.progressBar_stage.setStyleSheet(u"#progressBar_stage{\n"
"	background-color: #ffffff;\n"
"	padding: 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#progressBar_stage::chunk{\n"
"	background-color: #29D37E;\n"
"	padding: 0;\n"
"	border-radius: 5px;\n"
"}")
        self.progressBar_stage.setValue(24)
        self.progressBar_stage.setTextVisible(False)

        self.horizontalLayout_11.addWidget(self.progressBar_stage)

        self.horizontalSpacer_13 = QSpacerItem(3, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_13.addWidget(self.frame_22)


        self.verticalLayout_12.addWidget(self.frame_20, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.frame_19)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_main)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.stackedWidget.addWidget(self.page_settings)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_6.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439", None))

#if QT_CONFIG(tooltip)
        self.comboBox_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0420\u0435\u0436\u0438\u043c \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0433\u043e \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.comboBox_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.label_stage_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u042d\u0442\u0430\u043f \u0440\u0430\u0431\u043e\u0442\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_stage_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_stage_3.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0442\u0430\u043f \u0440\u0430\u0431\u043e\u0442\u044b", None))
#if QT_CONFIG(tooltip)
        self.label_specific_stage_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">\u041a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0440\u0430\u0431\u043e\u0442\u044b</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_specific_stage_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043c\u0435\u043d\u0442 \u0440\u0430\u0431\u043e\u0442\u044b", None))
#if QT_CONFIG(tooltip)
        self.progressBar_stage.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

