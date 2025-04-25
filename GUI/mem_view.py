# This Python file uses the following encoding: utf-8
import sys
sys.path.append('C:/proekt/PDP-11')
import PySide6
from PySide6.QtCore import QAbstractItemModel, QAbstractTableModel, QModelIndex, Qt
from PySide6.QtWidgets import QApplication, QWidget, QTableView, QTableWidgetItem
from virtual_executor.mem import mem, w_read
import numpy as np

import ui_mem_view


class MyModel_1(QAbstractTableModel):
    word_size = 0x02

    def __init__(self, mem):
        super().__init__()
        self.first_id = 0o001000
        self.last_id = 0o001022
        self.memory = mem

    def rowCount(self, parent: QModelIndex):
        return (self.last_id - self.first_id) // 2 + 1

    def columnCount(self, parent: QModelIndex):
        return 2

    def insertRows(self, position, rows=1, parent=QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)

        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, parent=QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)
        self.endRemoveRows()
        return True

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # print(index.row(), len(self.memory))
            if index.column() == 0:
                return f"{oct((index.row() * 2 + self.first_id))}"
            return oct(w_read((index.row() * 2 + self.first_id)))
        # print("ALARM")
        return None
    def headerData(self, col, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ["Адрес", "Значение"][col]


    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role != Qt.EditRole:
            return False

        row, col = index.row(), index.column()
        addr, val = self.memory[row]

        if col == 1:
            try:
                if value.lower().startswith("0o"):
                    new_val = int(value, 8)
                else:
                    new_val = int(value)
                self.memory[row] = (addr, new_val)
                self.dataChanged.emit(index, index)
                return True
            except ValueError:
                return False

        return False


    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        if index.column() == 1:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable



class MemoryView(PySide6.QtWidgets.QDockWidget, ui_mem_view.Ui_MemoryView):
    def __init__(self, parent: None):
        print("Memory view.init")
        super().__init__(parent)
        self.setupUi(self)
        print("setupUI")
        self.model = MyModel_1(mem)
        self.table.setModel(self.model)
        self.table.verticalHeader().setDefaultSectionSize(24)
        self.table.resizeRowsToContents = lambda: None  # отключение автоизменения высоты строк
        self.ui = ui_mem_view.Ui_MemoryView()
        self.setStartAddress()
        self.setEndAddress()




    def setStartAddress(self):
        address = self.from_item.text()
        try:
            value = int(address, base=8)
            assert value < 0 or value > 0xFF

            # if self.model.first_id <= value:
            #     self.model.memory = self.model.memory[((value - self.model.first_id) // 2)::]
            #     for i in range(value, self.model.first_id, 2):
            #         self.model.removeRows(0)
            # else:
            #     new_indexes = [[value + i, 0] for i in range(0, self.model.first_id - value, 2)]
            #     self.model.memory = new_indexes + self.model.memory
            #     for i in range(self.model.first_id - value):
            #         self.model.insertRows(0)
            #     # for row in range(len(self.model.memory)):
            #     #     self.table.setRowHeight(row, 24)

            self.model.beginResetModel()
            self.model.first_id = value
            self.model.endResetModel()
        except:
            self.from_item.setText(str(oct(self.model.first_id)))

    def setEndAddress(self):
        address = self.to_item.text()
        try:
            value = int(address, base=8)
            assert value < 0 or value > 0xFF
            # if self.model.last_id <= value:
            #     new_indexes = [[self.model.last_id + i, 0] for i in range(2, value - self.model.last_id + 2, 2)]
            #     self.model.memory = self.model.memory + new_indexes
            #     for i in range(value - self.model.last_id):
            #         self.model.insertRows(-1)
            #     for row in range(len(self.model.memory)):
            #         self.table.setRowHeight(row, 24)
            #
            # else:
            #     self.model.memory = self.model.memory[0:-((self.model.last_id - value) // 2)]
            #     for i in range(value, self.model.last_id, 2):
            #         self.model.removeRows(-1)

            self.model.beginResetModel()
            self.model.last_id = value
            self.model.endResetModel()
        except:
            self.to_item.setText(str(oct(self.model.last_id)))

    def update_memory(self, mem_changes):
        self.model.beginResetModel()

        self.model.endResetModel()

