#encoding:utf-8
from Zcore import ZBaseCoreObject

class ZDomainScanner(ZBaseCoreObject):

    def __init__(self,domain):
        self.domain = domain

    def getid(self):
        myaddr = socket.getaddrinfo(self.domain,'http')[0][4][0]
        return myaddr

    def getpz(self):
        r = requests.get('http://s.tool.chinaz.com/same?s='+self.domain+'&page=')
        responseHtml = r.content
        match = re.findall(r'<div class="w30-0 overhid"><a href=\'(.*?)\'', responseHtml)
        return match
