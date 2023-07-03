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
Date         : 2023-06-28 21:44:23 +0800
LastEditTime : 2023-07-03 23:52:29 +0800
Github       : https://github.com/YanMing-lxb/
FilePath     : \Inkjet_Printing_System\SLOT\Slot_WaveformDisplay.py
Description  : 
------------------------------------------------------------------------
'''

import pyqtgraph as pg
from PyQt5 import QtWidgets
import numpy as np

class RealTimePlot(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # 创建PlotWidget
        self.plot_widget = pg.PlotWidget()
        # 创建PlotItem对象
        self.plot_item = self.plot_widget.plotItem
        # 设置图表标题
        self.plot_item.setTitle('喷墨波形')

        # 创建曲线对象
        self.curve = None  # 初始化曲线
        
        # 显示水平和垂直网格
        self.plot_item.showGrid(x=True, y=True)

        # 调用init_graph方法以初始化曲线对象
        self.init_graph()

    def init_graph(self):
        # 设置坐标轴标签
        self.plot_item.setLabel('left', '电压 (V)')
        self.plot_item.setLabel('bottom', '时间 (μs)')

        # 初始化数据
        self.x_data = []
        self.y_data = []

        # 创建曲线
        self.curve = pg.PlotCurveItem(self.x_data, self.y_data)  # 创建PlotCurveItem对象

        # 添加曲线到plot_item
        self.plot_item.addItem(self.curve)

        # 设置范围
        self.plot_item.setXRange(0, 5)  # 设置X轴范围
        self.plot_item.setYRange(-1, 1)  # 设置Y轴范围

    def update_graph(self, values):
        x_coords, y_coords = zip(*values)

        # 更新数据列表
        self.x_data = np.array(x_coords)
        self.y_data = np.array(y_coords)

        # 更新曲线数据
        self.curve.setData(self.x_data, self.y_data)
        self.plot_item.autoRange()  # 自动调整范围