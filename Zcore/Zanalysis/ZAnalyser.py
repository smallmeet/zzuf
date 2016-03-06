#encoding:utf-8
import sys
sys.path.append('../')
from ZBaseCoreObject import ZBaseCoreObject
from bs4 import BeautifulSoup
import urlparse
import threading
import urllib

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
        
        """analyze scripts in pages"""
        self.js = set()
        self.css = set()
        self.links = set()
        self._flg_script_analyze_finished = False
        self._flg_script_store_finished = False
        
        """analyze imgs in pages"""
        self.imgs = set()
        self._flg_img_analyze_finished = False
        self._flg_img_store_finished = False
        
        """analyze iframe in pages"""
        self.iframes = set()
        self._flg_iframe_analyze_finished = False
        self._flg_iframe_store_finished = False
        
        """analyze development info in pages"""
        self._flg_development_analyze_finished = False
        self._flg_development_store_finished = False
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
            self.forms.add(form_tag)
            print form_tag
        
        if self._flg_form_analyze_finished != True:
            self._flg_form_analyze_finished = True
        
    def __store_forms(self):
        if self._flg_form_store_finished != False:
            self._flg_form_store_finished = False
            
        if self.forms != set():
            """Think how to store this data"""
            pass
        
        
        if self._flg_form_store_finished != True:
            self._flg_form_store_finished = True
        
    def analyze_scripts(self):
        if self._flg_script_analyze_finished != False:
            self._flg_script_analyze_finished = False
            
        
        script_tags = self.soup.find_all('script')
        
        for script_tag in script_tags :
            try:
                if script_tag['src'] != "":
                    """Think whether to dump the js from remote_server???"""
                    self.js.add(script_tag)
                    print script_tag['src']
            except:
                if script_tag.text != "":
                    self.js.add(script_tag)
                    print script_tag.text
                  
        style_tags = self.soup.find_all("style")
        for style_tag in style_tags:
            self.css.add(style_tag)
            print style_tag
            
        link_tags = self.soup.find_all('link')
        for link_tag in link_tags:
            self.links.add(link_tag)
            print link_tag
    
            
        if self._flg_script_analyze_finished != True:
            self._flg_script_analyze_finished = True
            
        self.__store_forms()
    def __store_scripts(self):
        if self._flg_script_store_finished != False:
            self._flg_script_store_finished = False
            
        if self.js != set():
            """TBD"""
            pass
        
        if self.css != set():
            """TBD"""
            pass

        if self.links != set():
            """TBD"""
            pass
                        
        if self._flg_script_store_finished != True:
            self._flg_script_store_finished = True
    
    def analyze_imgs(self):
        if self._flg_img_analyze_finished != False:
            self._flg_img_analyze_finished = False
        
        img_tags = self.soup.find_all('img')
        for img_tag in img_tags:
            try:
                if img_tag['src'] != "":
                    self.imgs.add(img_tag)
                    print img_tag
            except:
                pass
            
        if self._flg_img_analyze_finished != True:
            self._flg_img_analyze_finished = True
            
        self.__store_imgs()
        
    def __store_imgs(self):
        if self._flg_img_store_finished != False:
            self._flg_img_store_finished = False
            
        if self.imgs != set():
            """TBD"""
            pass
            
        if self._flg_img_store_finished != True:
            self._flg_img_store_finished = True
    
    def analyze_iframe(self):
        if self._flg_iframe_analyze_finished != False:
            self._flg_iframe_analyze_finished = True
            
        iframe_tags = self.soup.find_all('iframe')
        for iframe_tag in iframe_tags :
            self.iframes.add(iframe_tag)
            print iframe_tag
            
        if self._flg_iframe_analyze_finished != True:
            self._flg_iframe_analyze_finished = True
          
          
        self.__store_iframes()
        
    def __store_iframes(self):
        if self._flg_iframe_store_finished != False:
            self._flg_iframe_store_finished = False

        if self.iframes != set():
            """TBD"""
            pass
        
        if self._flg_iframe_store_finished != True:
            self._flg_iframe_store_finished = True
    
    def analyze_development(self):
        if self._flg_development_analyze_finished != False:
            self._flg_development_analyze_finished = False
            
        """TBD"""
            
        if self._flg_development_analyze_finished != True:
            self._flg_development_analyze_finished = True
            
        self.__store_development()
        
    def __store_development(self):
        if self._flg_development_store_finished != False:
            self._flg_development_store_finished = False

        """TBD"""
        
        if self._flg_development_store_finished != True:
            self._flg_development_store_finished = True
    

    def execute(self):
        threading.Thread(target=self.analyze_urls).start()
        threading.Thread(target=self.analyze_scripts).start()
        threading.Thread(target=self.analyze_imgs).start()
        threading.Thread(target=self.analyze_iframe).start()
        threading.Thread(target=self.analyze_forms).start()
        threading.Thread(target=self.analyze_development).start()
        
if __name__ == "__main__":
    web = urllib.urlopen("http://freebuf.com/")
    data = web.read()
    
    soup = BeautifulSoup(data)    
    
    ana = ZAnalyser(soup)
    ana.execute()