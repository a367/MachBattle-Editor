#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Item.MainList import MainList
from Item.AttrLine import AttrLine, Submit
from Function.DataManager import DataManager
from Item.NameSpace import engine_name_chinese

class EngineList(MainList):
    def __init__(self, viewer):
        MainList.__init__(self)
        self.viewer = viewer
        for name in viewer.getEnginesName():
            self.feedTitle(name)
        self.clicked.connect(self.changeViewer)

    def changeViewer(self, item):
        name = str(item.data().toString())
        self.viewer.displayEngineInformation(name)

    # 设置切换页面
    def feedTitle(self, title):
        item = QListWidgetItem(QIcon('../icon/engine.png'),title)
        item.setSizeHint(QSize(140,40))
        self.addItem(item)



class EngineView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dataManager = DataManager()
        self.information = self.dataManager.getInformation('engine')
        self.setLayout(QHBoxLayout())
        self.lineList = []
        self.engine = None
        self.curFrame = None

    def getEnginesName(self):
        return [engine['name'] for engine in self.information['engines']]

    def displayEngineInformation(self, name):
        self.lineList = []
        frame = QWidget()
        layout = QVBoxLayout()
        for e in self.information['engines']:
            if e['name'] == name:
                self.engine = e
                break
        for name, value in self.engine.iteritems():
            ch_name = engine_name_chinese[name]
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
            self.engine[item_name] = item_value
        
        self.dataManager.saveInformation()
        

class EngineWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.engineView = EngineView()
        self.list = EngineList(self.engineView) 
    
        layout.addWidget(self.list)
        layout.addWidget(self.engineView)

        self.setLayout(layout)
        self.setMinimumWidth(840)



