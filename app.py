# pip install -- upgrate lxml

import xml.etree.ElementTree as ET
tree = ET.parse ('example.xml')
root = tree.getroot()
print(root.findall('.//COURSE/MARK'))

#for i in root.findall("./ASSESSMENTS/STUDENT/MARK"):
 #   print(i)