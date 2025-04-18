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
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Header(object):
    def setupUi(self, Header):
        if not Header.objectName():
            Header.setObjectName(u"Header")
        Header.resize(640, 480)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.dockWidgetContents)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.custom_play = QWidget(self.horizontalWidget)
        self.custom_play.setObjectName(u"custom_play")
        self.custom_play.setStyleSheet(u"#custom_play{\n"
"background-color:rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.custom_play)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.runButton = QPushButton(self.custom_play)
        self.runButton.setObjectName(u"runButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runButton.sizePolicy().hasHeightForWidth())
        self.runButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/skip_next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.runButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.runButton, 0, Qt.AlignTop)

        self.speed = QSpinBox(self.custom_play)
        self.speed.setObjectName(u"speed")
        sizePolicy.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
        self.speed.setSizePolicy(sizePolicy)
        self.speed.setAccelerated(True)
        self.speed.setMinimum(1)
        self.speed.setMaximum(999)
        self.speed.setValue(60)

        self.horizontalLayout_2.addWidget(self.speed, 0, Qt.AlignTop)

        self.label = QLabel(self.custom_play)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.custom_play, 0, Qt.AlignTop)

        self.stepButton = QPushButton(self.horizontalWidget)
        self.stepButton.setObjectName(u"stepButton")
        sizePolicy.setHeightForWidth(self.stepButton.sizePolicy().hasHeightForWidth())
        self.stepButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":icons/icons/play_arrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stepButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.stepButton, 0, Qt.AlignVCenter)


        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1, Qt.AlignRight|Qt.AlignTop)

        Header.setWidget(self.dockWidgetContents)

        self.retranslateUi(Header)

        QMetaObject.connectSlotsByName(Header)
    # setupUi

    def retranslateUi(self, Header):
        Header.setWindowTitle(QCoreApplication.translate("Header", u"DockWidget", None))
        self.runButton.setText("")
#if QT_CONFIG(whatsthis)
        self.speed.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.speed.setSpecialValueText("")
        self.speed.setPrefix("")
        self.label.setText(QCoreApplication.translate("Header", u"\u041a\u043e\u043c/\u043c\u0438\u043d", None))
        self.stepButton.setText("")
    # retranslateUi

