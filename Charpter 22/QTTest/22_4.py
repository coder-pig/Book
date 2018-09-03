"""
水平布局代码示例
"""
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QDesktopWidget, QLayout


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.initUI()

    def initUI(self):
        name_label = QtWidgets.QLabel('用户名')
        name_edit = QtWidgets.QLineEdit()

        h_box = QHBoxLayout(self)
        h_box.addWidget(name_label)
        h_box.addWidget(name_edit)
        self.setLayout(h_box)

        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('水平布局代码示例')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
