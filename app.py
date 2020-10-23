# pip install -- upgrate lxml

import xml.etree
tree = xml.etree ('example.xml')

for i in tree.xpath("./ASSESSMENTS/STUDENT/MARK"):
   print(i)