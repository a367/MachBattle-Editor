#coding=utf8
import json

class DataManager:
    def __init__(self):
        with open('data.json','r') as f:
            self.information = json.loads(f.read())

    def getInformation(self, name):
        return self.information[name]
        
    def setWeaponInformation(self, name, information):
        self.information[name] = information
        with open('data.json', 'w') as f:
            f.write(json.dumps(self.information, ensure_ascii = False))

    def saveInformation(self):
        with open('data.json', 'w') as f:
            f.write(json.dumps(self.information, ensure_ascii = False))