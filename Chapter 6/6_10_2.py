"""
自定义迭代器对象示例
"""


class MyIterator():
    def __init__(self, names):
        self.names = names
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.names):
            raise StopIteration("已到达末尾")
        else:
            self.index += 1
            return self.names[self.index - 1]


iterator = MyIterator([1, 2, 3, 4, 5])
for i in iterator:
    print(i, end='\t')
