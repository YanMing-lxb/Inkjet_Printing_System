from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.button_a = QPushButton('Run Slot A')
        self.button_b = QPushButton('Run Slot B')
        self.button_b.setEnabled(False)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_a)
        self.layout.addWidget(self.button_b)

        self.setLayout(self.layout)