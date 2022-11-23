from abc import ABC,abstractmethod
#framework app
class UIControl:
    #owner is Mediator interface
    def __init__(self,owner):
        self._owner = owner

class ListBox(UIControl):
    
    def __init__(self,owner):
        super().__init__(owner)
    
    def setSelection(self,selection):
        self.__selection = selection
        self._owner.changed(self)
    
    def getSelection(self):
        return self.__selection
    
class TextBox(UIControl):
    
    def __init__(self,owner):
        super().__init__(owner)
    
    def setContent(self,content):
        self.__content = content
        self._owner.changed(self)
    
    def getContent(self):
        return self.__content
    
class Button(UIControl):
    
    def __init__(self,owner):
        super().__init__(owner)
    
    def setEnable(self,is_enable):
        self.__is_enable = is_enable
        self._owner.changed(self)
    
    def getEnable(self):
        return self.__is_enable
    
#********************************************************************
   
class Mediator(ABC):
    @abstractmethod
    def changed(self,control:UIControl):
        pass
    
#********************************************************************
#mediator for our app

class ArticleMediator(Mediator):
    
    def __init__(self):
        self.__articlesListBox = ListBox(self)
        self.__titleTextBox = TextBox(self)
        self.__saveButton = Button(self)
        
    def simulateUserInteraction(self):
        self.__articlesListBox.setSelection("Article 1")
        self.__titleTextBox.setContent("")
        self.__titleTextBox.setContent("Article 2")
        print("text box",self.__titleTextBox.getContent())
        print("button",self.__saveButton.getEnable())
        
    def changed(self, control: UIControl):
        if control == self.__articlesListBox:
            self.articleSelcted()
        elif control == self.__titleTextBox:
            self.titleChanged()
    
    def articleSelcted(self):
        self.__titleTextBox.setContent(self.__articlesListBox.getSelection())
        self.__saveButton.setEnable(True)
        
    def titleChanged(self):
        content = self.__titleTextBox.getContent()
        if content == '':
            self.__saveButton.setEnable(False)
            
        self.__saveButton.setEnable(True)
        
#********************************************************************
dialog = ArticleMediator()
dialog.simulateUserInteraction()

        