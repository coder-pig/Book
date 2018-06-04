"""
身份运算符使用示例
"""

# 普通数据类型
a = 1
b = 1
print('当前a和b引用同一个变量：%s' % (a is b))
# 复杂数据类型(数组)
a = [1]
b = [1]
print('当前a和b引用不同一个变量：%s' % (a is not b))
# 字符串
a = 'python'
b = 'python'
print('当前a和b引用同一个变量：%s' % (a is b))
