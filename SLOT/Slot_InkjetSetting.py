from GUI.Ui_InkjetSetting import Ui_Dialog  # 导入自动生成的UI文件Ui_Dialog
from PyQt5 import QtWidgets, QtCore

# ----------------------------------------------------------------------
# 喷墨设置类
# ----------------------------------------------------------------------   
class InkjetSetting(QtWidgets.QWidget):

    def inkjet_setting(self):
# ----------------------------------------------------------------------
        # 喷墨设置对话框类
# ----------------------------------------------------------------------   
        class InkjetSettingDialog(QtWidgets.QDialog, Ui_Dialog):
            # 构造函数
            def __init__(self):
                # 调用QDialog的构造函数，初始化
                super().__init__()

                # 使用Ui_Dialog中的方法创建对话框
                self.setupUi(self)
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

            # 读取之前存储的参数，并将其设置到控件上
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

            def WaveformDisplay(self):
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
                print(values)

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
            #print打印列表values
            print(values)
            
            return values
            
    