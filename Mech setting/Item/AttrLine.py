#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AttrLabel(QLabel):
    def __init__(self, name):
        super(AttrLabel, self).__init__(name)
        self.setFont(QFont(u"微软雅黑",13))

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(QPalette.WindowText,QColor(255,255,255))
        p.setColor(QPalette.Background,QColor(34,34,34))

        self.setPalette(p)
        self.setMaximumWidth(100)
        self.setMinimumWidth(100)

class AttrEdit(QLineEdit):
    def __init__(self, name):
        name = str(name).decode('utf8')
        super(AttrEdit, self).__init__(name)
        self.setFont(QFont(u"微软雅黑",13))



class AttrLine(QWidget):
    def __init__(self, name, value):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        self.attrEdit = AttrEdit(value)
        layout.addWidget(AttrLabel(name))
        layout.addWidget(self.attrEdit)
        self.setLayout(layout)

    def getText(self):
        return str(self.attrEdit.text())


class Submit(QPushButton):
    def __init__(self, name):
        QPushButton.__init__(self, name)

        self.setAutoFillBackground(True)
        self.setFont(QFont(u"微软雅黑",13))
        p = self.palette()
        p.setColor(QPalette.WindowText,QColor(255,255,255))
        p.setColor(QPalette.Background,QColor(34,34,34))

        self.setPalette(p)
        self.setMaximumSize(200,30)
        self.setMinimumSize(200,30)

        