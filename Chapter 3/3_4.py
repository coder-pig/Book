"""
位运算符示例
"""

a = 6
b = 17

print('a 对应的二进制值 %s' % bin(a))
print('b 对应的二进制值 %s' % bin(b))

# & 按位与，两个相应位都为1则为1，否则为0
print('a & b = %s 对应十进制的值为: %d' % (bin(a & b), a & b))

# | 按位或，两个相应位有一个为1，则为1，两个都不为0，才为0
print('a | b = %s 对应十进制的值为: %d' % (bin(a | b), a | b))

# ^ 异或，两个相应位不同为1，相同为0
print('a ^ b = %s 对应十进制的值为: %d' % (bin(a ^ b), a ^ b))

# ~ 按位取反，二进制位取反，0变1，1变0
print('~a = %s 对应十进制的值为：%a' % (bin(~a), ~a))

# << 左移运算符，所有位向左移一定位数，高位丢弃，低位补0
print('a << 2 = %s 对应十进制的值为：%a' % (bin(a << 2), a << 2))

# >> 右移运算符，所有位向右移一定位数
print('a >> 2 = %s 对应十进制的值为：%a' % (bin(a >> 2), a >> 2))
