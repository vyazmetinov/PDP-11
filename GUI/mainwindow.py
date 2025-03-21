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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 586)
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
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action.setCheckable(True)
        self.action.setChecked(True)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_2.setCheckable(True)
        self.action_2.setChecked(True)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_3.setCheckable(True)
        self.action_3.setChecked(True)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 990, 42))
        self.File = QMenu(self.menubar)
        self.File.setObjectName(u"File")
        self.Debug_2 = QMenu(self.menubar)
        self.Debug_2.setObjectName(u"Debug_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.registers = QDockWidget(MainWindow)
        self.registers.setObjectName(u"registers")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.registers.sizePolicy().hasHeightForWidth())
        self.registers.setSizePolicy(sizePolicy1)
        self.registers.setMinimumSize(QSize(62, 62))
        self.registers.setMaximumSize(QSize(524287, 524287))
        self.registers.setStyleSheet(u"")
        self.dockWidgetContents_7 = QWidget()
        self.dockWidgetContents_7.setObjectName(u"dockWidgetContents_7")
        self.reg_frame = QFrame(self.dockWidgetContents_7)
        self.reg_frame.setObjectName(u"reg_frame")
        self.reg_frame.setGeometry(QRect(0, 0, 1920, 1080))
        self.reg_frame.setMinimumSize(QSize(1920, 1080))
        self.reg_frame.setStyleSheet(u"#reg_frame{\n"
"background-color: white;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.reg_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.reg_item = QFrame(self.reg_frame)
        self.reg_item.setObjectName(u"reg_item")
        self.reg_item.setMaximumSize(QSize(16777215, 60))
        self.reg_item.setFrameShape(QFrame.Box)
        self.horizontalLayout_5 = QHBoxLayout(self.reg_item)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.reg = QLabel(self.reg_item)
        self.reg.setObjectName(u"reg")
        self.reg.setFrameShape(QFrame.Box)
        self.reg.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.reg)

        self.value = QTextBrowser(self.reg_item)
        self.value.setObjectName(u"value")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.value.sizePolicy().hasHeightForWidth())
        self.value.setSizePolicy(sizePolicy2)
        self.value.setMinimumSize(QSize(1920, 0))
        self.value.setFrameShape(QFrame.Box)
        self.value.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_5.addWidget(self.value)


        self.verticalLayout_3.addWidget(self.reg_item, 0, Qt.AlignTop)

        self.registers.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.registers)
        self.code = QDockWidget(MainWindow)
        self.code.setObjectName(u"code")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.code.sizePolicy().hasHeightForWidth())
        self.code.setSizePolicy(sizePolicy3)
        self.code.setBaseSize(QSize(500, 0))
        self.dockWidgetContents_10 = QWidget()
        self.dockWidgetContents_10.setObjectName(u"dockWidgetContents_10")
        self.code_frame = QFrame(self.dockWidgetContents_10)
        self.code_frame.setObjectName(u"code_frame")
        self.code_frame.setGeometry(QRect(-1, -1, 1920, 1080))
        self.code_frame.setMinimumSize(QSize(1920, 1080))
        self.code_frame.setStyleSheet(u"background-color: white;")
        self.code_frame.setFrameShape(QFrame.StyledPanel)
        self.code_frame.setFrameShadow(QFrame.Raised)
        self.code_item = QFrame(self.code_frame)
        self.code_item.setObjectName(u"code_item")
        self.code_item.setEnabled(True)
        self.code_item.setGeometry(QRect(0, 0, 1920, 1080))
        self.code_item.setMinimumSize(QSize(1920, 1080))
        self.code_item.setStyleSheet(u"#reg_frame{\n"
"background-color: white;\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.code_item)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.code_line = QFrame(self.code_item)
        self.code_line.setObjectName(u"code_line")
        self.code_line.setMaximumSize(QSize(1000000, 60))
        self.code_line.setFrameShape(QFrame.Box)
        self.horizontalLayout_9 = QHBoxLayout(self.code_line)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.line_id = QLabel(self.code_line)
        self.line_id.setObjectName(u"line_id")
        self.line_id.setEnabled(True)
        self.line_id.setFrameShape(QFrame.Box)
        self.line_id.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_9.addWidget(self.line_id)

        self.line = QTextEdit(self.code_line)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Box)
        self.line.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_9.addWidget(self.line)


        self.verticalLayout_6.addWidget(self.code_line, 0, Qt.AlignTop)

        self.code.setWidget(self.dockWidgetContents_10)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.code)
        self.header_2 = QDockWidget(MainWindow)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setMinimumSize(QSize(200, 80))
        self.dockWidgetContents_11 = QWidget()
        self.dockWidgetContents_11.setObjectName(u"dockWidgetContents_11")
        self.header_frame = QFrame(self.dockWidgetContents_11)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setGeometry(QRect(-20, 0, 1001, 80))
        self.header_frame.setMinimumSize(QSize(0, 80))
        self.header_frame.setStyleSheet(u"#header_2{\n"
"background-color: white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_item = QFrame(self.header_frame)
        self.header_item.setObjectName(u"header_item")
        self.header_item.setFrameShape(QFrame.NoFrame)
        self.header_item.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_item)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stop = QPushButton(self.header_item)
        self.stop.setObjectName(u"stop")
        self.stop.setMaximumSize(QSize(60, 40))
        icon = QIcon()
        icon.addFile(u":/icons/icons/crop_5_4.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.stop)

        self.run = QPushButton(self.header_item)
        self.run.setObjectName(u"run")
        self.run.setMaximumSize(QSize(60, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/play_arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.run.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.run)


        self.horizontalLayout_2.addWidget(self.header_item, 0, Qt.AlignRight|Qt.AlignTop)

        self.header_2.setWidget(self.dockWidgetContents_11)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.header_2)

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Debug_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.File.addAction(self.Open)
        self.File.addAction(self.Create)
        self.File.addAction(self.Save)
        self.File.addAction(self.Save_as)
        self.File.addAction(self.Close)
        self.Debug_2.addAction(self.Run_2)
        self.Debug_2.addAction(self.Build)
        self.Debug_2.addAction(self.actionDebug)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)

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
        self.actionDebug.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u0430\u0434\u043a\u0430", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u044b", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.File.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.Debug_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u0430\u0434\u043a\u0430", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u0430\u0434\u043a\u0438", None))
        self.reg.setText(QCoreApplication.translate("MainWindow", u"regsiter", None))
        self.value.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">value</p></body></html>", None))
        self.line_id.setText(QCoreApplication.translate("MainWindow", u"num", None))
        self.stop.setText("")
        self.run.setText("")
    # retranslateUi

