from abc import ABC,abstractmethod

class Element(ABC):
    @abstractmethod
    def execute(self,visitor:'Visitor'):
        pass

class HeadingElement(Element):
    def execute(self, visitor: 'Visitor'):
        visitor.visit(self,self)

class AnchorElement(Element):
    def execute(self, visitor: 'Visitor'):
        visitor.visit(self,self)
        
class HtmlDocument():
    def __init__(self):
        self.__elements = list()
    
    def add(self,element:Element):
        self.__elements.append(element)
        
    def execute(self, visitor: 'Visitor'):
        for element in self.__elements:
            element.execute(self,visitor)
    
#********************************************************************
class Visitor(ABC):
    @abstractmethod
    def visit(self,heading:HeadingElement):
        pass
    @abstractmethod
    def visit(self,anchor:AnchorElement):
        pass
    
class HighlightVisitor(Visitor):
    def visit(self,heading:HeadingElement):
        print("highlight heading")
    def visit(self, anchor: AnchorElement):
        print("highlight anchor")
#********************************************************************

document = HtmlDocument()
document.add(HeadingElement)
document.add(AnchorElement)
document.execute(HighlightVisitor)
    


