#encoding:utf-8
import sys
sys.path.append('../')
from ZBaseCoreObject import ZBaseCoreObject
from bs4 import BeautifulSoup
import urlparse

class ZAnalyser(ZBaseCoreObject):
    """Analyser is a object to parse all elements of target web"""
    def __init__(self, soup = None):
        ZBaseCoreObject.__init__(self)
        
        self.url_domain = None
        self.soup = soup
        self.db_names = ['']
        
        """analyze urls in pages"""
        self.same_domain_urls = set()
        self.other_domain_urls = set()
        self._flg_url_analyze_finished = False
        self._flg_url_store_finished = False
        
        """analyze forms in pages"""
        self.forms = set()
        self._flg_form_analyze_finished = False
        self._flg_form_store_finished = False
        
        """"""
        
        
        
        
    def analyze_urls(self):
        a_tags = self.soup.findAll('a')
        
        if self._flg_url_analyze_finished != False:
            self._flg_url_analyze_finished = False
            
        for a_tag in a_tags:
            try:
                ret = a_tag['href']
                """drop empty href"""
                if ret == "":
                    continue
                o = urlparse.urlparse(url)
                if o[0] == 'https' or o[0] == 'http':
                    if self.url_domain in o[1]:
                        self.same_domain_urls.add(ret)
                        print ret
                    else:
                        self.other_domain_urls.add(ret)
                        print ret
                else:
                    if o[1] == "":
                        self.same_domain_urls.add(ret)
                        print ret
                        
            except:
                pass
        if self._flg_url_analyze_finished != True:
            self._flg_url_analyze_finished = True
            
        self.__store_urls()
            
    def __store_urls(self):
        if self._flg_url_store_finished != False:
            self._flg_url_store_finished = False


        if self.same_domain_urls != set():
            """TBD"""
            pass
        
        if self.other_domain_urls != set():
            """TBD"""
            pass
        
        if self._flg_url_store_finished != True:
            self._flg_url_store_finished = True
        
            
    def analyze_forms(self):
        if self._flg_form_analyze_finished != False:
            self._flg_form_analyze_finished = False
        
        form_tags = self.soup.findAll('form')
        for form_tag in form_tags:
            self.forms.add(form)
            print form
        
        if self._flg_form_analyze_finished != True:
            self._flg_form_analyze_finished = True
    
    def analyze_scripts(self):
        pass
    
    def analyze_imgs(self):
        pass
    
    def analyze_development(self):
        pass

if __name__ == "__main__":
    ana = ZAnalyser()