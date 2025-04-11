# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'header.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QSpinBox, QWidget)
import res_rc

class Ui_header(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(640, 480)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.dockWidgetContents)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.custom_play = QWidget(self.horizontalWidget)
        self.custom_play.setObjectName(u"custom_play")
        self.custom_play.setStyleSheet(u"#custom_play{\n"
"background-color:rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.custom_play)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.custom_play)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/skip_next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignTop)

        self.speed = QSpinBox(self.custom_play)
        self.speed.setObjectName(u"speed")
        sizePolicy.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.speed, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.custom_play, 0, Qt.AlignTop)

        self.run = QPushButton(self.horizontalWidget)
        self.run.setObjectName(u"run")
        sizePolicy.setHeightForWidth(self.run.sizePolicy().hasHeightForWidth())
        self.run.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":icons/icons/play_arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.run.setIcon(icon1)

        self.horizontalLayout.addWidget(self.run, 0, Qt.AlignVCenter)

        self.stop = QPushButton(self.horizontalWidget)
        self.stop.setObjectName(u"stop")
        sizePolicy.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy)
        self.stop.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":icons/icons/crop_5_4.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop.setIcon(icon2)

        self.horizontalLayout.addWidget(self.stop, 0, Qt.AlignVCenter)


        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1, Qt.AlignRight|Qt.AlignTop)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.pushButton.setText("")
        self.run.setText("")
        self.stop.setText("")
    # retranslateUi

