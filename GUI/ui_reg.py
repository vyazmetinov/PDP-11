# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHeaderView,
    QSizePolicy, QTableView, QWidget)

class Ui_Registers(object):
    def setupUi(self, Registers):
        if not Registers.objectName():
            Registers.setObjectName(u"Registers")
        Registers.resize(736, 469)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableView(self.dockWidgetContents)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)

        Registers.setWidget(self.dockWidgetContents)

        self.retranslateUi(Registers)

        QMetaObject.connectSlotsByName(Registers)
    # setupUi

    def retranslateUi(self, Registers):
        Registers.setWindowTitle(QCoreApplication.translate("Registers", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u044b", None))
    # retranslateUi

