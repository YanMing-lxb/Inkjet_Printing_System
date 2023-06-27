from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import GUI
from Slot_A import Slot_A
from Slot_B import Slot_B
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Window')

        self.gui = GUI()
        self.gui.button_a.clicked.connect(self.run_slot_a)
        self.gui.button_b.clicked.connect(self.run_slot_b)

        self.setCentralWidget(self.gui)

        self.C = None

    def run_slot_a(self):
        slot_a = Slot_A()
        self.C = slot_a.calculate_C()
        print('Signal C calculated:', self.C)
        self.gui.button_b.setEnabled(True)
        

    def run_slot_b(self):
        if self.C is not None:
            slot_b = Slot_B()
            result = slot_b.calculate_sum(self.C)
            print('Signal C sum:', result)
        else:
            print('Signal C is not calculated yet!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())