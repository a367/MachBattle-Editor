#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Item.MainList import MainList
from Item.AttrLine import AttrLine, Submit
from Function.DataManager import DataManager
from Item.NameSpace import weapon_name_chinese

class WeaponList(MainList):
    def __init__(self, viewer):
        MainList.__init__(self)
        self.viewer = viewer
        for name in viewer.getWeaponsName():
            self.feedTitle(name)
        self.clicked.connect(self.changeViewer)

    def changeViewer(self, item):
        name = str(item.data().toString())
        self.viewer.displayWeaponInformation(name)

    # 设置切换页面
    def feedTitle(self, title):
        item = QListWidgetItem(QIcon('../icon/weapon.png'),title)
        item.setSizeHint(QSize(140,40))
        self.addItem(item)



class WeaponView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.dataManager = DataManager()
        self.information = self.dataManager.getInformation('weapon')
        self.setLayout(QHBoxLayout())
        self.lineList = []
        self.weapon = None
        self.curFrame = None

    def getWeaponsName(self):
        return [weapon['weapon_name'] for weapon in self.information['weapons']]

    def displayWeaponInformation(self, name):
        self.lineList = []
        frame = QWidget()
        layout = QVBoxLayout()
        for w in self.information['weapons']:
            if w['weapon_name'] == name:
                self.weapon = w
                break
        for name, value in self.weapon.iteritems():
            ch_name = weapon_name_chinese[name]
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
            self.weapon[item_name] = item_value
        
        self.dataManager.saveInformation()
            
            
        

class WeaponWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.weaponView = WeaponView()
        self.list = WeaponList(self.weaponView) 
    
        layout.addWidget(self.list)
        layout.addWidget(self.weaponView)

        self.setLayout(layout)
        self.setMinimumWidth(840)



