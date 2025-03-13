# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6.QtWidgets import QApplication, QWidget

import mainwindow




class ExampleApp(PySide6.QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ExampleApp()
    window.show()
    sys.exit(app.exec())
