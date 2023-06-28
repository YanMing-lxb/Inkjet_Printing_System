import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QtGui.QApplication([])
win = pg.GraphicsLayoutWidget()
win.show()

p = win.addPlot()

def waveform_display(values):
    x = []
    y = []
    for point in values:
        x.append(point[0])
        y.append(point[1])
    p.plot(x, y, pen='b')

values = [[0, 0], [1, 1], [2, 0], [3, -1]]  # 示例输入数据
waveform_display(values)

if __name__ == '__main__':
    app.exec_()