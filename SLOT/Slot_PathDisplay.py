import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np

class PathDisplay(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PathDisplay, self).__init__(parent)
        self.graphicsView_PathDisplay = None

    def PlotPathDisplay(self, ValuesCoordinate):
        # 创建一个Figure对象和一个绘图区域，用于绘制三维线图
        fig = plt.figure()

        ax = fig.add_subplot(111, projection='3d')

        # 从ValuesCoordinate中获取X、Y、Z三维坐标数据
        X = ValuesCoordinate['X']
        Y = ValuesCoordinate['Y']
        Z = ValuesCoordinate['Z']

        # 设置轴标签
        ax.set_xlabel('X (mm)')
        ax.set_ylabel('Y (mm)')
        ax.set_zlabel('Z (mm)')

        # 绘制三维线图
        ax.plot3D(X, Y, Z, 'k--')  # 设置路径颜色为黑色虚线

        # 添加移动方向箭头为红色，大小统一设置为0.5
        for i in range(len(X) - 1):
            # 计算向量长度
            vector_lengths = np.linalg.norm([X[i + 1] - X[i], Y[i + 1] - Y[i], Z[i + 1] - Z[i]])
            ax.quiver(X[i], Y[i], Z[i], X[i + 1] - X[i], Y[i + 1] - Y[i], Z[i + 1] - Z[i],
                      color='r',normalize = True,length=0.3*vector_lengths)

        # 添加蓝色的标记点，透明度设置为0.5
        ax.scatter(X, Y, Z, c='b', marker='o', alpha=0.5)

        # 将绘制的图形显示在graphicsView中
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout(self.graphicsView_PathDisplay)
        layout.addWidget(canvas)

        # 刷新graphicsView显示
        canvas.draw()