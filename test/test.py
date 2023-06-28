
'''
将pyqtgraph库将图形嵌入在objectname为graphicsView_WaveformDisplay的graphicsView中，values为二维list，每个子list都是一个坐标点，要求waveworm_display方法能够根据values中的坐标数据绘图并将图片嵌入在graphicsView中，纵坐标为电压，单位是V，横坐标是时间，单位为μs。

class WaveformDisplay():
    def __init__(self,values):
      self.values = values
    def waveworm_display(self):
        待写……

Ui_InkjetSetting.py 内为弹窗的gui界面，部分代码如下

```
self.graphicsView.setObjectName("graphicsView")
```
Slot_WaveformDisplay.py 文件内是使用pyqtgraph库绘制的折线图，该文件内的代码如下功能，当该文件内的类或方法被调用时能够在弹窗的gui界面中的graphicsview中嵌入折线图。折线图是根据values内的坐标绘制，values为二维list，每个子list都是一个坐标点。要求该折线图的纵坐标为电压，单位是V，横坐标为时间，单位为μs。

当Slot_InkjetSetting.py 文件中每次调用绘图，都会刷新graphicsview中嵌入的折线图。



请使用pyqtgraph库绘制可以实时更新的二维折线图，要求该折线图的纵坐标为电压，单位是V，横坐标为时间，单位为μs，同时将该图嵌入到对话框中的graphicsview组件中。在对话框中存在一个按钮，每次点击该按钮就会更新折线图






'''
import sys
import pyqtgraph as pg
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QGraphicsView, QGraphicsScene

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # 创建布局
        layout = QVBoxLayout()

        # 创建GraphicsView组件
        self.view = QGraphicsView()
        layout.addWidget(self.view)

        # 创建按钮
        self.button = QPushButton("更新折线图")
        layout.addWidget(self.button)

        # 设置布局
        self.setLayout(layout)

        # 初始化图形
        self.init_graph()

        # 设置按钮的点击事件
        self.button.clicked.connect(self.update_graph)

    def init_graph(self):
        # 创建PlotWidget
        self.plot_widget = pg.PlotWidget()

        # 创建QGraphicsScene
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.plot_widget)

        # 将QGraphicsScene设置为GraphicsView的场景
        self.view.setScene(self.scene)

        # 设置坐标轴标签
        self.plot_widget.setLabel('left', '电压 (V)')
        self.plot_widget.setLabel('bottom', '时间 (μs)')

        # 初始化数据
        self.x_data = []
        self.y_data = []

        # 创建曲线
        self.curve = self.plot_widget.plot(self.x_data, self.y_data)

    def update_graph(self):
        # 模拟更新数据
        import random
        voltage = random.uniform(0, 5)  # 生成随机电压值
        time = len(self.x_data) * 0.1  # 模拟时间增加

        # 更新数据列表
        self.x_data.append(time)
        self.y_data.append(voltage)

        # 更新曲线数据
        self.curve.setData(self.x_data, self.y_data)
        self.plot_widget.setXRange(min(self.x_data), max(self.x_data))  # 根据数据自动调整X轴范围
        self.plot_widget.setYRange(0, 5)  # 设置Y轴范围

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建主界面窗口
    main_window = QDialog()
    main_layout = QVBoxLayout()

    # 创建按钮
    button = QPushButton('打开对话框')
    main_layout.addWidget(button)

    # 设置按钮的点击事件
    dialog = None  # 对话框的引用
    def open_dialog():
        global dialog
        if not dialog:
            dialog = MyDialog()
        dialog.show()
    button.clicked.connect(open_dialog)

    # 设置主界面布局
    main_window.setLayout(main_layout)
    main_window.show()

    sys.exit(app.exec_())




    '''

    ```
    import pyqtgraph as pg

class RealTimePlot:
    def __init__(self, values):
        self.values = values
        self.plot = pg.PlotWidget()

    def init_graph(self):
        # 创建PlotWidget
        self.plot_widget = pg.PlotWidget()

        # 创建QGraphicsScene
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.plot_widget)

        # 将QGraphicsScene设置为GraphicsView的场景
        self.view.setScene(self.scene)

        # 设置坐标轴标签
        self.plot_widget.setLabel('left', '电压 (V)')
        self.plot_widget.setLabel('bottom', '时间 (μs)')

        # 初始化数据
        self.x_data = []
        self.y_data = []

        # 创建曲线
        self.curve = self.plot_widget.plot(self.x_data, self.y_data)

    def update_graph(self,values):

        x_coords, y_coords = zip(values)
        
        # 更新数据列表
        self.x_data = x_coords
        self.y_data = y_coords
        # 更新曲线数据
        self.curve.setData(self.x_data, self.y_data)
        self.plot_widget.setXRange(min(self.x_data), max(self.x_data))  # 根据数据自动调整X轴范围
        self.plot_widget.setYRange(0, 5)  # 设置Y轴范围
    ```
    '''