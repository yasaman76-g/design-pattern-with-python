from abc import ABC,abstractmethod

class Component(ABC):
    @abstractmethod
    def render(self):
        pass
    @abstractmethod
    def move(self):
        pass
    
class Shape(Component):
    def render(self):
        print("Render Shape")
        
    def move(self):
        print("Move Shape")
        
class Group(Component):
    def __init__(self):
        self.__components = list()
    
    def add(self,shape:Component):
        self.__components.append(shape)
        
    def render(self):
        for component in self.__components:
            component.render()
            
    def move(self):
        for component in self.__components:
            component.move()
#********************************************************************
group1 = Group()
group1.add(Shape()) #circle
group1.add(Shape()) #circle

group2 = Group()
group2.add(Shape()) #squere
group2.add(Shape()) #squere
group = Group()
group.add(group1)
group.add(group2)
group.render()
group.move()