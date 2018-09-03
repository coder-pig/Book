"""
底部状态栏使用示例
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('已就绪')
        self.setGeometry(300, 300, 300, 150)
        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('底部状态栏使用示例')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
