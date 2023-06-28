import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# ----------------------------------------------------------------------
    # 导入GUI主窗口界面库
# ----------------------------------------------------------------------   
from GUI.Ui_MainWindow import Ui_MainWindow

# ----------------------------------------------------------------------
    # 导入槽函数库
# ----------------------------------------------------------------------   
from SLOT.Slot_Main import Quit, File
from SLOT.Slot_InkjetSetting import InkjetSetting
from SLOT.Slot_PathDisplay import PathDisplay

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup UI
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.setWindowTitle('3D喷墨打印控制系统')

        self.ValuesCoordinate = None # 读取到的坐标数据初值为空
        self.ValueWaveForm = None # 波形数据初值为空

        # ----------------------------------------------------------------------
            # 将路径图作为组件添加到PathDisplay中
        # ----------------------------------------------------------------------
        self.PathDisplay= PathDisplay()
        self.main_ui.PathDisplay.addWidget(self.PathDisplay)
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
        file = File()
        self.ValuesCoordinate = file.FileRead()
        if self.ValuesCoordinate is not None: # 如果读取到数值，则让 轨迹预览 按钮可用
            self.main_ui.Button_TrajectoryPreview.setEnabled(True)
    
    # 加载显示路径的槽函数
    def path_display(self):
        if self.ValuesCoordinate is not None:
            self.PathDisplay.UpdatePathDisplay(self.ValuesCoordinate)
        else :
            print("请选择输入文件！")
    
    # 加载喷墨设置的槽函数
    def injet_setting(self):
        inkjetsetting = InkjetSetting()
        self.ValueWaveForm = inkjetsetting.inkjet_setting()
        if self.ValueWaveForm is not None: # 如果得到ValueWaveForm数据，则让 导出 按钮可用
            self.main_ui.Button_FileExport.setEnabled(True)

    # 加载导出文件的槽函数
    def file_export(self):
        file = File()
        file.FileExport()
    
    # 加载退出程序的槽函数
    def quit(self):
        quit_ = Quit()
        quit_.QuitClick()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())