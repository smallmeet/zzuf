#encoding:utf-8
import sys
sys.path.append("../..")
from ZBaseCoreObject import ZBaseCoreObject
from time import sleep
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser,NmapParserException
import time
try:
    import bsddb
except:
    print "Error with importing bsddb module"
from datetime import datetime



class ZServerScanner(ZBaseCoreObject):
    def __init_dbd__(self):
        try:
           
            index = "result_server" + str(time.strftime('%Y%m%d%H%M%S')) + ".db"
            self.scan_report = bsddb.btopen(file = index,flag = 'c')
            print "result_server is created successfully!"
            self.filename.append(index)
            self.filelist = bsddb.btopen(file = "filelist_re.db",flag = 'c')
            self.filelist[str(time.strftime('%Y%m%d%H%M%S'))] = index
          #  print self.filelist.items()
        except:
            print "Can't create BDB files!"
        
    def __init__(self,targets,options):
        
        self.targets = targets
        self.options = options
        """init_flag"""
        self._flg_is_initing = False
        self._flg_init_finished = False
        """init start flag"""
        if(self._flg_is_initing != True):
            self._flg_is_initing =True
        if(self._flg_init_finished != False):
            self._flg_init_finished = False
        """scan flag"""
        self._flg_is_scanning = False
        self._flg_scan_finished = False
        """store the nmap data flag"""
        self._flg_is_storing = False
        self._flg_store_finished =False
        """BDB"""
        self.scan_report = None
        self.filenlist =None
        """存储文件名"""
        self.filename = []        
        self.__init_dbd__()
        """重试次数&超时时间(s)"""
        self.retrycnt = 3
        self.timeout = 3600
        """处理端口状态"""
        self.port_states = ['open']
        """init finish flag"""
        if(self._flg_is_initing!= False):
            self._flg_is_initing = False
        if(self._flg_init_finished != True):
            self._flg_init_finished = True
            
            
    def do_scan(self):
        """scan start flag"""
        if(self._flg_is_scanning != True):
            self._flg_is_scanning = True
        if(self._flg_scan_finished != False):
            self._flg_scan_finished = False
        """运行次数初始化"""
        trycnt = 0
        while True:
            """运行时间初始化"""
            runtime = 0
            if trycnt >= self.retrycnt:
                print '-' * 50
                return 'retry overflow'
            try:
                nmap_proc = NmapProcess(targets=self.targets,options=self.options,safe_mode=False)
                self._flg_is_scanning = True    
                nmap_proc.run_background()
                while(nmap_proc.is_running()):
                    """运行超时，结束掉任务，休息1分钟，再重启这个nmap任务"""
                    if runtime >= self.timeout:
                        print '-' * 50
                        print "timeout....terminate it...."
                        nmap_proc.stop()
                        """休眠时间"""
                        sleep(60)
                        trycnt += 1
                        break
                    else:
                        print 'running[%ss]:%s' %(runtime,nmap_proc.command)
                        sleep(5)
                        runtime += 5
                if nmap_proc.is_successful():
                    """scan finished flag"""
                    if(self._flg_is_scanning != False):
                        self._flg_is_scanning = False
                    if(self._flg_scan_finished != True):
                        self._flg_scan_finished = True
                        
                    print '-' * 50
                    print nmap_proc.summary
                    return nmap_proc.stdout
            except Exception,e:
                print e
                trycnt +=1
                if trycnt >= retrycnt:
                    print '-' * 50
                    print 'retry overflow'
                    return e
                    
                        
    def parse_nmap_report(self,nmap_stdout):
        """parse start flag"""
        if(self._flg_is_storing != True):
            self._flg_is_storing = True
        if(self._flg_store_finished != False):
            self._flg_store_finished = False        
        try:
            nmap_report = NmapParser.parse(nmap_stdout)
            self._flg_is_storing = True
            for host in nmap_report.hosts:
                if len(host.hostnames):
                   tmp_host = host.hostnames.pop()
                else:
                    tmp_host = host.address
            
                for serv in host.services:
                   # if serv.state in self.port_states:
                    self.scan_report[str(serv.port)+serv.protocol] = serv.service
            """parse finished flag"""
            if(self._flg_is_storing != False):
                  self._flg_is_storing = False
            if(self._flg_is_storing != True):
                self._flg_is_storing = True                        
            print self.scan_report.items()
            return _flg_store_finished
        except Exception, e:
            return e
        
if __name__ == "__main__":
    task = ZServerScanner("127.0.0.1", "-sV")
    nmap_stdout = task.do_scan()
    if task.parse_nmap_report(nmap_stdout) :
        print "the program is done"

    