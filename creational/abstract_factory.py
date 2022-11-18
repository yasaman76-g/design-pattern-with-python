from abc import ABC,abstractmethod

class WidgetFactory(ABC):
    @abstractmethod
    def createButton(self):
        pass
    @abstractmethod
    def createTextBox(self):
        pass
    
class Widget(ABC):
    @abstractmethod
    def render(self):
        pass
    
class Button(Widget):
    def render(self):
        return super().render()
    
class TextBox(Widget):
    def render(self):
        return super().render()
    
#********************************************************************
#materials

class MaterialButton(Button):
    def render(self):
        print("Material button")
        
class MaterialTextBox(Button):
    def render(self):
        print("Material textbox")
        
class MaterialWidgetFactory(WidgetFactory):
    def createButton(self):
        return MaterialButton()
    def createTextBox(self):
        return MaterialTextBox()
        
#********************************************************************
#ant

class AntButton(Button):
    def render(self):
        print("Ant button")
        
class AntTextBox(Button):
    def render(self):
        print("Ant textbox")
        
class AntWidgetFactory(WidgetFactory):
    def createButton(self):
        return AntButton()
    def createTextBox(self):
        return AntTextBox()
#********************************************************************
#app
class ContactFrom:
    def render(self,factory:WidgetFactory):
        factory.createButton().render()
        factory.createTextBox().render()
#********************************************************************
ContactFrom().render(MaterialWidgetFactory())
        