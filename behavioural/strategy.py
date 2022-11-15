from abc import ABC, abstractmethod

class Compressor(ABC):
    @abstractmethod
    def compress(self,fileName):
        pass
    
class JpgCompressor(Compressor):
    def compress(self, fileName):
        print("compressing Jpg")
        
class JpegCompressor(Compressor):
    def compress(self, fileName):
        print("compressing Jpeg")
        
#********************************************************************
class Filter(ABC):
    @abstractmethod
    def apply(self,fileName):
        pass
    
class BlackAndWhiteFilter(Filter):
    def apply(self,fileName):
        print("B&W filter")
        
#********************************************************************
class ImageStorage:
        
    def store(self,fileName,compressor:Compressor,filter:Filter):
        compressor.compress(self,fileName)
        filter.apply(self,fileName)
        
#********************************************************************
imageStorage = ImageStorage() 
imageStorage.store("test",JpgCompressor,BlackAndWhiteFilter)     
