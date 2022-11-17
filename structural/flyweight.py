from enum import Enum

class PointType(Enum):
    HOSPITAL = "HOSPITAL"
    CAFE = "CAFE"
    RESTURANT = "RESTURANT"

#********************************************************************   
#flyweight
class PointIcon:
    def __init__(self,point_type:PointType,icon:list()):
        self.__point_type = point_type
        self.__icon = icon
        
    def getIcon(self):
        return self.__icon
    
    def getType(self):
        return self.__point_type.value
    
class PointIconFactory:
    def __init__(self):
        self.__icons = dict()
        
    def getPointIcon(self,type:PointType):
        
        if self.__icons.get(type) is None:
            icon = PointIcon(type,None)
            self.__icons[type] = icon
            
        return self.__icons[type]
#********************************************************************       
class Point:
    def __init__(self,x:int(),y:int(),icon : PointIcon):
        self.__x = x
        self.__y = y
        self.__icon = icon
        
    def draw(self):
        print(f"{self.__icon.getType()} at ({self.__x},{self.__y})")
        
class PointService:
    
    def __init__(self,icon_factory:PointIconFactory):
        self.__icon_factory = icon_factory
        
    def getPoints(self):
        points = list()
        point = Point(2,4,self.__icon_factory.getPointIcon(PointType.CAFE))
        points.append(point)
        return points
    
#********************************************************************
service = PointService(PointIconFactory())
for point in service.getPoints():
    point.draw()
        