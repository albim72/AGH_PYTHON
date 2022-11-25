from xml.etree import ElementTree
from xml.dom import minidom

def pretty(element):
    xml_string = ElementTree.tostring(element,'utf-8')
    rep = minidom.parseString(xml_string)
    return rep.toprettyxml(indent="  ")
