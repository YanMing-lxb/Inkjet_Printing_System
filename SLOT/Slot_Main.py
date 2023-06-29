# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import QObject, QDir
import pandas as pd

# ----------------------------------------------------------------------
    # 退出应用程序类
# ----------------------------------------------------------------------   
class Quit(QObject):
    def QuitClick(self):
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

# ----------------------------------------------------------------------
    # 文件类
# ----------------------------------------------------------------------   
class File(QObject):
    # 读取Excel文件，获取坐标点三维数组
    def FileRead(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        # 限定文件类型为Excel文件
        dialog.setNameFilter('Excel Files (*.xlsx;*.xls)') 
        if dialog.exec():
            # 获得文件路径
            filepath = dialog.selectedFiles()
            # 读取 Excel 文件
            data_df = pd.read_excel(filepath[0])
            # 将坐标数据保存在 values 中
            values = data_df[['X', 'Y', 'Z']]
            return values

    # 导出喷墨打印的信息
    def FileExport(self):
        print("保存喷墨打印运行数据")



    