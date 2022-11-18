from abc import ABC,abstractmethod
#prototype
class Componet(ABC):
    
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def clone(self):
        pass
    
class Circle(Componet):
    __radius = ''
        
    def setRadius(self,radius):
        self.__radius = radius
        
    def getRadius(self):
        return self.__radius
    
    def render(self):
        print("Rendering a circle")
    
    #for logic of create circle    
    def clone(self):
        newCircle = Circle()
        newCircle.setRadius(self.__radius)
        return newCircle
#client       
class ContextMenu:
    def duplicate(componet:Componet):
        new_component:Componet = componet.clone()
        return new_component.render()
    
#********************************************************************
circle = Circle()
circle.setRadius(15)
ContextMenu.duplicate(circle)
