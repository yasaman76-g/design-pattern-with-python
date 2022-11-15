from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def mouseDown(self):
        pass
    
    @abstractmethod
    def mouseUp(self):
        pass
    
class selectionTool(Tool):
    def mouseDown(self):
        print("selection icon")
        
    def mouseUp(self):
        print("draw a dashed rectangle")
        
class BrushTool(Tool):
    def mouseDown(self):
        print("brush icon")
        
    def mouseUp(self):
        print("draw a line")
#********************************************************************       
class Canvas(Tool):
    tool: Tool
    
    def mouseDown(self):
        return self.tool.mouseDown()
    
    def mouseUp(self):
        return self.tool.mouseUp()
    
    def getCurrentTool(self):
        return self.tool
    
    def setCurrentTool(self,tool:Tool):
        self.tool = tool
        
#********************************************************************
canvas = Canvas()
canvas.setCurrentTool(selectionTool())
canvas.mouseDown()
canvas.mouseUp()