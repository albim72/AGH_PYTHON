import xml.etree.ElementTree as ET

try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()

    for child in root:
        print(f"tag: {child.tag}, atrybuty: {child.attrib};")

    print(root[0][1].text)
except:
    print("element nie istnieje")
