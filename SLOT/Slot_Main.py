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
Date         : 2023-06-26 16:13:42 +0800
LastEditTime : 2023-07-03 23:52:59 +0800
Github       : https://github.com/YanMing-lxb/
FilePath     : \Inkjet_Printing_System\SLOT\Slot_Main.py
Description  : 
------------------------------------------------------------------------
'''

from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import QObject, QDir
import pandas as pd
import os
import sys
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

        # 获取程序运行时的当前路径
        current_path = os.path.dirname(sys.argv[0])
        
        # 设置默认打开位置为当前程序所在位置
        dialog.setDirectory(current_path)

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



    