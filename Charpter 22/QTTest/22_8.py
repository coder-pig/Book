"""
事件与槽使用代码示例2
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QSlider, QVBoxLayout




class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber()
        sld = QSlider(Qt.Horizontal, self)

        ly = QVBoxLayout()
        ly.addWidget(lcd)
        ly.addWidget(sld)

        self.setLayout(ly)
        sld.valueChanged[int].connect(self.value_change)
        self.setGeometry(250, 300, 350, 150)
        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('事件与槽代码示例')
        self.show()

    def value_change(self):
        print(self.sender())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
