from xml.etree.ElementTree import Element, SubElement, Comment
import xml.etree.ElementTree as ET
from prettyfy import pretty

top = Element("autokomis")
sam1 = SubElement(top,"samochod")

id = SubElement(sam1,"id")
id.text = "sam1"

marka = SubElement(sam1,"marka")
marka.text = "Subaru"

model = SubElement(sam1,"model")
model.text = "Impreza"

poj = SubElement(sam1,"pojemnosc")
id.text = "2.0"

rocznik = SubElement(sam1,"rocznik")
rocznik.text = "1999"

cena = SubElement(sam1,"cena")
cena.text = "52000"

wyp_dod = SubElement(sam1,"wyposazenie_dod")

kolor = SubElement(sam1,"kolor")
kolor.text = "czarna perła"

klima = SubElement(sam1,"klimatyzacja")
cena.text = "RTG56345"
