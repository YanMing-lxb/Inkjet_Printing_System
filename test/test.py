'''
main.py文件内容如下:
```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.Ui_MainWindow import Ui_MainWindow
from SLOT.Slot_Main import Quit, File
from SLOT.Slot_PathDisplay import PathDisplay
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup UI
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.setWindowTitle('3D喷墨打印控制系统')

        self.ValuesCoordinate = None
        self.ValueWaveForm = None 
        self.main_ui.Button_FileRead.clicked.connect(self.file_read)
        self.main_ui.Button_TrajectoryPreview.clicked.connect(self.path_display)
    def file_read(self):
        file = File()
        self.ValuesCoordinate = file.FileRead()
        if self.ValuesCoordinate is not None:
            self.main_ui.Button_TrajectoryPreview.setEnabled(True)
    
    def path_display(self):
        if self.ValuesCoordinate is not None:
            pathdisplay = PathDisplay()
            pathdisplay.graphicsView_PathDisplay = self.main_ui.graphicsView_PathDisplay
            pathdisplay.PlotPathDisplay(self.ValuesCoordinate)
        else :
            print("请选择输入文件！")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

```
Slot_PathDisplay.py文件内容如下:
```
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class PathDisplay(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PathDisplay, self).__init__(parent)
        self.graphicsView_PathDisplay = None

    def PlotPathDisplay(self, ValuesCoordinate):
        fig = plt.figure()

        ax = fig.add_subplot(111, projection='3d')

        X = ValuesCoordinate['X']
        Y = ValuesCoordinate['Y']
        Z = ValuesCoordinate['Z']

        ax.set_xlabel('X (mm)')
        ax.set_ylabel('Y (mm)')
        ax.set_zlabel('Z (mm)')

        ax.plot3D(X, Y, Z, 'k--') 

        for i in range(len(X) - 1):
            vector_lengths = np.linalg.norm([X[i + 1] - X[i], Y[i + 1] - Y[i], Z[i + 1] - Z[i]])
            ax.quiver(X[i], Y[i], Z[i], X[i + 1] - X[i], Y[i + 1] - Y[i], Z[i + 1] - Z[i],
                      color='r',normalize = True,length=0.3*vector_lengths)

        ax.scatter(X, Y, Z, c='b', marker='o', alpha=0.5)

        canvas = FigureCanvas(fig)
        layout = QVBoxLayout(self.graphicsView_PathDisplay)
        layout.addWidget(canvas)

        canvas.draw()
```

请修改代码，要求在点击Button_TrajectoryPreview后能够重新读取self.ValuesCoordinate中的数据内容并绘图
'''

import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

import numpy as np

from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class DynamicPlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(dynamic_canvas)
        layout.addWidget(NavigationToolbar(dynamic_canvas, self))

        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._line, = self._dynamic_ax.plot([], [])  # 创建空的Line2D对象
        self.update_plot([])  # 初始化图表内容

    def update_plot(self, data):
        t = np.linspace(0, 10, len(data))
        self._line.set_data(t, data)
        self._dynamic_ax.relim()  # 重新计算数据范围
        self._dynamic_ax.autoscale_view(True, True, True)  # 自动缩放视图
        self._line.figure.canvas.draw()


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QWidget()
        self.setCentralWidget(self._main)
        layout = QVBoxLayout(self._main)

        self.dynamic_plot_widget = DynamicPlotWidget()
        layout.addWidget(self.dynamic_plot_widget)

        self.button = QPushButton("Update Plot")
        layout.addWidget(self.button)

        self.button.clicked.connect(self.update_dynamic_plot)  # 按钮点击事件绑定到方法update_dynamic_plot

    def update_dynamic_plot(self):
        # 这里以随机生成数据作为示例，您可以将您的逻辑放在这个方法里来更新动态图的数据
        data = np.random.rand(100)
        self.dynamic_plot_widget.update_plot(data)


if __name__ == "__main__":
    qapp = QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()

    sys.exit(qapp.exec_())