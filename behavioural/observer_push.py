from abc import ABC,abstractmethod

#these classes are polymorphism class

class Observer(ABC):
    @abstractmethod
    def update(self,value:int):
        pass
    
class SpreadSheet(Observer):
    def update(self,value:int):
        print("Spread shit got notify",value)
    
class Chart(Observer):
    def update(self,value:int):
        print("Chart got notify",value)
    
#********************************************************************
#this class has methods need to talk with observer, that every classes need to talk with obsever should inheritance this classes.
class Subject:
    observers = list()
    
    def addObserver(self,observer:Observer):
        self.observers.append(observer)
    
    def removeObserver(self,observer:Observer):
        self.observers.remove(observer)
    
    def notifyObservers(self,value:int):
        for observer in self.observers:
            observer.update(value)
#********************************************************************
#primary class to talk with observer when it will changes

class DataSource(Subject):
    __value = '' 
    
    def setValue(self,value):
        self.__value = value
        self.notifyObservers(self.__value)
    
    def getValue(self):
        return self.__value
    
#********************************************************************
data_source = DataSource()
sheet1 = SpreadSheet()
sheet2 = SpreadSheet()
chart = Chart()

data_source.addObserver(sheet1)
data_source.addObserver(sheet2)
data_source.addObserver(chart)

data_source.setValue(2)