"""
PyQt5实战示例：编写一个简易小说阅读器
"""
import sys

from PyQt5 import sip
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests as r
from bs4 import BeautifulSoup

bqk_base_url = 'http://www.biqukan.com/'
bqk_search_base_url = 'http://www.biqukan.com/' + 's.php'


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.novel_dict = {}
        # 界面初始化
        self.resize(720, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 501, 31))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.horizontalLayout.addWidget(self.pushButton)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 70, 191, 491))
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 70, 421, 491))
        self.horizontalLayoutWidget.raise_()
        self.lineEdit.raise_()
        self.listWidget.raise_()
        self.textEdit.raise_()
        self.setCentralWidget(self.centralwidget)
        self.initUI()
        QtCore.QMetaObject.connectSlotsByName(self)

    def initUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "加载"))
        self.setWindowIcon(QIcon('duck.png'))
        self.setWindowTitle('简易小说阅读器')
        self.pushButton.clicked.connect(self.search_click)
        self.listWidget.currentTextChanged.connect(self.list_item_click)
        self.show()

    # 加载按钮被点击
    def search_click(self):
        self.fetch_novel_list(self.lineEdit.text())

    # 更新列表
    def update_list(self):
        self.listWidget.addItems(self.novel_dict.keys())

    # 列表item被点击
    def list_item_click(self, text):
        self.textEdit.setText(self.fetch_content(self.novel_dict.get(text)))

    # 获取小说内容
    def fetch_content(self, url):
        resp = r.get(url).text
        bs = BeautifulSoup(resp, 'lxml')
        showtxt = bs.find('div', attrs={'class': 'showtxt'}).text
        return showtxt

    # 获取小说每一章的链接
    def fetch_novel_list(self, novel_name):
        resp = r.get(bqk_search_base_url, params={'ie': 'gbk', 's': '2758772450457967865', 'q': novel_name})
        search_bs = BeautifulSoup(resp.text, 'lxml')
        div_p10 = search_bs.find("div", attrs={'class': 'p10'})
        if div_p10 is not None:
            article_url = bqk_base_url[:-1] + div_p10.find("div").find("a").get('href')
            article_resp = r.get(article_url).text
            article_bs = BeautifulSoup(article_resp, 'lxml')
            a_s = article_bs.find('div', attrs={'class': 'listmain'}).findAll('a')[12:]
            for a in a_s:
                self.novel_dict[a.text] = bqk_base_url[:-1] + a.get('href')
            self.update_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())
