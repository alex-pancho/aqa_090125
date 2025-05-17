import xml.etree.ElementTree as ET
from pathlib import Path

xml_path = Path(__file__).parent / "group.xml"

tree = ET.parse(xml_path)
root = tree.getroot()

# Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)

for group in root.findall('group'): # root.findall(".//bbo")
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        bbo = timing_exbytes.find('bbo')
        if bbo is not None:
            print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
        else:
            print(f"Group: {group.find('name').text}, bbo: Не знайдено")
