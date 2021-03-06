"""
字符串格式化函数format使用示例
"""
# 位置参数
str1 = "{0}生{1}，{2}{3}！".format("人", "苦短", "我用", "Python")
print(str1)

# 关键字参数
str1 = "{a}生{c}，{b}{d}！".format(a="人", c="苦短", b="我用", d="Python")
print(str1)

# 位置参数可以与关键字参数一起使用，不过位置参数需要在关键字参数前，否则会报错！

# 另外还有个叫替换域的东西，冒号代表格式化符号开始，比如下面的例子：
str1 = "{0}:{1:.4}".format("圆周率", 3.1415926)
print(str1)
