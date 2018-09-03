"""
菜单栏和工具栏使用示例
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('菜单栏使用示例')
        # 创建一个空的状态栏
        self.statusBar()

        # 创建一个空的菜单栏
        mb = self.menuBar()

        # 为了保持全平台一致要加上这句代码
        mb.setNativeMenuBar(False)

        # 添加菜单项
        fm = mb.addMenu('File')
        ed = mb.addMenu('Edit')
        v = mb.addMenu('View')

        # 为menu创建一个退出的Action
        exit_action = QAction(QIcon('exit.png'), '退出', self)
        exit_action.setShortcut('Ctrl+Q')    # 设置快捷键
        exit_action.setStatusTip('退出程序')    # 状态栏显示提示信息
        exit_action.triggered.connect(qApp.quit)    # 退出程序
        fm.addAction(exit_action)

        # 再添加一个子菜单
        open_action = QAction(QIcon('open.png'), '打开', self)
        fm.addAction(open_action)

        # 添加工具栏
        self.toolbar = self.addToolBar('退出')
        self.toolbar.addAction(exit_action)
        self.toolbar.addAction(open_action)


        self.setGeometry(300, 300, 300, 150)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
