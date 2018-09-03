"""
QInputDialog使用代码示例
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLabel, QVBoxLayout


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.input_label = QLabel()
        self.show_btn = QPushButton('打开对话框')
        self.resize(300, 200)
        self.initUI()

    def initUI(self):
        root_layout = QVBoxLayout()
        root_layout.addWidget(self.show_btn)
        root_layout.addWidget(self.input_label)
        self.setLayout(root_layout)
        self.show_btn.clicked.connect(self.showDialog)
        self.setWindowTitle('QInputDialog示例')
        self.setWindowIcon(QIcon('duck.png'))
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, '输入对话框', '输入提示语:')
        if ok:
            self.input_label.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
