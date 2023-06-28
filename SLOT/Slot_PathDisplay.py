import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import MultipleLocator

class PathDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        dynamic_canvas = FigureCanvas(Figure(figsize=(8, 6)))
        layout.addWidget(dynamic_canvas)
        layout.addWidget(NavigationToolbar(dynamic_canvas, self))

        self.dynamic_ax = dynamic_canvas.figure.add_subplot(111, projection='3d')
        self._line = None  # 初始化线对象

        self.UpdatePathDisplay(pd.DataFrame())  # 初始化图表内容


    def UpdatePathDisplay(self, data):
        if data.empty:
            return

        self._line = None  # 创建新的线对象

        self.dynamic_ax.clear()  # 清空图表

        X = data['X']
        Y = data['Y']
        Z = data['Z']

        self.dynamic_ax.set_xlabel('X (mm)', color='black')
        self.dynamic_ax.set_ylabel('Y (mm)', color='black')
        self.dynamic_ax.set_zlabel('Z (mm)', color='black')

        x_min, x_max = X.min(), X.max()
        y_min, y_max = Y.min(), Y.max()
        z_min, z_max = np.nanmin(Z), np.nanmax(Z)

        self.dynamic_ax.set_xlim(x_min, x_max)
        self.dynamic_ax.set_ylim(y_min, y_max)
        self.dynamic_ax.set_zlim(z_min, z_max)

        

        # self.dynamic_ax.locator_params(axis='x', nbins=num)
        # self.dynamic_ax.locator_params(axis='y', nbins=num)
        # self.dynamic_ax.locator_params(axis='z', nbins=num)

        self.dynamic_ax.scatter(X, Y, Z, c='blue', alpha=0.5)

        for i in range(len(X) - 1):
            vector_lengths = np.linalg.norm([X[i + 1] - X[i], Y[i + 1] - Y[i], Z[i + 1] - Z[i]])
            self.dynamic_ax.quiver(X[i], Y[i], Z[i], X[i + 1] - X[i], Y[i + 1] - Y[i],
                                    Z[i + 1] - Z[i], color='red', normalize=True, length=0.5 * vector_lengths)

        if self._line is None:  # 创建线对象
            self._line, = self.dynamic_ax.plot([], [], [], color='black', linestyle='dashed')

        self._line.set_data(X, Y)  # 更新线的数据
        self._line.set_3d_properties(Z)

        num = 6 # 主刻度数目

        # 设置主刻度数目
        self.dynamic_ax.set_xticks(np.linspace(x_min, x_max, num=num))
        self.dynamic_ax.set_yticks(np.linspace(y_min, y_max, num=num))
        self.dynamic_ax.set_zticks(np.linspace(z_min, z_max, num=num))

        # 设置次刻度输入
        self.dynamic_ax.set_xticks(np.linspace(x_min, x_max, num=num*2-1), minor=True)
        self.dynamic_ax.set_yticks(np.linspace(y_min, y_max, num=num*2-1), minor=True)
        self.dynamic_ax.set_zticks(np.linspace(z_min, z_max, num=num*2-1), minor=True)


        # 显示网格
        self.dynamic_ax.grid(which='both')
        
        # 调用tight_layout()设置为tight layout模式
        self.dynamic_ax.figure.tight_layout()
        # 绘制图像
        self.dynamic_ax.figure.canvas.draw()