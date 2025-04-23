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
<<<<<<< HEAD
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QHBoxLayout, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

from code import Code
=======
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QTabWidget, QWidget)

from assembler import Assembler
from code import Code
from header import Header
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
from mem_view import MemoryView
from reg import Registers
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
<<<<<<< HEAD
        MainWindow.resize(1006, 714)
=======
        MainWindow.resize(968, 714)
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
<<<<<<< HEAD
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
=======
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setBaseSize(QSize(0, 0))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionCreate = QAction(MainWindow)
        self.actionCreate.setObjectName(u"actionCreate")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.ationSaveAs = QAction(MainWindow)
        self.ationSaveAs.setObjectName(u"ationSaveAs")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionBuild = QAction(MainWindow)
        self.actionBuild.setObjectName(u"actionBuild")
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
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
<<<<<<< HEAD
=======
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.actionStep = QAction(MainWindow)
        self.actionStep.setObjectName(u"actionStep")
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
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
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tabWidget.setDocumentMode(True)
<<<<<<< HEAD
        self.code = Code(MainWindow)
        self.code.setObjectName(u"code")
        self.tabWidget.addTab(self.code, "")
        self.widget = QWidget()
=======
        self.tabWidget.setTabsClosable(False)
        self.code = Code()
        self.code.setObjectName(u"code")
        self.tabWidget.addTab(self.code, "")
        self.widget = Assembler()
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
        self.widget.setObjectName(u"widget")
        self.tabWidget.addTab(self.widget, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
<<<<<<< HEAD
        self.menubar.setGeometry(QRect(0, 0, 1006, 24))
=======
        self.menubar.setGeometry(QRect(0, 0, 968, 24))
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
        self.File = QMenu(self.menubar)
        self.File.setObjectName(u"File")
        self.Debug_2 = QMenu(self.menubar)
        self.Debug_2.setObjectName(u"Debug_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
<<<<<<< HEAD
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
        self.dockWidget = Registers(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)
        self.dockWidget_3 = MemoryView(MainWindow)
        self.dockWidget_3.setObjectName(u"dockWidget_3")
        self.dockWidget_3.setAllowedAreas(Qt.BottomDockWidgetArea)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dockWidget_3)
=======
        self.header_2 = Header(MainWindow)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setStyleSheet(u"#header_2{\n"
"background-color: white;\n"
"}")
        self.header_2.setFloating(False)
        self.header_2.setFeatures(QDockWidget.NoDockWidgetFeatures)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.header_2)
        self.registers = Registers(MainWindow)
        self.registers.setObjectName(u"registers")
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.registers)
        self.memoryView = MemoryView(MainWindow)
        self.memoryView.setObjectName(u"memoryView")
        self.memoryView.setAllowedAreas(Qt.AllDockWidgetAreas)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.memoryView)
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e

        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Debug_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
<<<<<<< HEAD
        self.File.addAction(self.Open)
        self.File.addAction(self.Create)
        self.File.addAction(self.Save)
        self.File.addAction(self.Save_as)
        self.File.addAction(self.Close)
        self.Debug_2.addAction(self.Run_2)
        self.Debug_2.addAction(self.Build)
        self.Debug_2.addAction(self.actionDebug)
=======
        self.File.addAction(self.actionOpen)
        self.File.addAction(self.actionCreate)
        self.File.addAction(self.actionSave)
        self.File.addAction(self.ationSaveAs)
        self.Debug_2.addAction(self.actionDebug)
        self.Debug_2.addAction(self.actionBuild)
        self.Debug_2.addAction(self.actionStep)
        self.Debug_2.addAction(self.actionRun)
        self.Debug_2.addAction(self.actionStop)
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)

        self.retranslateUi(MainWindow)
<<<<<<< HEAD
=======
        self.actionOpen.triggered.connect(MainWindow.openFile)
        self.actionCreate.triggered.connect(MainWindow.createFile)
        self.actionSave.triggered.connect(MainWindow.saveFile)
        self.ationSaveAs.triggered.connect(MainWindow.saveFileAs)
        self.actionStep.triggered.connect(MainWindow.runAssemblyOnce)
        self.actionStop.triggered.connect(MainWindow.stopAssembly)
        self.actionRun.triggered.connect(MainWindow.runAssembly)
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
<<<<<<< HEAD
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
=======
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionCreate.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.actionCreate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.ationSaveAs.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
#if QT_CONFIG(shortcut)
        self.ationSaveAs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"\u0417\u044b\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionBuild.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u043e\u0440\u043a\u0430", None))
#if QT_CONFIG(shortcut)
        self.actionBuild.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionDebug.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
#if QT_CONFIG(shortcut)
        self.actionDebug.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u0430\u0434\u043a\u0430", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u044b", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionStep.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433", None))
#if QT_CONFIG(shortcut)
        self.actionStep.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.code), QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"\u0410\u0441\u0441\u0435\u043c\u0431\u043b\u0435\u0440", None))
        self.File.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.Debug_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043b\u0430\u0434\u043a\u0430", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u0430\u0434\u043a\u0438", None))
<<<<<<< HEAD
        self.stop.setText("")
        self.run.setText("")
=======
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
    # retranslateUi

