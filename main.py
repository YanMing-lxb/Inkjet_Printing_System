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
Date         : 2023-06-26 09:52:25 +0800
LastEditTime : 2023-07-04 11:04:56 +0800
Github       : https://github.com/YanMing-lxb/
FilePath     : \Inkjet_Printing_System\main.py
Description  : 
------------------------------------------------------------------------
'''

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

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

# ----------------------------------------------------------------------
    # 打包后资源文件目录访问
# ----------------------------------------------------------------------   
def source_path(relative_path):
    # 是否Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ----------------------------------------------------------------------
    # 主程序
# ----------------------------------------------------------------------   
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup UI
        self.main_ui = UMW()
        self.main_ui.setupUi(self)
        self.setWindowTitle('3D喷墨打印系统')

        icon = QIcon("IPS-Resource/Printing.png")  # 替换为你的图标文件的路径

        self.setWindowIcon(icon)  # 设置窗口图标

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
    # 修改当前工作目录，使得资源文件可以被正确访问
    cd = source_path('')
    os.chdir(cd)


    # 确保脚本在直接运行时才会执行以下代码，而在作为模块导入时不会执行
    app = QApplication(sys.argv)  # 创建一个QApplication实例，作为应用程序的主对象
    window = MyWindow()  # 创建一个自定义窗口对象
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入应用程序的主循环，等待退出信号，然后终止程序并返回退出代码


'''pyinstaller打包命令
pyinstaller -Fw main.py

pyinstaller --onefile --clean main.py
使用上述命令后，PyInstaller将会将你的脚本文件和所有依赖项编译成一个单独的可执行文件，并且自动清除生成的临时文件和缓存文件。

-w:不显示终端
-F:将所有的库打包成一个单独的文件

pyinstaller main.py -wF --icon=Resource_files/Printing.png --add-data Resource_files/Printing.png;Resource_files --add-data Resource_files/Inkjet-setting.png;Resource_files --clean --distpath
'''