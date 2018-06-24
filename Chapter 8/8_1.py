"""
文件基础操作示例
"""


# 1.创建一个可读写的文件
def mk_file(file):
    with open(file, 'w+', encoding='UTF-8') as f:
        print("创建了一个可读写的文件：%s" % file)


# 2.往文件中写入内容
def write_to_file(file, content):
    with open(file, 'w+', encoding='UTF-8') as f:
        f.write(content + '\n')
        print("内容写入成功！")


# 3.读取文件里的内容
def read_from_file(file):
    with open(file, 'r+', encoding='UTF-8') as f:
        print("输出文件内容：" + f.read())


# 4.往文件追加内容
def append_to_file(file, content):
    with open(file, 'a+', encoding='UTF-8') as f:
        f.write(content + '\n')
        print("内容追加成功！")


if __name__ == '__main__':
    file_name = 'test.txt'
    mk_file(file_name)
    write_to_file(file_name, "人生苦短我用Python！")
    read_from_file(file_name)
    append_to_file(file_name, "Hello Python！")
    read_from_file(file_name)
