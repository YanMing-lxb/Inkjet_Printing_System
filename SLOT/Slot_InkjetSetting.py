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
Date         : 2023-06-26 22:02:20 +0800
LastEditTime : 2023-07-04 15:08:45 +0800
Github       : https://github.com/YanMing-lxb/
FilePath     : \Inkjet_Printing_System\SLOT\Slot_InkjetSetting.py
Description  : 
------------------------------------------------------------------------
'''

from GUI.Ui_InkjetSetting import Ui_Dialog  # 导入自动生成的UI文件Ui_Dialog
from PyQt5 import QtWidgets, QtCore
from SLOT.Slot_WaveformDisplay import RealTimePlot as RTP
from PyQt5.QtGui import QIcon

# ----------------------------------------------------------------------
# 喷墨设置类
# ----------------------------------------------------------------------   
class InkjetSetting(QtWidgets.QWidget):

    def inkjet_setting(self):
# ----------------------------------------------------------------------
        # 喷墨设置对话框类
# ----------------------------------------------------------------------   
        class InkjetSettingDialog(QtWidgets.QDialog, Ui_Dialog,):
            # 构造函数
            def __init__(self):
                super().__init__()
                self.setupUi(self) # 使用Ui_Dialog中的方法创建对话框

                # 设置对话框图标
                icon = QIcon("IPS-Resource/Inkjet-setting.png")  # 替换为你的图标文件的路径
                self.setWindowIcon(icon)

                # ----------------------------------------------------------------------
                    # 将绘制的波形图做成组件添加到对话框中的self.graphicsView组件中
                # ----------------------------------------------------------------------
                self.plot = RTP() # 创建 RealTimePlot 实例
                layout = QtWidgets.QVBoxLayout(self.graphicsView) # 将PlotWidget添加到self.graphicsView中
                layout.setContentsMargins(0, 0, 0, 0)  # 设置边距为0
                layout.addWidget(self.plot.plot_widget)

                # 初始化对话框上的控件值
                self.load_settings()
                
                # 监听输入值的变化，运行槽函数
                self.TimeRise1.valueChanged.connect(self.WaveformDisplay) 
                self.TimeDwell.valueChanged.connect(self.WaveformDisplay)
                self.TimeFall.valueChanged.connect(self.WaveformDisplay)
                self.TimeEcho.valueChanged.connect(self.WaveformDisplay)
                self.TimeRise2.valueChanged.connect(self.WaveformDisplay)
                self.VoltageIdle.valueChanged.connect(self.WaveformDisplay)
                self.VoltageDwell.valueChanged.connect(self.WaveformDisplay)
                self.VoltageEcho.valueChanged.connect(self.WaveformDisplay)

                # 绑定"确定"按钮的信号槽，将其连接到accept函数
                self.buttonBox.accepted.connect(self.accept)
                # 绑定"取消"按钮的信号槽，将其连接到reject函数
                self.buttonBox.rejected.connect(self.reject)

            # 读取之前存储的参数，并将其设置到控件上，并绘制波形图
            def load_settings(self):
                # 获取名为"MyApp"，对应key为"InkjetSettings"的QSettings对象，以便获取之前设置的值
                settings = QtCore.QSettings('YanMing', 'Inkjet Printing')

                # 分别将之前设置的值赋值给控件，如果之前没有设置过，则将其设置为0（默认值）
                self.TimeRise1.setValue(settings.value('TimeRise1', 0))
                self.TimeDwell.setValue(settings.value('TimeDwell', 0))
                self.TimeFall.setValue(settings.value('TimeFall', 0))
                self.TimeEcho.setValue(settings.value('TimeEcho', 0))
                self.TimeRise2.setValue(settings.value('TimeRise2', 0))
                self.VoltageIdle.setValue(settings.value('VoltageIdle', 0))
                self.VoltageDwell.setValue(settings.value('VoltageDwell', 0))
                self.VoltageEcho.setValue(settings.value('VoltageEcho', 0))

                values = [
                    settings.value('TimeRise1', 0), 
                    settings.value('TimeDwell', 0),
                    settings.value('TimeFall', 0), 
                    settings.value('TimeEcho', 0),
                    settings.value('TimeRise2', 0),
                    settings.value('VoltageIdle', 0),
                    settings.value('VoltageDwell', 0),
                    settings.value('VoltageEcho', 0)
                ]
            
                Coordinate = [
                    [0,values[5]],
                    [sum(values[:1]),values[6]],
                    [sum(values[:2]),values[6]],
                    [sum(values[:3]),values[7]],
                    [sum(values[:4]),values[7]],
                    [sum(values[:5]),values[5]]
                ]
                # 绘制波形图
                self.plot.update_graph(Coordinate)




            #将当前设置的值更新到名为"MyApp"，对应key为"InkjetSettings"的QSettings对象
            def save_settings(self):
                # 获取名为"MyApp"，对应key为"InkjetSettings"的QSettings对象，以便保存当前设置的值
                settings = QtCore.QSettings('YanMing', 'Inkjet Printing')

                # 存储所有控件的当前值
                settings.setValue('TimeRise1', self.TimeRise1.value())
                settings.setValue('TimeDwell', self.TimeDwell.value())
                settings.setValue('TimeFall', self.TimeFall.value())
                settings.setValue('TimeEcho', self.TimeEcho.value())
                settings.setValue('TimeRise2', self.TimeRise2.value())
                settings.setValue('VoltageIdle', self.VoltageIdle.value())
                settings.setValue('VoltageDwell', self.VoltageDwell.value())
                settings.setValue('VoltageEcho', self.VoltageEcho.value())

            # 监控数值变化时，被调用来绘制波形图的槽函数
            def WaveformDisplay(self):
                # 获取数值
                values = [
                        self.TimeRise1.value(),
                        self.TimeDwell.value(),
                        self.TimeFall.value(),
                        self.TimeEcho.value(),
                        self.TimeRise2.value(),
                        self.VoltageIdle.value(),
                        self.VoltageDwell.value(),
                        self.VoltageEcho.value()
                    ]
                # 将获取到的数值转换成类型为二维数组的坐标
                Coordinate = [
                    [0,values[5]],
                    [sum(values[:1]),values[6]],
                    [sum(values[:2]),values[6]],
                    [sum(values[:3]),values[7]],
                    [sum(values[:4]),values[7]],
                    [sum(values[:5]),values[5]],
                ]
                # 绘制波形图
                self.plot.update_graph(Coordinate)

                
                

        # 创建InkjetSettingDialog对象
        dialog = InkjetSettingDialog()
        # 显示对话框，等待用户操作完成
        result = dialog.exec_()

        # 如果用户点击对话框内的"确定"按钮
        if result == QtWidgets.QDialog.Accepted:
            # 存储所有控件的当前值
            dialog.save_settings()
            # 获取每个控件的当前值，存储到values列表中
            values = [
                dialog.TimeRise1.value(),
                dialog.TimeDwell.value(),
                dialog.TimeFall.value(),
                dialog.TimeEcho.value(),
                dialog.TimeRise2.value(),
                dialog.VoltageIdle.value(),
                dialog.VoltageDwell.value(),
                dialog.VoltageEcho.value()
            ]
            # 将获取到的数值转换成类型为二维数组的坐标
            Coordinate = [
                [0,values[5]],
                [sum(values[:1]),values[6]],
                [sum(values[:2]),values[6]],
                [sum(values[:3]),values[7]],
                [sum(values[:4]),values[7]],
                [sum(values[:5]),values[5]],
            ]
            # 返回坐标数据
            return Coordinate
            
    