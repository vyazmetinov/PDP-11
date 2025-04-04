import mem_view

class Stack(mem_view.MemoryView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.to_label.setVisible(False)
        self.from_label.setVisible(False)
        self.to_item.setVisible(False)
        self.from_item.setVisible(False)
