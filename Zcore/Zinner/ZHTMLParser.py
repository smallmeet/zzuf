#encoding:utf-8
from Zcore import ZBaseCoreObject
import selenium
import threading
import bs4
import requests

class ZHTMLParser(ZBaseCoreObject):
    """Get & Parser HTML"""
    def __init__(self, url='', request_method = '', param = ''):
        ZBaseCoreObject.__init__(self)
        self.tag_stack = None
        self.url = url
        self.soup = None
        self.raw_html = ""
        self.request_method = request_method
        self.request_param = param
        self.flg_is_hooked = False

    def begin_parse(self):
        pass

    def request(self):
        pass

