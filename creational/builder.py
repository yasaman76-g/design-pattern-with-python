from abc import ABC, abstractmethod
 
class PdfDocument:
    def addPage(self,text):
        print("adding a page to pdf")
        
class Image:
    def addFrame(self,text):
        print("adding a page to image")


class Slide:
    
    def __init__(self,text):
        self.__text = text
        
    def getText(self):
        self.__text
                
class PresentationBuilder(ABC):
    @abstractmethod
    def addSlide(self,slide:Slide):
        pass

class PdfDocumentBuilder(PresentationBuilder):
    def __init__(self):
        self.__pdf = PdfDocument()
        
    def addSlide(self, slide: Slide):
        self.__pdf.addPage(slide)
        
    def getPdfDocument(self):
        return self.__pdf
        
class ImageBuilder(PresentationBuilder):
    def __init__(self):
        self.__image = Image()
        
    def addSlide(self, slide: Slide):
        self.__image.addFrame(slide)
        
    def getImage(self):
        return self.__image
        
class Presentation:
    def __init__(self):
        self.__slides : Slide = list()
        
    def addSlides(self,slide:Slide):
        self.__slides.append(slide)
        
    def export(self,builder:PresentationBuilder):
        builder.addSlide(Slide("Copy Write"))
        for slide in self.__slides:
            builder.addSlide(slide)
            
#********************************************************************
presentation = Presentation()
presentation.addSlides("slide 1")
presentation.addSlides("slide 2")

builder = PdfDocumentBuilder()
presentation.export(builder)
pdf = builder.getPdfDocument()