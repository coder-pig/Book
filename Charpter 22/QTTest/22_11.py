"""
QFontDialog使用代码示例
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog, QLabel, QVBoxLayout


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('打开对话框', self)
        self.label = QLabel('字体设置测试')
        self.initUI()

    def initUI(self):
        # 设置初始颜色为黑色
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.showDialog)
        self.setGeometry(300, 300, 300, 150)

        root_layout = QVBoxLayout()
        root_layout.addWidget(self.btn)
        root_layout.addWidget(self.label)
        self.setLayout(root_layout)

        self.setWindowTitle('QFontDialog示例')
        self.setWindowIcon(QIcon('duck.png'))
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
