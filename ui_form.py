# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGroupBox, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 600)
        MainWindow.setStyleSheet(u"background-color:white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, 50, 951, 50))
        self.widget.setStyleSheet(u"background-color: rgb(238, 243, 243)")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save = QPushButton(self.widget)
        self.save.setObjectName(u"save")
        icon = QIcon()
        icon.addFile(u"../GUI/resources/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save.setIcon(icon)
        self.save.setIconSize(QSize(32, 32))
        self.save.setFlat(True)

        self.horizontalLayout.addWidget(self.save)

        self.cut = QPushButton(self.widget)
        self.cut.setObjectName(u"cut")
        icon1 = QIcon()
        icon1.addFile(u"../GUI/resources/content_cut.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cut.setIcon(icon1)
        self.cut.setIconSize(QSize(32, 32))
        self.cut.setFlat(True)

        self.horizontalLayout.addWidget(self.cut)

        self.copy = QPushButton(self.widget)
        self.copy.setObjectName(u"copy")
        icon2 = QIcon()
        icon2.addFile(u"../GUI/resources/file_copy.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.copy.setIcon(icon2)
        self.copy.setIconSize(QSize(32, 32))
        self.copy.setFlat(True)

        self.horizontalLayout.addWidget(self.copy)

        self.paste = QPushButton(self.widget)
        self.paste.setObjectName(u"paste")
        self.paste.setStyleSheet(u"QPush-Button{\n"
"	font-color: black\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../GUI/resources/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.paste.setIcon(icon3)
        self.paste.setIconSize(QSize(32, 32))
        self.paste.setFlat(True)

        self.horizontalLayout.addWidget(self.paste)

        self.back = QPushButton(self.widget)
        self.back.setObjectName(u"back")
        icon4 = QIcon()
        icon4.addFile(u"../GUI/resources/keyboard_return.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back.setIcon(icon4)
        self.back.setIconSize(QSize(32, 32))
        self.back.setFlat(True)

        self.horizontalLayout.addWidget(self.back)

        self.build = QPushButton(self.widget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.build)
        self.build.setObjectName(u"build")
        icon5 = QIcon()
        icon5.addFile(u"../GUI/resources/hardware.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.build.setIcon(icon5)
        self.build.setIconSize(QSize(32, 32))
        self.build.setFlat(True)

        self.horizontalLayout.addWidget(self.build)

        self.run = QPushButton(self.widget)
        self.buttonGroup.addButton(self.run)
        self.run.setObjectName(u"run")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        self.run.setFont(font)
        self.run.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"../GUI/resources/play_arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.run.setIcon(icon6)
        self.run.setIconSize(QSize(32, 32))
        self.run.setFlat(True)

        self.horizontalLayout.addWidget(self.run)

        self.pushButton_9 = QPushButton(self.widget)
        self.buttonGroup.addButton(self.pushButton_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon7 = QIcon()
        icon7.addFile(u"../GUI/resources/crop_5_4.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(32, 32))
        self.pushButton_9.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.horizontalSpacer_2 = QSpacerItem(297, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.CODE = QWidget(self.centralwidget)
        self.CODE.setObjectName(u"CODE")
        self.CODE.setGeometry(QRect(-10, 100, 511, 531))
        self.CODE.setStyleSheet(u"border: 1px solid rgb(155, 158, 158);\n"
"border-radius: 7px;")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 941, 51))
        self.widget_2.setStyleSheet(u"background:rgb(196, 199, 199);\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.F = QPushButton(self.widget_2)
        self.F.setObjectName(u"F")
        font1 = QFont()
        font1.setFamilies([u"Raleway"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.F.setFont(font1)
        self.F.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"}\n"
"\n"
"\n"
"")
        self.F.setFlat(True)

        self.horizontalLayout_3.addWidget(self.F)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color:black;\n"
"")
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"color:black;\n"
"")
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	color:black;\n"
"}")
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"color:black")
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.horizontalSpacer = QSpacerItem(339, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 100, 941, 521))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(490, 240, 120, 80))
        self.Filemenu = QWidget(self.centralwidget)
        self.Filemenu.setObjectName(u"Filemenu")
        self.Filemenu.setGeometry(QRect(40, 190, 160, 80))
        self.File_menu = QVBoxLayout(self.Filemenu)
        self.File_menu.setObjectName(u"File_menu")
        self.pushButton_5 = QPushButton(self.Filemenu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"color:black\n"
"")

        self.File_menu.addWidget(self.pushButton_5)

        self.pushButton = QPushButton(self.Filemenu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color:black\n"
"")

        self.File_menu.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.F.clicked["bool"].connect(self.Filemenu.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save.setText("")
        self.cut.setText("")
        self.copy.setText("")
        self.paste.setText("")
        self.back.setText("")
        self.build.setText("")
        self.run.setText("")
        self.pushButton_9.setText("")
        self.F.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u043e\u0435\u043d\u0438\u0435", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u0430\u0434\u043a\u0430", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;h1, style=&quot;font-color: black&quot;&gt;THRES`S YOUR CODE&lt;\\h1&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
    # retranslateUi

