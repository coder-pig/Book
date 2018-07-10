"""
组合代码示例
"""


class Book:
    def __init__(self, num):
        self.num = num


class Phone:
    def __init__(self, num):
        self.num = num


class Wallet:
    def __init__(self, num):
        self.num = num


class Bag:
    def __init__(self, x, y, z):
        self.book = Book(x)
        self.phone = Phone(y)
        self.wallet = Wallet(z)

    def show_bag(self):
        print("您的背包里有：【书本】* %d 【手机】* %d 【钱包】* %d" %
              (self.book.num, self.phone.num, self.wallet.num))


if __name__ == '__main__':
    bag = Bag(3, 2, 1)
    bag.show_bag()
