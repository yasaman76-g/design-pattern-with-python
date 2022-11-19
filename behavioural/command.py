from abc import ABC, abstractmethod

#these classes is part of framwork

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
#invoker   
class Button:
    def __init__(self,command : Command):
        self.__command = command
        
    def click(self):
        self.__command.execute()
        
#********************************************************************
#these classes is part of custom application

#reciever
class CustomerService:
    def addCustomer(self):
        print("add customers to data base")
        
class AddCustomerCommand(Command):
    def __init__(self,customerService : CustomerService):
        self.__customerService = customerService
        
    def execute(self):
        self.__customerService.addCustomer()
        
#********************************************************************
service = CustomerService()
command = AddCustomerCommand(service)
button = Button(command)
button.click()
