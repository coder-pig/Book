"""
列表遍历示例
"""
num_list = [0, 1, 2, 3, 4, 5]

for num in num_list:
    print(num, end='\t')

print()

for index in range(0, len(num_list)):
    print(num_list[index], end='\t')

print()

for index, value in enumerate(num_list):
    print('index = %d values = %d' % (index, value))
