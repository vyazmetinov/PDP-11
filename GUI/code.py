# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np

import ui_code



class Code(PySide6.QtWidgets.QWidget, ui_code.Ui_Code):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ui = ui_code.Ui_Code()
        print(self.code.toPlainText())

    def on_run_button_clicked(self):
        # Получаем текст из QTextEdit (замените self.code на правильное имя, если требуется)
        text = self.code.toPlainText()
        print(text)

    def setText(self, text):
        return self.code.setText(text)

    def text(self):
        return self.code.toPlainText()