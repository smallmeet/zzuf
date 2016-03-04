#encoding:utf-8
import sys
sys.path.append('../')
from ZBaseCoreObject import ZBaseCoreObject
import selenium
import threading
from bs4 import BeautifulSoup
import requests
import urlparse
import time
import bsddb
import os
#import ZLOG

class ZHTMLParser(ZBaseCoreObject):
    """Get & Parser HTML"""
    def __init__(self, request_url='', dynamic_html = False, 
                 request_headers = {}, request_method = '', request_params = {}):
        """Attention at now , only the static_html can make your own request items"""
        ZBaseCoreObject.__init__(self)
        
        self.db_name = ["url_info.db"]
        for ret in self.db_name:    
            if os.path.exists(ret) == True:
                os.remove(ret)

        
        """init_flag"""
        self._flg_is_initing = False
        self._flg_init_finished = False
        
        """set flag func_start"""
        if self._flg_is_initing != True:
            self._flg_is_initing = True
        if self._flg_init_finished != False:
            self._flg_init_finished = False
        
        """request flag"""
        self._flg_is_requesting = False
        self._flg_request_finished = False
        
        """parse flag"""
        self._flg_is_parsing = False
        self._flg_parse_finished = False
        
        """
        store flag
        Because the process of storing is very fast,
        Just a finish flag
        """
        self._flg_store_finished = False
        
        """execute flag"""
        self._flg_is_executing = False
        self._flg_execute_finished = False
        
        """dynamic parse flag"""
        self._flg_is_dynamic = dynamic_html
        self.webdriver = None
        if self._flg_is_dynamic == True:
            self__init_selenium()
            
        
        self.url = request_url
        self.url_protocol = ""
        self.url_domain = ""
        self.url_path = ""
        self.url_param = ""
        self.url_query = ""
        self.url_fragment = ""
        if self.__url_parser(self.url) == 0:
            """Wait the LOG module completed by ZLOG.error send"""
           #ZLOG.error("[!] ZHTMLParser __url_parser ERROR!")
            pass
        
        """HTML items"""
        self.soup = None
        self.html_raw_data = None
        self.html_tag_tree = []
        
        """request items"""
        self.request_headers = request_headers
        self.request_params = request_params
        request_method.upper()
        self.request_method = request_method
        self.__r_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH']
        #self.flg_is_hooked = False
        
        """finish init"""
        if self._flg_is_initing != False:
            self._flg_is_initing = False
        if self._flg_init_finished != True:
            self._flg_init_finished = True
            
    def __init_selenium(self):
        try:
            self.webdriver = selenium.webdriver.PhantomJS(executable_path="phantomjs.exe")
            return 1
        except:
            return 0
        
    def __url_parser(self, url = ""):
        if url != "":
            try:
                url_obj = urlparse.urlparse(url)
            except:
                return 0
            self.url_protocol = url_obj[0]
            self.url_domain = url_obj[1]
            self.url_path = url_obj[2]
            self.url_param = url_obj[3]
            self.url_query = url_obj[4]
            self.url_fragment = url_obj[5]
            return 1
        else:
            return 0
                
            

    def parse(self):
        if self._flg_is_parsing == False:
            self._flg_is_parsing = True
        if self._flg_parse_finished == True:
            self._flg_parse_finished = False
            
        
        if self.html_raw_data != "":
            soup = BeautifulSoup(self.html_raw_data) 
            self.soup=soup.prettify()
            for tag in soup.find_all(True):
                self.html_tag_tree.append(tag)
        
        if self._flg_is_parsing == True:
            self._flg_is_parsing = False
        if self._flg_parse_finished == False:
            self._flg_parse_finished = True
    
    def execute(self):
        """Main in ZHTMLParser"""
        if self._flg_is_executing == False:
            self._flg_is_executing = True
        if self._flg_execute_finished == True:
            self._flg_execute_finished = False
        
    

        
        while True:
            if self._flg_init_finished == True:
                print "initialize finished"
                self.request()
                break
        
        while True:
            if self._flg_request_finished == True:
                print "request finished"
                self.parse()
                break
                
        while True:
            if self._flg_parse_finished == True:
                print "parse finished"
                self.store()
                break
                
                
        
        if self._flg_is_executing == True:
            self._flg_is_executing = False
        if self._flg_execute_finished == False:
            self._flg_execute_finished = True        

    def request(self):
        if self._flg_is_requesting == False:
            self._flg_is_requesting = True
        if self._flg_request_finished == True:
            self._flg_request_finished = False
        
        
        if self._flg_is_dynamic == True:
            self.webdriver.get(self.url)
            """
            Wind can use selenium http://selenium-python.readthedocs.org/en/latest/waits.html
            find how to make this page completed then get source codes
            """
            time.sleep(4)
            self.html_raw_data = self.webdriver.page_source
            self.webdriver.close()
            return 0
            
        else:
            if self.request_method not in self.__r_methods:
                self.request_method = "GET"
            response = requests.request(self.request_method, url=self.url, params = self.request_params
                                        ,headers = self.request_headers)
            if response.text != "":
                self.html_raw_data = response.text
                
        
        if self._flg_is_requesting == True:
            self._flg_is_requesting = False
        if self._flg_request_finished == False:
            self._flg_request_finished = True

    def store(self):
        if self._flg_store_finished == True:
            self._flg_store_finished = False
        
        
        
        urldb=bsddb.btopen(self.db_name[0],'c')
        
        urldb['url']=self.url
        urldb['protocol']=self.url_protocol
        urldb['domain']=self.url_domain
        urldb['path']=self.url_path
        urldb['param']=self.url_param
        urldb['fragment']=self.url_fragment
        urldb.sync()
        urldb.close()

        
        if self._flg_store_finished == False:
            self._flg_store_finished = True

    
if __name__ == "__main__":
    test_obj = ZHTMLParser(request_url='http://freebuf.com/')
    test_obj.execute()
    
    #you can use these field
    test_obj.soup
    test_obj.db_name
    test_obj.html_raw_data
    test_obj.html_tag_tree
    
    for i in test_obj.html_tag_tree:
        print i.encode('gbk')
    