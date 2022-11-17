
class Message:
    def __init__(self,content:str):
        self.__message = content
        
class Connection:
    def disconnect(self):
        pass
 
class AuthToken:
    pass
   
class NotificationServer:
    def connect(self,ip_address):
        return Connection()
    
    def authenticate(self,app_id,password):
        return AuthToken()
    
    def send(self,auth_token:AuthToken,message:Message,target):
        print("sending a message")
        
#********************************************************************
#facade class

class NotifiationService:
    def send(self,message,target):
        server = NotificationServer()
        connection = server.connect("ip")
        auth_token = server.authenticate("app_id","password")
        server.send(auth_token,Message(message),target)
        connection.disconnect()
#********************************************************************
service = NotifiationService()
service.send("hello word","target")