from abc import ABC, abstractmethod

class Ebook(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod   
    def getFileName(self):
        pass

class RealEbook(Ebook):
    
    def __init__(self,file_name):
        self.__file_name = file_name
        self.load()
        
    def load(self):
        print("Loading ebook ",self.__file_name)
        
    def show(self):
        print("Showing ebook ",self.__file_name)
        
    def getFileName(self):
        return self.__file_name
    
class EbookProxy(Ebook):
    def __init__(self,file_name):
        self.__file_name = file_name
        self.__ebook = None
        
    def show(self):
        if self.__ebook is None:
            self.__ebook = RealEbook(self.__file_name)
        return self.__ebook.show()
    
    def getFileName(self):
        return self.__file_name
#client   
class Library:
    def __init__(self):
        self.__ebooks = dict()
        
    def add(self,ebook:Ebook):
        self.__ebooks[ebook.getFileName()] = ebook
        
    def openEbook(self,file_name):
        ebook = self.__ebooks.get(file_name)
        ebook.show()

#********************************************************************
library = Library()
file_names = ["a","b","c"]

for name in file_names:
    library.add(EbookProxy(name))
    
library.openEbook("b")