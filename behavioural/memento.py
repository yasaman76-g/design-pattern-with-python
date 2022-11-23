#editorState
class Memento:
    def __init__(self,content,fontName,fontSize):
        self.__content = content
        self.__fontName = fontName
        self.__fontSize = fontSize
        
    def getContent(self):
        return self.__content
    
    def getFontName(self):
        return self.__fontName
    
    def getFontSize(self):
        return self.__fontSize

#editor    
class Originator:
   
    def setContent(self,content):
        self.__content = content
    
    def setFontName(self,fontName):
        self.__fontName = fontName
        
    def setFontSize(self,fontSize):
        self.__fontSize = fontSize
        
    def createState(self):
        return Memento(self.__content,self.__fontName,self.__fontSize)
    
    def restore(self,memento:Memento):
        self.__content = memento.getContent()
        self.__fontName = memento.getFontName()
        self.__fontSize = memento.getFontSize()
    
    def getContent(self):
        return self.__content
    
    def getFontName(self):
        return self.__fontName
    
    def getFontSize(self):
        return self.__fontSize

#history   
class Caretaker:
    
    def pushState(self,memento:Memento):
        self.__states = list()
        self.__states.append(memento)
        
    def popState(self):
        lastIndex = len(self.__states) - 1
        lastState = self.__states.pop(lastIndex)
        return lastState
    
history = Caretaker ()   
editor = Originator()

editor.setContent("hello")
editor.setFontName("arial")
editor.setFontSize(11)

history.pushState(editor.createState())

editor.setContent("yasaman")
editor.setFontName("arial")
editor.setFontSize(22)

history.pushState(editor.createState())

editor.setContent("golesorkh")
editor.setFontName("arial")
editor.setFontSize(18)

editor.restore(history.popState())
print(editor.getContent())
print(editor.getFontName())
print(editor.getFontSize())