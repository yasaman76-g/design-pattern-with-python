from abc import ABC,abstractmethod

class ViewEngine(ABC):
    @abstractmethod
    def render(self,view_name:str(),context:dict()):
        pass
    
#default engine of framework
class DjangoViewEngine(ViewEngine):
    def render(self,view_name:str(),context:dict()):
        return 'Rendring view by Django Engine'
    
#custom view engine
class SharpViewEngine(ViewEngine):
    def render(self,view_name:str(),context:dict()):
        return 'Rendring view by sharp Engine'

#********************************************************************
#creator    
class Controller:
    def render(self,view_name:str(),context:dict()):
        engine = self._createViewEngine()
        html = engine.render(view_name,context)
        print(html)
        
    #factoryMethod   
    def _createViewEngine(self):
        return DjangoViewEngine()
 
class SharpController(Controller):  
    def _createViewEngine(self):
        return SharpViewEngine()   
           
class ProductController(SharpController):
    def getProductslist(self):
        # get products from db
        context = dict()
        #context[key] = [value]
        self.render('products.html',context)
    
   
    
#********************************************************************
ProductController().getProductslist()
