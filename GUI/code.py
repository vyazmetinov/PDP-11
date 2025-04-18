# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np

import ui_code


<<<<<<< HEAD
class MyModel_2(QAbstractTableModel):

    def rowCount(self, parent: QModelIndex):
        return 3
    def columnCount(self, parent: QModelIndex):
        return 2

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return index.row() + index.column()
        return None
    def headerData(self, col, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ["Адрес", "Значение"][col]

class Code(PySide6.QtWidgets.QWidget, ui_code.Ui_Code):
    def __init__(self, parent: None):
        print("Memory view.init")
        super().__init__(parent)
        self.setupUi(self)
        print("setupUI")
        self.model = MyModel_2()

        self.ui = ui_code.Ui_Code()
=======

class Code(PySide6.QtWidgets.QWidget, ui_code.Ui_Code):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ui = ui_code.Ui_Code()
        print(self.code.toPlainText())

    def on_run_button_clicked(self):
        text = self.code.toPlainText()
        print(text)


    def setText(self, text):
        return self.code.setText(text)

    def text(self):
        return self.code.toPlainText()
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
