#coding=utf8

from Widget.WeaponWidget import WeaponWidget
from Widget.EngineWidget import EngineWidget
from Widget.BuildWidget import BuildWidget

class WidgetManager:
    def __init__(self):
        self.WidgetDict = {}
        self.current = 'weapon'
        self.WidgetDict['weapon'] = WeaponWidget()
        self.WidgetDict['engine'] = EngineWidget()
        self.WidgetDict['engine'].hide()
        self.WidgetDict['build'] = BuildWidget()
        self.WidgetDict['build'].hide()
        

    def getCurrentWidget(self):
        return self.WidgetDict[self.current]

    def changeCurrentWidget(self, name):
        self.WidgetDict[self.current].hide()
        self.WidgetDict[name].setVisible(True)
        self.current = name
