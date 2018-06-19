"""
批量文件命名脚本
"""
import os


def rename(file_dir, model_name, file_type):
    pos = 1
    # 获取文件夹下所有文件(包括文件夹)
    file_list = os.listdir(file_dir)
    for file in file_list:
        # 判断是否为对应后缀的文件
        if file.endswith(file_type):
            try:
                # 旧文件名
                old_name = os.path.join(file_dir, file)
                # 新文件名
                new_name = os.path.join(file_dir, model_name + str(pos) + file_type)
                os.rename(old_name, new_name)
                pos = pos + 1
            except:
                continue


rename(os.path.join(os.getcwd(), 'res'), 'image_', '.png')
