# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mem_view.ui'
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
    QLabel, QLineEdit, QSizePolicy, QTableView,
    QWidget)

class Ui_MemoryView(object):
    def setupUi(self, MemoryView):
        if not MemoryView.objectName():
            MemoryView.setObjectName(u"MemoryView")
        MemoryView.setEnabled(True)
        MemoryView.resize(640, 480)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_2 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table = QTableView(self.dockWidgetContents)
        self.table.setObjectName(u"table")

        self.gridLayout_2.addWidget(self.table, 2, 0, 1, 2)

        self.from_item = QLineEdit(self.dockWidgetContents)
        self.from_item.setObjectName(u"from_item")

        self.gridLayout_2.addWidget(self.from_item, 0, 1, 1, 1)

        self.from_label = QLabel(self.dockWidgetContents)
        self.from_label.setObjectName(u"from_label")

        self.gridLayout_2.addWidget(self.from_label, 0, 0, 1, 1)

        self.to_label = QLabel(self.dockWidgetContents)
        self.to_label.setObjectName(u"to_label")

        self.gridLayout_2.addWidget(self.to_label, 1, 0, 1, 1)

        self.to_item = QLineEdit(self.dockWidgetContents)
        self.to_item.setObjectName(u"to_item")

        self.gridLayout_2.addWidget(self.to_item, 1, 1, 1, 1)

        MemoryView.setWidget(self.dockWidgetContents)

        self.retranslateUi(MemoryView)
        self.from_item.editingFinished.connect(MemoryView.setStartAddress)
        self.to_item.editingFinished.connect(MemoryView.setEndAddress)

        QMetaObject.connectSlotsByName(MemoryView)
    # setupUi

    def retranslateUi(self, MemoryView):
        MemoryView.setWindowTitle(QCoreApplication.translate("MemoryView", u"\u041f\u0430\u043c\u044f\u0442\u044c", None))
        self.from_label.setText(QCoreApplication.translate("MemoryView", u"\u041e\u0442", None))
        self.to_label.setText(QCoreApplication.translate("MemoryView", u"\u0414\u043e", None))
    # retranslateUi

