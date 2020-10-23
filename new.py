#pip install requests

import lxml.html
import requests

url = "http://www.imdb.com/calendar?region=IE&ref_rlm"
response = requests.get(url, stream=True)
response.raw.decode_content = True
tree = lxml.html.parse(response.raw)

for i in tree.xpath('//div[@id="main"]/h4/fo/following-sibling::ul[1]/li/a/text()'):
    print(i)

