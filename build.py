import sys
from PyInstaller.__main__ import run
import shutil
import os

def del_file(file):
    # 检查文件是否存在
    if os.path.exists(file):
        # 删除文件
        os.remove(file)
        print(f"{file}删除成功！")
    else:
        print(f"{file}不存在！")

if __name__ == '__main__':
    


    sys.argv.append('main.py')
    sys.argv.append('-w')  # 指定为窗口应用程序（无命令行界面）
    sys.argv.append('--icon=ICON/Printing.png')  # 设置主窗口的图标路径
    sys.argv.append('--add-data=ICON/Printing.png;ICON')  # 添加 Printing.png 的图标到打包中
    sys.argv.append('--add-data=ICON/Inkjet-setting.png;ICON')  # 添加 Inkjet Setting 的图标到打包中
    sys.argv.append('--clean')  # 清除无用文件
    # sys.argv.append('--distpath=.')  # 设置输出目录为当前目录
    sys.argv.append('--onefile')  # 生成单个可执行文件
    run()


    # 将main.exe文件重命名为"喷墨打印系统"
    dist_folder = 'dist'
    main_exe = 'main.exe'
    new_name = '喷墨打印系统 v1.0.exe'

    main_exe_path = os.path.join(dist_folder, main_exe)
    new_main_exe_path = os.path.join(os.getcwd(), new_name)

    os.rename(main_exe_path, new_main_exe_path)

    # 移动main.exe文件到根目录下
    shutil.move(new_main_exe_path, new_name)

    # 删除dist文件夹和build文件夹
    shutil.rmtree(dist_folder)
    shutil.rmtree('build')


    del_file("main.exe")
    del_file("main.spec")