# This Python file uses the following encoding: utf-8
import sys
sys.path.append('/Users/ivan/Documents/GitHub/PDP-11')
from virtual_executor.mem import *
import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np
import ui_reg

class MyModel(QAbstractTableModel):
    dataset = [
        ["N", 0, 0],
        ["Z", 0, 0],
        ["V", 0, 0],
        ["C", 0, 0],
        ["R0", 0, 0],
        ["R1", 0, 0],
        ["R2", 0, 0],
        ["R3", 0, 0],
        ["R4", 0, 0],
        ["R5", 0, 0],
        ["R6", 0, 0],
        ["R7", 0, 0],
    ]


    def rowCount(self, parent: QModelIndex):
        return len(self.dataset)
    def columnCount(self, parent: QModelIndex):
        return 2

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):

        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return (str(self.dataset[index.row()][0]))
            elif index.column() == 1:
                return self.dataset[index.row()][1]


        return None

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            try:
                value = int(value, base=8)
            except ValueError:
                return False

            # if not(0 <= value <= 3):
            #     return False
            print(f"Register {index.row()}, changed to {value}")
            self.dataset[index.row()][1] = value
            return True
        return False

    def headerData(self, col, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ["Регистр", "Значение"][col]

    def flags(self, index):
        default_flags = QAbstractTableModel.flags(self, index)
        if index.column() == 1:
            return PySide6.QtCore.Qt.ItemFlag.ItemIsEditable | QAbstractTableModel.flags(self, index)
        return default_flags
class Registers(PySide6.QtWidgets.QDockWidget, ui_reg.Ui_Registers):
    def __init__(self, parent: None):
        super().__init__(parent)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.model = MyModel()
        self.table.setModel(self.model)
        self.ui = ui_reg.Ui_Registers()
    def updateRegisters(self, reg_changes, nzvc_changes):
        for i in range(len(self.model.dataset)):
            if i < 4:
                self.model.beginResetModel()
                self.model.dataset[i] = [self.model.dataset[i][0], NZVC[i], i in nzvc_changes]
                self.model.endResetModel()

            else:
                self.model.beginResetModel()
                self.model.dataset[i] = [self.model.dataset[i][0], reg[i - 4], i - 4 in reg_changes]
                self.model.endResetModel()




