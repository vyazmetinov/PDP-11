import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QTableView
import numpy as np
import ui_header



class Header(PySide6.QtWidgets.QDockWidget, ui_header.Ui_Header):
    def __init__(self, parent: None):
        print("Memory view.init")
        super().__init__(parent)
        self.setupUi(self)
        print("setupUI")
        self.ui = ui_header.Ui_Header()

        self.timer = QTimer(self)
        self.runButton.clicked.connect(lambda: self.timer.start(1000))
        self.stopButton.clicked.connect(lambda: self.timer.stop())






