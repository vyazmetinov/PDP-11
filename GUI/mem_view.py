# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np

import ui_mem_view


class MyModel_1(QAbstractTableModel):
<<<<<<< HEAD

    def rowCount(self, parent: QModelIndex):
        return 3
    def columnCount(self, parent: QModelIndex):
        return 2

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return index.row() + index.column()
        return None
=======
    word_size = 0x02

    def __init__(self):
        super().__init__()
        self.first_id = 0x001000
        self.last_id = 0x001022

    def rowCount(self, parent: QModelIndex):
        return (self.last_id - self.first_id) // self.word_size + 1

    def columnCount(self, parent: QModelIndex):
        return 2

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return f"{oct(self.first_id + self.word_size + index.row())}"
            return index.row() + index.column()
        return None

>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
    def headerData(self, col, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ["Адрес", "Значение"][col]

<<<<<<< HEAD
=======
    # def flags(self, index):
    #     default_flags = QAbstractTableModel.flags(self, index)
    #     # if index.column() == 1:
    #     #     return default_flags | PySide6.QtCore.Qt.ItemFlag.ItemIsEditable
    #     return default_flags


>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
class MemoryView(PySide6.QtWidgets.QDockWidget, ui_mem_view.Ui_MemoryView):
    def __init__(self, parent: None):
        print("Memory view.init")
        super().__init__(parent)
        self.setupUi(self)
        print("setupUI")
        self.model = MyModel_1()
        self.table.setModel(self.model)
        self.ui = ui_mem_view.Ui_MemoryView()
<<<<<<< HEAD
=======
        self.setStartAddress()
        self.setEndAddress()

    def setStartAddress(self):
        address = self.from_item.text()
        try:
            value = int(address, base=8)
            assert value < 0 or value > 0xFF
            self.model.first_id = value
        except:
            self.from_item.setText(oct(self.model.first_id))

    def setEndAddress(self):
        address = self.to_item.text()
        try:
            value = int(address, base=8)
            assert value < 0 or value > 0xFF
            self.model.last_id = value
        except:
            self.to_item.setText(oct(self.model.last_id))
>>>>>>> beb2c9fb29a537f83deca539133c5fc84028614e
