#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Item.MainList import MainList
from Item.AttrLine import AttrLine, Submit
from Function.DataManager import DataManager
from Item.NameSpace import build_name_chinese

class BuildList(MainList):
    def __init__(self, viewer):
        MainList.__init__(self)
        self.viewer = viewer
        for name in viewer.getBuildsName():
            self.feedTitle(name)
        self.clicked.connect(self.changeViewer)

    def changeViewer(self, item):
        name = str(item.data().toString())
        self.viewer.displayBuildInformation(name)

    # 设置切换页面
    def feedTitle(self, title):
        item = QListWidgetItem(QIcon('../icon/build.png'),title)
        item.setSizeHint(QSize(140,40))
        self.addItem(item)


class BuildView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dataManager = DataManager()
        self.information = self.dataManager.getInformation('build')
        self.setLayout(QHBoxLayout())
        self.lineList = []
        self.build = None
        self.curFrame = None

    def getBuildsName(self):
        return [build['name'] for build in self.information['builds']]

    def displayBuildInformation(self, name):
        self.lineList = []
        frame = QWidget()
        layout = QVBoxLayout()
        for b in self.information['builds']:
            if b['name'] == name:
                self.build = b
                break
        for name, value in self.build.iteritems():
            ch_name = build_name_chinese[name]
            line = AttrLine(ch_name, value)
            self.lineList.append({'line':line, 'name':name})
            layout.addWidget(line)
        
        btn = Submit(u'提交修改')
        btn.clicked.connect(self.submit)
        layout.addWidget(btn,0,Qt.AlignHCenter)
        frame.setLayout(layout)

        if self.curFrame != None:
            self.curFrame.deleteLater()
            self.layout().removeWidget(self.curFrame)
        self.layout().addWidget(frame)
        self.curFrame = frame

    def submit(self):
        for m_line in self.lineList:
            line = m_line['line']
            item_name = m_line['name']
            item_value = line.getText()
            self.build[item_name] = item_value
        
        self.dataManager.saveInformation()


class BuildWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        layout = QHBoxLayout()
        self.buildView = BuildView()
        self.list = BuildList(self.buildView) 
    
        layout.addWidget(self.list)
        layout.addWidget(self.buildView)

        self.setLayout(layout)
        self.setMinimumWidth(840)