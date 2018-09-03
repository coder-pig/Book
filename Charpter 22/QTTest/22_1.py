import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    # 1.pyqt5程序都需要创建一个应用程序对象（必须），参数是从命令行获取输入参数，列表类型
    app = QApplication(sys.argv)

    # 2.QWidget组件是所有用户界面对象的父类，
    w = QWidget()

    # 3.resize函数，用于调整窗口大小，参数为宽高
    w.resize(250, 250)

    # 4.move函数，移动窗口在屏幕的位置，参数为x,y轴坐标
    # w.move(300, 300)

    # 5.setWindowTitle()函数，用于设置窗口标题
    w.setWindowTitle("Hello PyQt5")

    # 修改图标
    w.setWindowIcon(QIcon('duck.png'))

    # 让窗口显示在屏幕中心
    # 获得窗口
    qr = w.frameGeometry()
    # 获得屏幕中心点
    cp = QDesktopWidget().availableGeometry().center()
    # 显示到屏幕中心
    qr.moveCenter(cp)
    w.move(qr.topLeft())

    # 6.show()显示到屏幕上
    w.show()

    # 7.调用系统的exit函数，保证程序完全退出
    sys.exit(app.exec_())
