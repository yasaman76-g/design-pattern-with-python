from abc import ABC,abstractmethod

class HttpRequest:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Handler:
    
    def __init__(self,next:'Handler'):
        self.__next = next
      
    def handle(self,request:HttpRequest):
        if self.doHandle(request):
            return
        
        if self.__next is not None:
            self.__next.handle(request)
      
    @abstractmethod
    def doHandle(self,request:HttpRequest):
        pass
    
class WebServer:
    def __init__(self,handler:Handler):
        self.__handler = handler
    def handle(self,request:HttpRequest):
        self.__handler.handle(request)
    
class Authenticator(Handler):
    def __init__(self, next: Handler):
        super().__init__(next)
        
    def doHandle(self, request: HttpRequest):
        print("authenticator")
        if request.username == 'admin' and request.password == '123456':
            return False
        return True
    
class Compressor(Handler):
    def __init__(self, next: Handler):
        super().__init__(next)
        
    def doHandle(self, request: HttpRequest):
        print("Compressor")
        return False
    
class Logger(Handler):
    def __init__(self, next: Handler):
        super().__init__(next)
        
    def doHandle(self, request: HttpRequest):
        print("logger")
        return False
    
#********************************************************************

#authenticator -> logger -> compressor
compressor = Compressor(None)
logger = Logger(compressor)
authenticator = Authenticator(logger)
server = WebServer(authenticator)
server.handle(HttpRequest('admin','123456'))


    