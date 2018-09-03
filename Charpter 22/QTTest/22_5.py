"""
垂直布局代码示例
"""
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QVBoxLayout


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.initUI()

    def initUI(self):
        name_label = QtWidgets.QLabel('用户名')
        name_edit = QtWidgets.QLineEdit()
        name_layout = QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_edit)

        pawd_label = QtWidgets.QLabel('密码')
        pawd_edit = QtWidgets.QLineEdit()
        pawd_layout = QHBoxLayout()
        pawd_layout.addWidget(pawd_label)
        pawd_layout.addWidget(pawd_edit)

        root_layout = QVBoxLayout()
        root_layout.addItem(name_layout)
        root_layout.addItem(pawd_layout)
        self.setLayout(root_layout)

        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('垂直布局代码示例')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
