# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np

import ui_assembler


class MyModel_3(QAbstractTableModel, ui_assembler.Ui_Assembler):
    dataset = [
        dict({"memory": "001000", "command": "mov     #000200,r1", "comment": "[001002]=000200"}),
        dict({"memory": "001004", "command": "movb    (r1)+,r0   ", "comment": "[000200]=110"}),
        dict({"memory": "001006", "command": "beq     001024     ", "comment": ""}),
        dict({"memory": "001010", "command": "tstb    @#177564   ", "comment": "[177564]=200"}),
        dict({"memory": "001014", "command": "bpl     001010     ", "comment": ""}),
        dict({"memory": "001016", "command": "movb    r0,@#177566", "comment": "R0=110 [177566]"}),
        dict({"memory": "001022", "command": "br      001004     ", "comment": ""}),
        dict({"memory": "001004", "command": "movb    (r1)+,r0   ", "comment": "[000201]=145"}),
        dict({"memory": "001006", "command": "beq     001024     ", "comment": ""}),
        dict({"memory": "001010", "command": "tstb    @#177564   ", "comment": "[177564]=200"}),
        dict({"memory": "001014", "command": "bpl     001010     ", "comment": ""}),
        dict({"memory": "001016", "command": "movb    r0,@#177566", "comment": "R0=145 [177566]"}),
        dict({"memory": "001022", "command": "br      001004     ", "comment": ""}),
        dict({"memory": "001004", "command": "movb    (r1)+,r0   ", "comment": "[000202]=154"}),
        dict({"memory": "001006", "command": "beq     001024     ", "comment": ""}),
        dict({"memory": "001010", "command": "tstb    @#177564   ", "comment": "[177564]=200"}),
        dict({"memory": "001014", "command": "bpl     001010     ", "comment": ""}),
        dict({"memory": "001016", "command": "movb    r0,@#177566", "comment": "R0=154 [177566]"}),
        dict({"memory": "001022", "command": "br      001004     ", "comment": ""}),
        dict({"memory": "001004", "command": "movb    (r1)+,r0   ", "comment": "[000203]=154"}),
        dict({"memory": "001006", "command": "beq     001024     ", "comment": ""}),
        dict({"memory": "001010", "command": "tstb    @#177564   ", "comment": "[177564]=200"}),
        dict({"memory": "001014", "command": "bpl     001010     ", "comment": ""}),
        dict({"memory": "001016", "command": "movb    r0,@#177566", "comment": "R0=154 [177566]"}),
        dict({"memory": "001022", "command": "br      001004     ", "comment": ""}),
        dict({"memory": "001004", "command": "movb    (r1)+,r0   ", "comment": "[000204]=157"}),
        dict({"memory": "001006", "command": "beq     001024     ", "comment": ""}),
        dict({"memory": "001010", "command": "tstb    @#177564   ", "comment": "[177564]=200"}),
        dict({"memory": "001014", "command": "bpl     001010     ", "comment": ""}),
        dict({"memory": "001016", "command": "movb    r0,@#177566", "comment": "R0=157 [177566]"}),
        dict({"memory": "001022", "command": "br      001004     ", "comment": ""}),
        dict({"memory": "001004", "command": "movb    (r1)+,r0   ", "comment": "[000205]=054})"}),
    ]

    def rowCount(self, parent: QModelIndex):
        return len(self.dataset)

    def columnCount(self, parent: QModelIndex):
        return 3

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return (str(self.dataset[index.row()]["memory"]) + ":")
            elif index.column() == 1:
                return self.dataset[index.row()]["command"]
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
        self.tableView.resizeColumnsToContents()

