import xml.sax

class UchwytFilmu(xml.sax.ContentHandler):
    
    def __init__(self):
        self.CurrentData = ""
        self.id = ""
        self.tytul = ""
        self.rok = ""
        self.kraj = ""
        self.czas_t = ""
        self.gatunek = ""
        
    def startElement(self,tag,attribs):
        self.CurrentData = tag
        if tag == "film":
            print("_____________ nowy film _________________")
