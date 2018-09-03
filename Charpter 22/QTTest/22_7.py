"""
事件与槽使用代码示例1
"""
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn_close = QPushButton('关闭应用程序', self)
        btn_close.move(100, 60)
        # 按钮点击信号和槽连接
        btn_close.clicked.connect(self.btn_clicked)
        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('事件与槽代码示例')
        self.show()

    def btn_clicked(self):
        sender = self.sender()
        print(sender)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
