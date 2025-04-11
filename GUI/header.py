import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np
import ui_header


class Header(PySide6.QtWidgets.QDockWidget, ui_header.Ui_header):
    def __init__(self, parent: None):
        print("Memory view.init")
        super().__init__(parent)
        self.setupUi(self)
        print("setupUI")
        self.ui = ui_header.Ui_header()




