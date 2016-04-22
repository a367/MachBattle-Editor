#coding=utf8
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolBtn(QToolButton):
    def __init__(self, icon, name):
        QPushButton.__init__(self)
        self.setIcon(icon)
        self.setText(name)
        self.setFont(QFont(u"微软雅黑",10))
        self.setIconSize(QSize(40,50))
        self.setCheckable(True)
        self.setAutoExclusive(True)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        p = self.palette()
        p.setColor(QPalette.ButtonText,QColor(255,255,255))
        self.setPalette(p)




class ToolBar(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.setStyleSheet(open("../qss/ToolBarStyle.qss",'r').read())
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(QPalette.Background,QColor(49,49,49))
        self.setPalette(p)


        btn_weapon = ToolBtn(QIcon("../icon/weapon.png"), u"武器")
        btn_weapon.setChecked(True)
        btn_weapon.clicked.connect(lambda: self.changeFrame('weapon'))

        btn_engine = ToolBtn(QIcon("../icon/engine.png"), u"引擎")
        btn_engine.clicked.connect(lambda: self.changeFrame('engine'))

        btn_build = ToolBtn(QIcon("../icon/build.png"), u"建筑")
        btn_build.clicked.connect(lambda: self.changeFrame('build'))

        layout = QHBoxLayout()

        layout.addWidget(btn_weapon)
        layout.addWidget(btn_engine)
        layout.addWidget(btn_build)
        layout.setMargin(0)
        layout.setSpacing(0)

        self.setLayout(layout)       
        self.setMaximumHeight(65)
        self.setMinimumHeight(65)
       
    def changeFrame(self, name):
        self.widgetMgr.changeCurrentWidget(name)

    def setWidgetManager(self, widgetManager):
        self.widgetMgr = widgetManager