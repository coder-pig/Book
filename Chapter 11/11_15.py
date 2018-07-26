"""
进程池实现文件行数和字数统计脚本实例
"""
import multiprocessing as mp
import time
import os

result_file = 'result.txt'  # 统计结果写入文件名


# 获得路径下的文件列表
def get_files(path):
    file_list = []
    for file in os.listdir(path):
        if file.endswith('py'):
            file_list.append(os.path.join(path, file))
    return file_list


# 统计每个文件中函数与字符数
def get_msg(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.readlines()
        f.close()
        lines = len(content)
        char_count = 0
        for i in content:
            char_count += len(i.strip("\n"))
        return lines, char_count, path


# 将数据写入到文件中
def write_result(result_list):
    with open(result_file, 'a', encoding='utf-8') as f:
        for result in result_list:
            f.write(result[2] + " 行数：" + str(result[0]) + " 字符数：" + str(result[1]) + "\n")
        f.close()


if __name__ == '__main__':
    start_time = time.time()
    file_list = get_files(os.getcwd())
    pool = mp.Pool()
    result_list = pool.map(get_msg, file_list)
    pool.close()
    pool.join()
    write_result(result_list)
    print("处理完毕，用时：", time.time() - start_time)
