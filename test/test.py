from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Window')

        self.button = QPushButton('Click me!', self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.button_clicked)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(50, 100)

    def button_clicked(self):
        text = self.line_edit.text()
        print('Button clicked with text:', text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

