import os
import sys
from PyInstaller.__main__ import run

if __name__ == '__main__':
    sys.argv.append('main.py')
    sys.argv.append('-w')  # 指定为窗口应用程序（无命令行界面）
    sys.argv.append('--icon=ICON/Printing.png')  # 设置主窗口的图标路径
    sys.argv.append('--add-data=ICON/Printing.png')  # 添加 Printing.png 的图标到打包中
    sys.argv.append('--add-data=ICON/Inkjet-setting.png;ICON')  # 添加 Inkjet Setting 的图标到打包中
    sys.argv.append('--clean')  # 清除无用文件
    sys.argv.append('--distpath=.')  # 设置输出目录为当前目录
    run()

# 移动可执行文件到当前目录
dist_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist')
if os.path.exists(dist_dir) and os.path.isdir(dist_dir):
    for file in os.listdir(dist_dir):
        if file.endswith('.exe'):
            src_path = os.path.join(dist_dir, file)
            dest_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
            os.rename(src_path, dest_path)
    os.rmdir(dist_dir)