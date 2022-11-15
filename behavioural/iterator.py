from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def hasNext(self):
        pass
    
    @abstractmethod
    def current(self):
        pass
    
    @abstractmethod
    def next(self):
        pass
    
    
class BrowseHistory:
            
    __urls = list()
    def pushUrl(self,urls:Iterator):
        self.__urls.append(urls)
        
    def popUrl(self):
        lastIndex = len(self.__urls) - 1
        lastState = self.__urls.pop(lastIndex)
        return lastState
    
    def getUrls(self):
        return self.__urls
    
    def createIterator(self):
        return self.ListIterator(self)
    
    class ListIterator(Iterator): 
        __index = int()
        def __init__(self,history):
            self.__history =history
            
        def hasNext(self):
            return (self.__index < len(self.__history.getUrls()))
        
        def current(self):
            return self.__history.getUrls()[self.__index]
        
        def next(self):
            self.__index +=1
    
#********************************************************************   
history = BrowseHistory()
history.pushUrl("a")
history.pushUrl("b")
history.pushUrl("c")

iterator : Iterator = history.createIterator()
while(iterator.hasNext()):
    url = iterator.current()
    print(url)
    iterator.next()