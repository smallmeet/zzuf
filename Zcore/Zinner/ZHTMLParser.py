#encoding:utf-8
from Zcore import ZBaseCoreObject
import selenium
import threading
import bs4
import requests
import urlparse
import time
#import ZLOG

class ZHTMLParser(ZBaseCoreObject):
    """Get & Parser HTML"""
    def __init__(self, request_url='', dynamic_html = False, 
                 request_headers = {}, request_method = '', request_params = {}):
        """Attention at now , only the static_html can make your own request items"""
        ZBaseCoreObject.__init__(self)
        
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
        self.html_tag_tree = None
        
        """request items"""
        self.request_headers = request_headers
        self.request_params = request_params
        request_method.lower()
        self.request_method = request_method
        self.__r_methods = ['get', 'post', 'put', 'delete', 'head', 'options']
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
        html_tag_tree=[]
        if self.html_raw_data!="":
            soup = BeautifulSoup(self.html_raw_data, "lxml")
            self.soup=soup.prettify()
            for tag in soup.find_all(True):
                self.html_tag_tree.append(tag)
        
        if self._flg_is_parsing == True:
            self._flg_is_parsing = False
        if self._flg_parse_finished == False:
            self._flg_parse_finished = True
    
    def execute(self):
        """Main in ZHTMLParser"""
        pass

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
                self.request_method = "get"
                requests.get(url)
            response = eval("requests."+self.request_method+"(self.url, params = self.request_params, headers = self.request_headers)")
            if response.text != "":
                self.html_raw_data = response
                
            return 0
        
        if self._flg_is_requesting == True:
            self._flg_is_requesting = False
        if self._flg_request_finished == False:
            self._flg_request_finished = True

    def data_handler(self):
        urldb=bsddb.btopen('url.db','c')
        htmldb=bsddb.btopen('html.db','c')
        
        urldb['url']=self.url
        urldb['protocol']=self.url_protocol
        urldb['domain']=self.url_domain
        urldb['path']=self.url_path
        urldb['param']=self.url_param
        urldb['fragment']=self.url_fragment
        urldb.sync()
        urldb.close()
        
        htmldb['raw_data']=self.html_raw_data
        htmldb['soup']=self.soup
        htmldb['tag_tree']=self.html_tag_tree
        htmldb.sync()
        htmldb.close()



            
        

