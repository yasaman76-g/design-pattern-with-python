from abc import ABC,abstractmethod

class Stream(ABC):
    @abstractmethod
    def write(self,data:str):
        pass

class CloudStream(Stream):
    def write(self, data: str):
        print("Storing: ",data)

#********************************************************************
#decorators       
class CompressCloudStream(Stream):
    def __init__(self,stream:Stream):
        self.__stream = stream
        
    def write(self, data: str):
        compressed = self.compress(data)
        self.__stream.write(compressed)
        
    
    def compress(self,data:str):
        return data[0:5]
    
class EncryptCloudStream(Stream):
    def __init__(self,stream:Stream):
        self.__stream = stream
        
    def write(self, data: str):
        encrypted = self.encrypt(data)
        self.__stream.write(encrypted)
        
    
    def encrypt(self,data:str):
        return '@#dd&JNM)J'
#********************************************************************

def storeCreditCart(stream:Stream):
    stream.write("2303-1012-8595-9632")
    
data1 = storeCreditCart(CloudStream())
data2 = storeCreditCart(EncryptCloudStream((CloudStream())))
data1 = storeCreditCart(CompressCloudStream((CloudStream())))
data1 = storeCreditCart(CompressCloudStream(EncryptCloudStream((CloudStream()))))
