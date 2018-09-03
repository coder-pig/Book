"""
网格布局代码示例
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        keys = ['AC', '+/-', '%', '/',
                '7', '8', '9', '*',
                '4', '5', '6', '-',
                '1', '2', '3', '+']
        positions = [(i, j) for i in range(4) for j in range(4)]
        for position, key in zip(positions, keys):
            print(position, key)
            button = QPushButton(key)
            grid.addWidget(button, *position)
        grid.addWidget(QPushButton('0'), 4, 0, 1, 2)
        grid.addWidget(QPushButton('.'), 4, 2)
        grid.addWidget(QPushButton('='), 4, 3)
        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('网格布局代码示例')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
