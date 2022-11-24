class ConfigManger(object):
    __instance = None
    def __init__(self):
        raise RuntimeError('Call instance() instead')
    
    def setSetting(self,key,value):
        self.__settings = dict()
        self.__settings[key] = value
        
    def getSetting(self):
        return self.__settings
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            print('Creating new instance')
            cls.__instance = cls.__new__(cls)
            # Put any initialization here.
        return cls.__instance
    
#********************************************************************

setting1:ConfigManger = ConfigManger.getInstance()
setting1.setSetting("name","yasi")
print(setting1.getSetting())

setting2:ConfigManger = ConfigManger.getInstance()
print(setting2.getSetting())
    