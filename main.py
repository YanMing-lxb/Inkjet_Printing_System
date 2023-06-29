import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

# ----------------------------------------------------------------------
    # 导入GUI主窗口界面库
# ----------------------------------------------------------------------   
from GUI.Ui_MainWindow import Ui_MainWindow as UMW

# ----------------------------------------------------------------------
    # 导入槽函数库
# ----------------------------------------------------------------------   
from SLOT.Slot_Main import Quit, File
from SLOT.Slot_InkjetSetting import InkjetSetting as IJS
from SLOT.Slot_PathDisplay import PathDisplay as PD
from SLOT.Slot_WaveformDisplay import RealTimePlot as RTP

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup UI
        self.main_ui = UMW()
        self.main_ui.setupUi(self)
        self.setWindowTitle('3D喷墨打印控制系统')

        self.ValuesCoordinate = None # 读取到的坐标数据初值为空
        self.ValueWaveForm = None # 波形数据初值为空

        # ----------------------------------------------------------------------
            # 将路径图作为组件添加到主UI界面的self.PathDisplay组件中
        # ----------------------------------------------------------------------
        self.PathDisplay= PD()
        self.main_ui.PathDisplay.addWidget(self.PathDisplay)

        # ----------------------------------------------------------------------
            # 将绘制的波形图做成组件添加到主UI界面的self.graphicsView_WaveformDisplay组件中
        # ----------------------------------------------------------------------
        # 创建 RealTimePlot 实例
        self.plot = RTP()
        # 将PlotWidget添加到self.graphicsView中
        layout = QtWidgets.QVBoxLayout(self.main_ui.graphicsView_WaveformDisplay)
        layout.setContentsMargins(0, 0, 0, 0)  # 设置边距为0
        layout.addWidget(self.plot.plot_widget)

        # ----------------------------------------------------------------------
            # 链接槽函数
        # ----------------------------------------------------------------------
        self.main_ui.Button_Quit.clicked.connect(self.quit)  # 链接 退出 按钮
        self.main_ui.Button_FileRead.clicked.connect(self.file_read)  # 链接 读取文件 按钮
        self.main_ui.Button_FileExport.clicked.connect(self.file_export)# 链接 导出 按钮
        self.main_ui.Button_TrajectoryPreview.clicked.connect(self.path_display) # 链接 轨迹预览 按钮
        self.main_ui.Button_InkjetSetting.clicked.connect(self.injet_setting) # 链接 喷墨设置 按钮

    # ----------------------------------------------------------------------
        # 加载槽函数
    # ----------------------------------------------------------------------
    # 加载读取文件的槽函数
    def file_read(self):
        file = File() # 初始化文件类
        self.ValuesCoordinate = file.FileRead() # 将从excel文件中读取的路径数据赋予self.ValuesCoordinate参数
        if self.ValuesCoordinate is not None:
            self.main_ui.Button_TrajectoryPreview.setEnabled(True) # 让 轨迹预览 按钮可用
    
    # 加载显示路径的槽函数
    def path_display(self):
        if self.ValuesCoordinate is not None: # 如果读取到路径数据，则显示路径
            self.PathDisplay.UpdatePathDisplay(self.ValuesCoordinate) # 根据路径数据绘制路径图
        else :
            print("请选择输入文件！")
    
    # 加载喷墨设置的槽函数
    def injet_setting(self):
        inkjetsetting = IJS() # 初始化喷墨设置
        self.ValueWaveForm = inkjetsetting.inkjet_setting() # 将从弹窗中读到的波形数据赋予self.ValueWaveForm参数
        if self.ValueWaveForm is not None: 
            self.plot.update_graph(self.ValueWaveForm) # 绘制主界面的波形图
            self.main_ui.Button_FileExport.setEnabled(True) # 让 导出 按钮可用

    # 加载导出文件的槽函数
    def file_export(self):
        file = File() # 初始化文件类
        file.FileExport() # 导出文件
    
    # 加载退出程序的槽函数
    def quit(self):
        quit_ = Quit() # 初始化退出类
        quit_.QuitClick()

# ----------------------------------------------------------------------
    # 加载槽函数
# ----------------------------------------------------------------------

if __name__ == '__main__':
    # 确保脚本在直接运行时才会执行以下代码，而在作为模块导入时不会执行
    app = QApplication(sys.argv)  # 创建一个QApplication实例，作为应用程序的主对象
    window = MyWindow()  # 创建一个自定义窗口对象
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入应用程序的主循环，等待退出信号，然后终止程序并返回退出代码