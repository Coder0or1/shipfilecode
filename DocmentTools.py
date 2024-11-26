import os
import re

# 对文件的高级操作，复制移动等
import shutil

import json
class DocumentToolsClass:
    '''该函数主要将文档里面的用[]标签包裹的校对时添加信息内容进行删除'''

    @staticmethod
    def remove_bracket_content_inplace(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            cleaned_content = re.sub(r'\[.*?\]', '', content)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)
        except FileNotFoundError:
            print("文件不存在。")

    '''该函数实现根据pdf的文件路径，去创建md文件的文件目录结构，
       同时，将别处的md文件，根据pdf的文件名重新命名，且将md文件移动到新创建的文件目录中
    '''

    @staticmethod
    def Create_file_directory_in_Markdown(pdf_file_path, md_file_path):
        # 父级目录的驱动盘
        parentpath = "D:" + os.sep
        # 获得pdf的目录
        Pdf_Path = pdf_file_path

        '''根据pdf的路径创建md文件的文件树'''
        # 对Pdf_Path的目录进行切割，这里使用 os.path.splitdrive 函数来分割路径为驱动器盘符和路径的其余部分
        drive_letter, directory_path = os.path.splitdrive(Pdf_Path)

        # 获取md的文件路径，将pdf的路径与驱动盘D结合，Md_temp_FilePath是定位到md文件的路径。
        Md_temp_FilePath = parentpath + directory_path
        # 获得去除md文件名的文件路径,即该路径定位的是文件目录
        directory_path = os.path.dirname(Md_temp_FilePath)

        """os.path.normpath()函数接收一个路径字符串作为参数，并返回一个规范化后的路径字符串。
            规范化的过程包括去除多余的分隔符、解析相对路径、处理 “.” 和 “..” 等特殊路径表示。
            """
        normalized_path = os.path.normpath(directory_path)

        # 根据pdf的文件路径更新md的文件目录，exist_ok=True 参数确保如果目录已经存在时不会报错。
        os.makedirs(normalized_path, exist_ok=True)

        '''将md文件移动到创建的文件树目录，并根据pdf的名字对md文件进行重命名'''

        # 获取pdf文件名（包含后缀）
        pdf_name_with_extension = os.path.basename(Pdf_Path)

        # 分割pdf文件名和扩展名
        pdf_name, pdf_extension = os.path.splitext(pdf_name_with_extension)

        # 文件移动，shutil.move()方法移动文件时可以实现重命名。
        # destination_file是将md文件移动的目的地
        md_source_file = md_file_path
        md_destination_file = (normalized_path + os.sep + pdf_name + "修改备注版.md")
        # 移动md文件，并进行重命名
        shutil.move(md_source_file, md_destination_file)

        return md_destination_file

    '''该函数将文件复制一份，放入该文件所在的文件目录下的MD_Train文件夹中
    '''

    @staticmethod
    def Create_file_directory_MD_Train(md_trainfile_path):
        src_file = md_trainfile_path

        # 获取修改备注版.md文件名（包含扩展名）
        md_name_with_extension = os.path.basename(md_trainfile_path)

        # 分割修改备注版.md文件名文件名和扩展名
        md_name, md_extension = os.path.splitext(md_name_with_extension)

        dst_file = os.path.dirname(md_trainfile_path) + os.sep + ('md_trainfiles')

        dst_file_name = dst_file + os.sep + md_name + "模型训练版" + md_extension

        # 根据pdf的文件路径更新md的文件目录，exist_ok=True 参数确保如果目录已经存在时不会报错。
        os.makedirs(dst_file, exist_ok=True)

        shutil.copy(src_file, dst_file_name)

        return dst_file_name

    @staticmethod
    def get_key_value_pairs():
        key_value_pairs = {}
        while True:
            key = input("请输入键（输入'quit'结束）: ")
            if key.lower() == 'quit':
                break
            value = input(f"请输入对应的值（键为 {key}）: ")
            key_value_pairs[key] = value

        return key_value_pairs

    @staticmethod
    def save_to_json_file(data, file_path):
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file)
                print(f"数据已成功写入 {file_path}")
        except Exception as e:
            print(f"写入文件时出现错误: {e}")

    @staticmethod
    def Create_file_directory_MD_Json(md_path):
        md_name_with_extension = os.path.basename(md_path)
        md_name, md_extension = os.path.splitext(md_name_with_extension)

        # 使用os.path.join来拼接路径，自动使用正确的路径分隔符（在Windows下是\\）
        dst_file = os.path.join(os.path.dirname(md_path), 'md_Json')
        os.makedirs(dst_file, exist_ok=True)

        # 同样使用os.path.join来拼接文件名到目录路径上
        dst_file_name = os.path.join(dst_file, md_name + '.json')

        return dst_file_name
