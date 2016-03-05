import urllib
from bs4 import BeautifulSoup
import urlparse

web = urllib.urlopen("http://freebuf.com/")
data = web.read()

soup = BeautifulSoup(data)

form_tags = soup.findAll('form')
for form_tag in form_tags:
    #print form_tag.encode('gbk')
    pass
"""
tag_as = soup.findAll("a")

for tag_a in tag_as:
    try:
        z = tag_a["href"]
        o = urlparse.urlparse(z)
        if 'https' in o[0] or 'http' in o[0]:
            if 'freebuf.com' in o[1]:
                print z
                #pass
            else:
                #print z
                pass
        else:
            if "java" in o[0]:
                continue
            if o[1] == "":
                print z
                
    except:
        pass
"""


script_tags = soup.find_all('script')
"""
for script_tag in script_tags :
    try:
        if script_tag['src'] != "":
            print script_tag['src']
    except:
        if script_tag.text != "":
            print script_tag.text
"""            
style_tags = soup.find_all("style")
for style_tag in style_tags:
    print style_tag
    
link_tags = soup.find_all('link')
for link_tag in link_tags:
    print link_tag

img_tags = soup.find_all('img')
for img_tag in img_tags:
    print img_tag.encode('gbk')