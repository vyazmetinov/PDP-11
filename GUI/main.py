# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
import subprocess
if __name__ == "__main__":
    for f in ["reg", "mainwindow", "mem_view", "code", "assembler", "header"]:
        subprocess.run(["pyside6-uic", f"{f}.ui", "-o", f"ui_{f}.py"], check=True)
import ui_mainwindow
from pathlib import Path





class ExampleApp(PySide6.QtWidgets.QMainWindow, ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.header_2.stepButton.clicked.connect(self.runAssemblyOnce)
        self.header_2.timer.timeout.connect(self.runAssemblyOnce)


    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open code', './', 'PDP-11 assembly files (*.py)')
        print("fileName", fileName[0])
        fileName = Path(fileName[0])
        text = fileName.read_text()
        self.code.setText(text)
    def runAssemblyOnce(self):
        print("Asssembly code running...")



app = QApplication(sys.argv)

window = ExampleApp()
window.show()
sys.exit(app.exec())
