# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assembler.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableView, QWidget)

class Ui_Assembler(object):
    def setupUi(self, Assembler):
        if not Assembler.objectName():
            Assembler.setObjectName(u"Assembler")
        Assembler.resize(640, 480)
        self.gridLayout = QGridLayout(Assembler)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(Assembler)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)


        self.retranslateUi(Assembler)

        QMetaObject.connectSlotsByName(Assembler)
    # setupUi

    def retranslateUi(self, Assembler):
        Assembler.setWindowTitle(QCoreApplication.translate("Assembler", u"Form", None))
    # retranslateUi

