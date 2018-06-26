"""
批量修改特定文件夹里所有文件中的内容
"""
import os


def replace(dir_path, word_before, word_after):
    file_list = []
    # 遍历获得文件地址
    for f in os.listdir(dir_path):
        file_list.append(os.path.join(dir_path, f))
    # 打开文件，按行读取，替换对应内容
    for file in file_list:
        with open(file, 'r+', encoding='UTF-8') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(word_before, word_after))

if __name__ == '__main__':
    replace(os.path.join(os.getcwd(), 'doc'), 'Java', 'Python')
