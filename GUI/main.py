# This Python file uses the following encoding: utf-8
import sys

import PySide6
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
import subprocess

if __name__ == "__main__":
    for f in ["reg", "mainwindow", "mem_view", "code", "assembler", "header"]:
        subprocess.run(["pyside6-uic", f"{f}.ui", "-o", f"ui_{f}.py"], check=True)
import ui_mainwindow
from pathlib import Path





class Mainwindow(PySide6.QtWidgets.QMainWindow, ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.current_file_path = None
        self.running = False
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.header_2.stepButton.clicked.connect(self.runAssemblyOnce)
        self.header_2.timer.timeout.connect(self.runAssemblyOnce)
        self.actionRun.setCheckable(True)
        self.header_2.runButton.setCheckable(True)
        self.header_2.runButton.toggled.connect(self.runAssembly)
        self.current_line = 0


    def openFile(self, file_path: str):
        fileName = ""
        if file_path:
            fileName = file_path
            text = Path(fileName).read_text()
            self.current_file_path = fileName
            self.code.setText(text)
        else:
            fileName, _ = QFileDialog.getOpenFileName(self, 'Open code', './', 'PDP-11 (*.pdp);;Текстовые файлы (*.txt);;Все файлы (*)')
            print("fileName", fileName[0])
            fileName = Path(fileName)
            text = fileName.read_text()
            self.current_file_path = fileName
            self.code.setText(text)

    def createFile(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Создать файл", "", "PDP-11 (*.pdp);;Текстовые файлы (*.txt);;Все файлы (*)")
        if file_path:
            with open(file_path, 'w') as f:
                f.write("Напишите что-нибудь:")

            self.openFile(file_path)
            self.current_file_path = file_path
            print(f"Файл создан: {file_path}")

    def saveFileAs(self):
        text = self.code.text()

        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "",
                                                             "PDP (*.pdp);;Текстовые файлы (*.txt);;Все файлы (*)",
                                                             options=options)

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text)
                QtWidgets.QMessageBox.information(self, "Успех", "Файл успешно сохранён!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{e}")

    def saveFile(self):
        print(f"currentDIR: {self.current_file_path}")
        if not hasattr(self, 'current_file_path') or not self.current_file_path:
            QtWidgets.QMessageBox.warning(self, "Внимание", "Файл не открыт.")
            return

        try:
            text = self.code.text()
            with open(self.current_file_path, 'w', encoding='utf-8') as file:
                file.write(text)
            QtWidgets.QMessageBox.information(self, "Успех", "Файл успешно сохранён!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении файла:\n{e}")

    def runAssemblyOnce(self):

        text = self.code.text().split("\n")
        if self.current_line < len(text):
            print(text[self.current_line])
            self.current_line += 1
        else:
            print("COMPLETE")
            self.stopAssembly()
            self.current_line = 0

    def runAssembly(self, checked):
        if checked:
            self.runAssemblyOnce()
            self.header_2.runButton.setIcon(QIcon(":icons/icons/crop_5_4.svg"))
            self.header_2.timer.start(int(60000 / int(self.header_2.speed.text())))

        else:
            self.stopAssembly()


    def stopAssembly(self):
        self.header_2.timer.stop()
        self.header_2.runButton.setIcon(QIcon(":icons/icons/play_arrow.svg"))


app = QApplication(sys.argv)

window = Mainwindow()

window.show()
sys.exit(app.exec())
