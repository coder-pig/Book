"""
QFileDialog使用代码示例
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QTextEdit, QAction, QMainWindow, QFileDialog


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.content_edit = QTextEdit()
        self.setCentralWidget(self.content_edit)
        self.statusBar()
        self.initUI()

    def initUI(self):
        open_file = QAction(QIcon('open.png'), 'Open', self)
        open_file.setStatusTip('打开一个新的文件')
        open_file.setShortcut('Ctrl+O')
        open_file.triggered.connect(self.showDialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&文件')
        file_menu.addAction(open_file)

        self.setWindowTitle('QFileDialog示例')
        self.setWindowIcon(QIcon('duck.png'))
        self.show()

    def showDialog(self):
        # 第二个参数为对话框标题，第二个参数为对话框的工作目录
        fname = QFileDialog.getOpenFileName(self, '打开文件', '/home')
        if fname[0]:
            # 获得文件名，读取文件内容，显示到
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.content_edit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
