"""
可变参数代码示例
"""
def plus(*a):
    result = 0
    for b in a:
        print(b, end='\t')

def test(**a):
    result = 0
    for b in a:
        print(b, end='\t')

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    test(a)
    print()
    plus(*a)
