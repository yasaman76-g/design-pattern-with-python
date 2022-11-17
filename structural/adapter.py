from abc import ABC,abstractmethod

class Image:
    pass

class ImageView:
    def __init__(self,image:Image):
        self.__image = image
        
    def apply(self,filter:'Filter'):
        filter.apply(self.__image)

class Filter(ABC):
    @abstractmethod
    def apply(self,image:Image):
        pass

class Caramel:
    def init(self):
        pass
    def render(self,image:Image):
        print("Applying carmel filter")
   
class CaramelAdapter(Filter):
    def __init__(self,caramel:Caramel):
        self.__caramel = caramel
        
    def apply(self, image: Image):
        self.__caramel.init()
        self.__caramel.render(image)

#********************************************************************
image_view = ImageView(Image())
image_view.apply(CaramelAdapter(Caramel()))