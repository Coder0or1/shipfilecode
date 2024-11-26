import subprocess
import time

import os
# 在 Python 中可以使用tkinter库来实现弹出一个对话框让用户选择文件。
import tkinter as tk
from tkinter import filedialog

import sys

# 导入自定义的工具类
from DocmentTools import DocumentToolsClass

print("欢迎使用文档修改校对系统。")
print("")
print("----------------------------------------------")
print("功能1转换：将转换的MD文件放入MD文件目录中")
print("功能2提取文件：输出去除标签后法规文件的MD文件路径")
print("功能3对md文件进行修改：对要修改的md文件进行一些修改")
print("功能4对md文件进行修改时：元信息的输入，保存为Json文件")
print("请输入对应的功能数字，进入对应功能。")
print("输入其它任意数字则退出该系统。")
print("----------------------------------------------")
print("")

loge = True

while True:
    button = int(input("如果继续使用该系统，请输入功能数字："))
    if button == 1 or button == 2 or button == 3 or button == 4:
        loge = True
    else:
        break
    while loge:
        if button == 1:
            print("请在弹框中选择pdf的文件路径")

            while True:
                # 弹出框选择pdf的文件的路径
                # 创建一个Tk实例root，它代表主窗口。
                root1 = tk.Tk()
                # 使用root.withdraw()隐藏主窗口，这样只显示文件选择对话框而不显示额外的主窗口。
                root1.withdraw()
                # filedialog.askopenfilename()弹出一个文件选择对话框，让用户选择一个文件。它返回用户选择的文件的路径。
                pdf_file_path = filedialog.askopenfilename()

                print("pdf的文件地址为：" + pdf_file_path)

                answer = input("你当前所选择的 “pdf文件”  “是否为” 该文件路径下的文件吗？请输入 “是或者否” ：")
                if answer == "是":
                    break
                else:
                    print("请在弹框中选择正确pdf的文件路径")

            print("请在弹框中选择md的文件路径")

            while True:
                # 弹出框选择md的文件的路径
                root2 = tk.Tk()
                root2.withdraw()
                md_file_path1 = filedialog.askopenfilename()

                print("md的文件地址为：" + md_file_path1)

                answer = input("你当前所选择的 “md文件”  “是否为” 该文件路径下的文件吗？请输入 “是或者否” ：")
                if answer == "是":
                    break
                else:
                    print("请在弹框中选择正确md的文件路径")

            # 对选中文件的路径进行格式规格化
            normalized_pdf_path = os.path.normpath(pdf_file_path)
            ormalized_md_path = os.path.normpath(md_file_path1)

            # 创建md的文件目录，并将md文件移动到该目录下,返回md文件的新路径
            md_path = DocumentToolsClass.Create_file_directory_in_Markdown(normalized_pdf_path, ormalized_md_path)

            # 参数是文件所在地址+可执行文件.exe
            # 在 Python 中使用subprocess模块打开其他软件 并 传入文件路径作为参数。
            # 在md文件的新路径下，打开Typora.exe执行程序
            process1 = subprocess.Popen(["C:\\Program Files\\Typora\\Typora.exe", md_path])

            process2 = subprocess.Popen(
                ["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe", normalized_pdf_path])

            # 退出二层while时的条件，“进入如果继续使用该系统，请输入功能数字：”的选择
            break

        if button == 2:
            print("请在弹框中选择需要去除md文件备注标签的文件路径：")

            while True:
                # 弹出框选择md的文件的路径
                root3 = tk.Tk()
                root3.withdraw()
                md_file_path2 = filedialog.askopenfilename()

                print("md的文件地址为：" + md_file_path2)

                answer = input("你当前所选择的 “md文件”  “是否为” 该文件路径下的文件吗？请输入 “是或者否” ：")
                if answer == "是":
                    break
                else:
                    print("请在弹框中选择正确md的文件路径")

            md_train_path = DocumentToolsClass.Create_file_directory_MD_Train(md_file_path2)

            DocumentToolsClass.remove_bracket_content_inplace(md_train_path)
            print("该路径下的模型训练版md文件：" + md_train_path + "的备注标签已去除。")
            # 退出二层while时的条件，“进入如果继续使用该系统，请输入功能数字：”的选择
            break

        if button == 3:
            print("请在弹框中选择要对md文件进行一些修改的文件路径：")

            while True:
                # 弹出框选择md的文件的路径
                root4 = tk.Tk()
                root4.withdraw()
                md_file_path3 = filedialog.askopenfilename()

                print("md的文件地址为：" + md_file_path3)

                answer = input("你当前所选择的 “md文件”  “是否为” 该文件路径下的文件吗？请输入 “是或者否” ：")
                if answer == "是":
                    process3 = subprocess.Popen(["C:\\Program Files\\Typora\\Typora.exe", md_file_path3])

                else:
                    print("请在弹框中选择正确md的文件路径")

                break
            # 退出二层while时的条件，“进入如果继续使用该系统，请输入功能数字：”的选择
            break

        if button == 4:
            print("请在弹框中选择要对md文件进行一些修改的文件路径：")

            while True:
                # 弹出框选择md的文件的路径
                root5 = tk.Tk()
                root5.withdraw()
                md_file_path4 = filedialog.askopenfilename()

                print("md的文件地址为：" + md_file_path4)

                answer = input("你当前所选择的 “md文件”  “是否为” 该文件路径下的文件吗？请输入 “是或者否” ：")
                if answer == "是":
                    json_data = DocumentToolsClass.get_key_value_pairs()
                    json_path = DocumentToolsClass.Create_file_directory_MD_Json(md_file_path4)
                    DocumentToolsClass.save_to_json_file(json_data , json_path)
                else:
                    print("请在弹框中选择正确md的文件路径")

                break
            # 退出二层while时的条件，“进入如果继续使用该系统，请输入功能数字：”的选择
            break

print("退出程序")
sys.exit()
