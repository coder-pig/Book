"""
递归求和示例
"""
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

print("1到100的求和结果是: %d" % sum(100))