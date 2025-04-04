# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np

import ui_mem_view


class MyModel_1(QAbstractTableModel):

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

class MemoryView(PySide6.QtWidgets.QDockWidget, ui_mem_view.Ui_MemoryView):
    def __init__(self, parent: None):
        print("Memory view.init")
        super().__init__(parent)
        self.setupUi(self)
        print("setupUI")
        self.model = MyModel_1()
        self.table.setModel(self.model)
        self.ui = ui_mem_view.Ui_MemoryView()
