"""
QColorDialog使用代码示例
"""
import sys

from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.frm = QFrame(self)
        self.btn = QPushButton('打开对话框', self)
        self.initUI()

    def initUI(self):
        # 设置初始颜色为黑色
        col = QColor(0, 0, 0)
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.showDialog)

        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 300, 180)
        self.setWindowTitle('QColorDialog示例')
        self.setWindowIcon(QIcon('duck.png'))
        self.show()

    def showDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"% color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
