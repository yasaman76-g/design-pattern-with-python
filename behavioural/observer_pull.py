from abc import ABC,abstractmethod

#these classes are polymorphism class

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass
    
class SpreadSheet(Observer):
    
    def __init__(self,data_source):
        self.__data_source = data_source
        
    def update(self):
        print("Spread shit got notify",self.__data_source.getValue())
    
class Chart(Observer):
    def __init__(self,data_source):
        self.__data_source = data_source
        
    def update(self):
        print("Chart got notify",self.__data_source.getValue())
    
#********************************************************************
#this class has methods need to talk with observer, that every classes need to talk with obsever should inheritance this classes.
class Subject:
    
    def addObserver(self,observer:Observer):
        self.observers = list()
        self.observers.append(observer)
    
    def removeObserver(self,observer:Observer):
        self.observers.remove(observer)
    
    def notifyObservers(self):
        for observer in self.observers:
            observer.update()
#********************************************************************
#primary class to talk with observer when it will changes

class DataSource(Subject):
        
    def setValue(self,value):
        self.__value = value
        self.notifyObservers()
    
    def getValue(self):
        return self.__value
    
#********************************************************************
data_source = DataSource()
sheet1 = SpreadSheet(data_source)
sheet2 = SpreadSheet(data_source)
chart = Chart(data_source)

data_source.addObserver(sheet1)
data_source.addObserver(sheet2)
data_source.addObserver(chart)

data_source.setValue(2)