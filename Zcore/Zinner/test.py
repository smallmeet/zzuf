from selenium import webdriver
import time
import bs4
import urllib2
"""
request_item = urllib2.Request(url)
s = urllib2.urlopen(url)

"""
webdri = webdriver.Firefox()


time.sleep(10)

webdri.get("http://freebuf.com/")
print ""
time.sleep(5)
soup = bs4.BeautifulSoup(webdri.page_source)
print soup.tagStack
webdri.close()
