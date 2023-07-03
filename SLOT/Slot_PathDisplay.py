'''
 =======================================================================
 ····Y88b···d88P················888b·····d888·d8b·······················
 ·····Y88b·d88P·················8888b···d8888·Y8P·······················
 ······Y88o88P··················88888b·d88888···························
 ·······Y888P··8888b···88888b···888Y88888P888·888·88888b·····d88b·······
 ········888······"88b·888·"88b·888·Y888P·888·888·888·"88b·d88P"88b·····
 ········888···d888888·888··888·888··Y8P··888·888·888··888·888··888·····
 ········888··888··888·888··888·888···"···888·888·888··888·Y88b·888·····
 ········888··"Y888888·888··888·888·······888·888·888··888··"Y88888·····
 ·······························································888·····
 ··························································Y8b·d88P·····
 ···························································"Y88P"······
 =======================================================================

Author       : 焱铭
Date         : 2023-06-27 16:02:51 +0800
LastEditTime : 2023-07-03 23:53:16 +0800
Github       : https://github.com/YanMing-lxb/
FilePath     : \Inkjet_Printing_System\SLOT\Slot_PathDisplay.py
Description  : 
------------------------------------------------------------------------
'''

import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class PathDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        # 创建一个FigureCanvas，用于显示图表
        dynamic_canvas = FigureCanvas(Figure(figsize=(8, 6)))
        layout.addWidget(dynamic_canvas)

        # 添加一个导航工具栏，用于操作图表
        layout.addWidget(NavigationToolbar(dynamic_canvas, self))

        # 创建一个3D子图对象
        self.dynamic_ax = dynamic_canvas.figure.add_subplot(111, projection='3d')

        self._line = None  # 初始化线对象

        self.UpdatePathDisplay(pd.DataFrame())  # 初始化图表内容


    def UpdatePathDisplay(self, data):
        if data.empty:
            return

        self._line = None  # 创建新的线对象

        self.dynamic_ax.clear()  # 清空图表

        # 从传入的数据中获取X、Y和Z轴的值
        X = data['X']
        Y = data['Y']
        Z = data['Z']

        # 设置坐标轴标签
        self.dynamic_ax.set_xlabel('X (mm)', color='black')
        self.dynamic_ax.set_ylabel('Y (mm)', color='black')
        self.dynamic_ax.set_zlabel('Z (mm)', color='black')

        # 计算X、Y和Z轴的范围
        x_min, x_max = X.min(), X.max()
        y_min, y_max = Y.min(), Y.max()
        z_min, z_max = np.nanmin(Z), np.nanmax(Z)

        # 设置X、Y和Z轴的显示范围
        self.dynamic_ax.set_xlim(x_min, x_max)
        self.dynamic_ax.set_ylim(y_min, y_max)
        self.dynamic_ax.set_zlim(z_min, z_max)

        # 绘制散点图
        self.dynamic_ax.scatter(X, Y, Z, c='blue', alpha=0.5)

        # 绘制向量箭头
        for i in range(len(X) - 1):
            vector_lengths = np.linalg.norm([X[i + 1] - X[i], Y[i + 1] - Y[i], Z[i + 1] - Z[i]])
            self.dynamic_ax.quiver(X[i], Y[i], Z[i], X[i + 1] - X[i], Y[i + 1] - Y[i],
                                    Z[i + 1] - Z[i], color='red', normalize=True, length=0.5 * vector_lengths)

        if self._line is None:  # 创建线对象
            self._line, = self.dynamic_ax.plot([], [], [], color='black', linestyle='dashed')

        # 更新线对象的数据
        self._line.set_data(X, Y)
        self._line.set_3d_properties(Z)

        num = 6  # 主刻度数目

        # 设置X、Y和Z轴的主刻度
        self.dynamic_ax.set_xticks(np.linspace(x_min, x_max, num=num))
        self.dynamic_ax.set_yticks(np.linspace(y_min, y_max, num=num))
        self.dynamic_ax.set_zticks(np.linspace(z_min, z_max, num=num))

        # 设置X、Y和Z轴的次刻度
        self.dynamic_ax.set_xticks(np.linspace(x_min, x_max, num=num*2-1), minor=True)
        self.dynamic_ax.set_yticks(np.linspace(y_min, y_max, num=num*2-1), minor=True)
        self.dynamic_ax.set_zticks(np.linspace(z_min, z_max, num=num*2-1), minor=True)

        # 显示网格
        self.dynamic_ax.grid(which='both')
        
        # 使用tight_layout()方法调整子图布局
        self.dynamic_ax.figure.tight_layout()

        # 绘制图表
        self.dynamic_ax.figure.canvas.draw()