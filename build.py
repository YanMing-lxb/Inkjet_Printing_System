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
Date         : 2023-06-29 15:45:39 +0800
LastEditTime : 2023-07-03 23:58:27 +0800
Github       : https://github.com/YanMing-lxb/
FilePath     : \Inkjet_Printing_System\build.py
Description  : 
------------------------------------------------------------------------
'''

from PyInstaller.__main__ import run
import shutil
import os

def build_pyinstaller(exe_name, icon_pic):
    args1 = [
        'main.py',  # 要打包的主程序文件
        '-w',  # 指定为窗口应用程序（无命令行界面）
        f'--icon=Resource_files/{icon_pic}',  # 设置主窗口的图标路径，使用 icon_pic 参数作为图标文件
        '--add-data=Resource_files;Resource_files',  # 将 Resource_files 文件夹中的所有文件添加到可执行文件中
        '--onefile',  # 生成单个可执行文件
        '--clean',
        f'--name={exe_name}'  # 指定可执行文件的名称，使用 exe_name 参数作为可执行文件名
    ]

    args2 = [
        exe_name+".spec"
    ]

    run(args1)
    run(args2)

def del_file(file):
    # 检查文件是否存在
    if os.path.exists(file):
        # 删除文件
        os.remove(file)
        print(f"{file}删除成功！")
    else:
        print(f"{file}不存在！")

def move_file(src_folder, file_name, des_folder):
    src_file_path = os.path.join(src_folder, file_name +'.exe')  # 源文件路径
    des_file_path = os.path.join(des_folder, file_name+'.exe')  # 目标文件路径

    # 移动文件
    shutil.move(src_file_path, des_file_path)
    print(f"已将文件 {file_name}.exe 从{src_folder}移动到 {des_folder} 文件夹。")


if __name__ == '__main__':
    # 设置参数
    file_name = '3D喷墨打印系统 v1.0'  # 可执行文件名
    src_folder = 'dist'  # 源文件夹路径
    des_folder = 'Releases'  # 目标文件夹路径
    icon_pic = 'Printing.png'  # 图标文件名

    build_pyinstaller(file_name, icon_pic)  # 调用方法编译生成可执行文件

    move_file(src_folder, file_name, des_folder)  # 移动文件到目标文件夹

    # 删除不需要的文件和文件夹
    shutil.rmtree(src_folder)  # 删除 dist 文件夹
    shutil.rmtree('build')  # 删除 build 文件夹
    del_file(f"{file_name}.spec")  # 删除 .spec 文件

