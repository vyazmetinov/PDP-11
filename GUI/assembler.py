# This Python file uses the following encoding: utf-8
import sys
sys.path.append('/Users/ivan/Documents/GitHub/PDP-11')
from Compiler.pdp11_parsing import compiled
import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np

import ui_assembler


class MyModel_3(QAbstractTableModel, ui_assembler.Ui_Assembler):
    dataset = []

    def rowCount(self, parent: QModelIndex):
        return len(self.dataset)


    def columnCount(self, parent: QModelIndex):
        return 3

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return (str(self.dataset[index.row()]["adr"]) + ":")
            elif index.column() == 1:
                return self.dataset[index.row()]["cmd"]
            elif index.column() == 2:
                return self.dataset[index.row()]["comment"]
        return None

    def headerData(self, col, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ["Адрес", "Команда", "Комментарий"][col]


class Assembler(PySide6.QtWidgets.QWidget, ui_assembler.Ui_Assembler):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.model = MyModel_3()
        self.tableView.setModel(self.model)
        self.ui = ui_assembler.Ui_Assembler()

    def update_dataset(self, assm):
        self.model.beginResetModel()
        self.model.dataset = assm

        self.model.endResetModel()
        self.tableView.resizeColumnsToContents()

