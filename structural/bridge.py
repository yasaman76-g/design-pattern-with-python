from abc import ABC, abstractmethod

#features
class RemoteControl():
    def __init__(self,device:'Device'):
        #this is bridge
        self._device =device
         
    def turnOn(self):
        self._device.turnOn()
    
    def turnOff(self):
        self._device.turnOff()

class AdvancedRemoteControl(RemoteControl):
   
    @abstractmethod
    def setChanel(self,number:int()):
        self._device.setChanel(number)

#********************************************************************
#implemention    

class Device(ABC):
    @abstractmethod
    def turnOn(self):
        pass
    @abstractmethod
    def turnOff(self):
        pass
    @abstractmethod
    def setChanel(self,number:int()):
        pass

    
class SonyTv(Device):
    
    def turnOn(self):
        print("Sony turn on")
    
    def turnOff(self):
        print("Sony turn off")
        
    def setChanel(self, number: int()):
        print("Sony setChannel")
        
class SamsungTv(Device):
    
    def turnOn(self):
        print("Samsung turn on")
    
    def turnOff(self):
        print("Samsung turn off")
        
    def setChanel(self, number: int()):
        print("Samsung setChannel")
        
#********************************************************************
remote_control = RemoteControl(SonyTv())
remote_control.turnOn()

remote_control2 = AdvancedRemoteControl(SamsungTv())
remote_control2.turnOn()
 
 