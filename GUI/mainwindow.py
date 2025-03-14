# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 501)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setBaseSize(QSize(0, 0))
        self.Open = QAction(MainWindow)
        self.Open.setObjectName(u"Open")
        self.Create = QAction(MainWindow)
        self.Create.setObjectName(u"Create")
        self.Save = QAction(MainWindow)
        self.Save.setObjectName(u"Save")
        self.Save_as = QAction(MainWindow)
        self.Save_as.setObjectName(u"Save_as")
        self.Close = QAction(MainWindow)
        self.Close.setObjectName(u"Close")
        self.Run_2 = QAction(MainWindow)
        self.Run_2.setObjectName(u"Run_2")
        self.Build = QAction(MainWindow)
        self.Build.setObjectName(u"Build")
        self.actionDebug = QAction(MainWindow)
        self.actionDebug.setObjectName(u"actionDebug")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setSizeIncrement(QSize(100, 100))
        self.centralwidget.setBaseSize(QSize(791, 501))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Frame = QFrame(self.centralwidget)
        self.Frame.setObjectName(u"Frame")
        self.Frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Frame.sizePolicy().hasHeightForWidth())
        self.Frame.setSizePolicy(sizePolicy1)
        self.Frame.setMinimumSize(QSize(700, 400))
        self.Frame.setMaximumSize(QSize(1920, 1080))
        self.Frame.setSizeIncrement(QSize(0, 0))
        self.Frame.setBaseSize(QSize(0, 0))
        self.Frame.setAutoFillBackground(True)
        self.Frame.setStyleSheet(u"")
        self.Frame.setFrameShape(QFrame.NoFrame)
        self.Frame.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.Frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.Frame)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(785, 38))
        self.Header.setMaximumSize(QSize(16777215, 38))
        self.Header.setStyleSheet(u"#verticalFrame{\n"
"background-color: white;\n"
"border-bottom: 1px solid rgb(169, 172, 172);\n"
"}")
        self.Header.setFrameShape(QFrame.NoFrame)
        self.Header.setLineWidth(1)
        self.Vertical_items = QVBoxLayout(self.Header)
        self.Vertical_items.setObjectName(u"Vertical_items")
        self.Vertical_items.setContentsMargins(0, 0, 0, 0)
        self.Debug_3 = QFrame(self.Header)
        self.Debug_3.setObjectName(u"Debug_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Debug_3.sizePolicy().hasHeightForWidth())
        self.Debug_3.setSizePolicy(sizePolicy2)
        self.Debug_3.setMinimumSize(QSize(100, 36))
        self.Debug = QHBoxLayout(self.Debug_3)
        self.Debug.setObjectName(u"Debug")
        self.Debug.setContentsMargins(0, 1, 6, 0)
        self.Run = QPushButton(self.Debug_3)
        self.Run.setObjectName(u"Run")
        self.Run.setEnabled(True)
        self.Run.setMinimumSize(QSize(75, 25))
        font = QFont()
        font.setFamilies([u"Raleway"])
        self.Run.setFont(font)
        self.Run.setStyleSheet(u"QPushButton{\n"
"color: green;\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid red;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 1px solid red;\n"
"}")
        self.Run.setInputMethodHints(Qt.ImhNone)
        self.Run.setIconSize(QSize(32, 32))
        self.Run.setCheckable(False)
        self.Run.setAutoRepeatDelay(0)
        self.Run.setAutoRepeatInterval(0)
        self.Run.setAutoDefault(False)
        self.Run.setFlat(False)

        self.Debug.addWidget(self.Run)

        self.Stop = QPushButton(self.Debug_3)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setMinimumSize(QSize(75, 25))
        self.Stop.setFont(font)
        self.Stop.setStyleSheet(u"color: red;\n"
"border: 1px solid black;\n"
"border-radius: 5px")
        self.Stop.setIconSize(QSize(32, 32))

        self.Debug.addWidget(self.Stop)


        self.Vertical_items.addWidget(self.Debug_3, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.Header)

        self.Editor = QHBoxLayout()
        self.Editor.setSpacing(0)
        self.Editor.setObjectName(u"Editor")
        self.Stroke_numbers = QTextBrowser(self.Frame)
        self.Stroke_numbers.setObjectName(u"Stroke_numbers")
        self.Stroke_numbers.setMinimumSize(QSize(30, 0))
        self.Stroke_numbers.setMaximumSize(QSize(30, 16777215))
        self.Stroke_numbers.setFont(font)
        self.Stroke_numbers.setStyleSheet(u"background:white;\n"
"color: black;\n"
"border-right: 1px solid black;\n"
"\n"
"")

        self.Editor.addWidget(self.Stroke_numbers)

        self.Memory = QPlainTextEdit(self.Frame)
        self.Memory.setObjectName(u"Memory")
        self.Memory.setMinimumSize(QSize(50, 0))
        self.Memory.setMaximumSize(QSize(200, 16777215))
        self.Memory.setFont(font)
        self.Memory.setStyleSheet(u"background:white;\n"
"color: black;\n"
"border-right: 1px solid black;\n"
"")

        self.Editor.addWidget(self.Memory)

        self.Registers = QPlainTextEdit(self.Frame)
        self.Registers.setObjectName(u"Registers")
        self.Registers.setMinimumSize(QSize(50, 0))
        self.Registers.setMaximumSize(QSize(200, 16777215))
        self.Registers.setFont(font)
        self.Registers.setStyleSheet(u"background:white;\n"
"color: black;\n"
"border-right: 1px solid black;")

        self.Editor.addWidget(self.Registers)

        self.Code = QPlainTextEdit(self.Frame)
        self.Code.setObjectName(u"Code")
        self.Code.setFont(font)
        self.Code.setStyleSheet(u"background:white;\n"
"color: black;\n"
"")

        self.Editor.addWidget(self.Code)


        self.verticalLayout_2.addLayout(self.Editor)


        self.gridLayout.addWidget(self.Frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 791, 42))
        self.File = QMenu(self.menubar)
        self.File.setObjectName(u"File")
        self.Debug_2 = QMenu(self.menubar)
        self.Debug_2.setObjectName(u"Debug_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Debug_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.File.addAction(self.Open)
        self.File.addAction(self.Create)
        self.File.addAction(self.Save)
        self.File.addAction(self.Save_as)
        self.File.addAction(self.Close)
        self.Debug_2.addAction(self.Run_2)
        self.Debug_2.addAction(self.Build)
        self.Debug_2.addAction(self.actionDebug)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.Create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.Save_as.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.Close.setText(QCoreApplication.translate("MainWindow", u"\u0417\u044b\u043a\u0440\u044b\u0442\u044c", None))
        self.Run_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.Build.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0440\u043a\u0430", None))
        self.actionDebug.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.Run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Stroke_numbers.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Raleway'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">\u041d\u043e\u043c\u0435\u0440\u0430</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont';\">\u0441\u0442\u0440\u043e\u043a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'.AppleSystemUIFont';\"><br /></p></body></html>", None))
        self.Memory.setPlainText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043c\u044f\u0442\u044c\n"
"", None))
        self.Registers.setPlainText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u044b\n"
"", None))
        self.Code.setPlainText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0441\u0442\u0438\u043d\u0433\n"
"", None))
        self.File.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.Debug_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u0430\u0434\u043a\u0430", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

