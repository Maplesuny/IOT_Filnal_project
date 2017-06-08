#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import requests
import kerker
import xml.etree.ElementTree as ET
import math

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self): # <-- HTTP GET
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #print post_data
        #f = open('temp.txt','r+')
        #f.write(post_data)
        print 'get notify'
        tree = kerker.decode(post_data)
        root = tree.getroot()
        print '----------' + 'ow' + '-----------------'
        print mydevice.S1_OW
        print mydevice.S2_OW
        print mydevice.S3_OW
        print '----------' + 'ow' + '-----------------'
        tempanswer = mydevice.where_am_i(float(root[1].attrib['val']),float(root[2].attrib['val']),float(root[3].attrib['val']))
        
        str1 = '<obj><str name="appId" val="MY_SENSOR"/><int name="state" val="'
        str2 = '"/></obj>'
        
        if tempanswer == 1 :
            str3 = 'home'
        if tempanswer == 2 :
            str3 = 'court'
        if tempanswer == 3 :
            str3 = 'LAB'    
        print str3
        xml = str1 + str3 + str2 
        r = requests.post('http://127.0.0.1:8080/om2m/nscl/applications/MY_SENSOR/containers/DATA/contentInstances',data = xml, auth=('admin','admin'))
        
        
        self._set_headers()
        self.wfile.write(post_data)
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    #notify container 
    xml = """<om2m:subscription xmlns:om2m="http://uri.etsi.org/m2m"><om2m:contact>http://127.0.0.1:8383</om2m:contact></om2m:subscription>"""
    r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers/DATA/contentInstances/subscriptions',data = xml,auth=('admin','admin'))
    
    httpd.serve_forever()

class J:
    def __init__(self):
        self.S1F_data = []
        self.S1H_data = []
        self.S1w_data = []
        self.S2F_data = []
        self.S2H_data = []
        self.S2w_data = []
        self.S3F_data = []
        self.S3H_data = []
        self.S3w_data = []
        self.S1_CW = 1
        self.S2_CW = 1
        self.S3_CW = 1
        self.S1_OW = 1
        self.S2_OW = 1
        self.S3_OW = 1
        
        f = open('stat1-1.txt','r')
        b = f.readline()
        
        while len(b) != 0 :
            a = int(b)
            self.S1F_data.append(a)
            b = f.readline()
        f = open('stat1-2.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S1H_data.append(a)
            b = f.readline()
        f = open('stat1-3.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S1w_data.append(a)
            b = f.readline()
            
        f = open('stat2-1.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S2F_data.append(a)
            b = f.readline()
        f = open('stat2-2.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S2H_data.append(a)
            b = f.readline()
        f = open('stat2-3.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S2w_data.append(a)
            b = f.readline()
        f = open('stat3-1.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S3F_data.append(a)
            b = f.readline()
        f = open('stat3-2.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S3H_data.append(a)
            b = f.readline()
        f = open('stat3-3.txt','r')
        b = f.readline()
        while len(b) != 0 :
            a = int(b)
            self.S3w_data.append(a)
            b = f.readline()
        mean = float(sum(self.S1F_data)) / len(self.S1F_data)
        var = sum([(d - mean)**2 for d in self.S1F_data]) / len(self.S1F_data)
        Sdevia = math.sqrt(var)
        self.S1F_H = Sdevia * (4/3*len(self.S1F_data))**(1.0/5)
        
        mean = float(sum(self.S1H_data)) / len(self.S1H_data)
        var = sum([(d - mean)**2 for d in self.S1H_data]) / len(self.S1H_data)
        Sdevia = math.sqrt(var)
        self.S1H_H = Sdevia * (4/3*len(self.S1H_data))**(1.0/5)

        mean = float(sum(self.S1w_data)) / len(self.S1w_data)
        var = sum([(d - mean)**2 for d in self.S1w_data]) / len(self.S1w_data)
        Sdevia = math.sqrt(var)
        self.S1w_H = Sdevia * (4/3*len(self.S1w_data))**(1.0/5)
    
        mean = float(sum(self.S2F_data)) / len(self.S2F_data)
        var = sum([(d - mean)**2 for d in self.S2F_data]) / len(self.S2F_data)
        Sdevia = math.sqrt(var)
        self.S2F_H = Sdevia * (4/3*len(self.S2F_data))**(1.0/5)
        
        mean = float(sum(self.S2H_data)) / len(self.S2H_data)
        var = sum([(d - mean)**2 for d in self.S2H_data]) / len(self.S2H_data)
        Sdevia = math.sqrt(var)
        self.S2H_H = Sdevia * (4/3*len(self.S2H_data))**(1.0/5)

        mean = float(sum(self.S2w_data)) / len(self.S2w_data)
        var = sum([(d - mean)**2 for d in self.S2w_data]) / len(self.S2w_data)
        Sdevia = math.sqrt(var)
        self.S2w_H = Sdevia * (4/3*len(self.S2w_data))**(1.0/5)
        
        mean = float(sum(self.S3F_data)) / len(self.S3F_data)
        var = sum([(d - mean)**2 for d in self.S3F_data]) / len(self.S3F_data)
        Sdevia = math.sqrt(var)
        self.S3F_H = Sdevia * (4/3*len(self.S3F_data))**(1.0/5)
        
        mean = float(sum(self.S3H_data)) / len(self.S3H_data)
        var = sum([(d - mean)**2 for d in self.S3H_data]) / len(self.S3H_data)
        Sdevia = math.sqrt(var)
        self.S3H_H = Sdevia * (4/3*len(self.S3H_data))**(1.0/5)

        mean = float(sum(self.S3w_data)) / len(self.S3w_data)
        var = sum([(d - mean)**2 for d in self.S3w_data]) / len(self.S3w_data)
        Sdevia = math.sqrt(var)
        self.S3w_H = Sdevia * (4/3*len(self.S3w_data))**(1.0/5)
        
    def where_am_i(self ,Fahrenhei , humidity , wind) :   
        s1s1w =  sum([math.exp(((Fahrenhei-d)/self.S1F_H)**2/-2) for d in self.S1F_data]) / len(self.S1F_data) / self.S1F_H / (math.sqrt(math.pi))
        s1s2w =  sum([math.exp(((humidity-d)/self.S1H_H)**2/-2) for d in self.S1H_data]) / len(self.S1H_data) / self.S1H_H / (math.sqrt(math.pi))
        s1s3w =  sum([math.exp(((wind-d)/self.S1w_H)**2/-2) for d in self.S1w_data]) / len(self.S1w_data) / self.S1w_H / (math.sqrt(math.pi))
        
        self.S1_CW = self.S1_OW * s1s1w * s1s2w * s1s3w 
        self.S1_OW = self.S1_CW 
        
        s2s1w =  sum([math.exp(((Fahrenhei-d)/self.S2F_H)**2/-2) for d in self.S2F_data]) / len(self.S2F_data) / self.S2F_H / (math.sqrt(math.pi))
        s2s2w =  sum([math.exp(((humidity-d)/self.S2H_H)**2/-2) for d in self.S2H_data]) / len(self.S2H_data) / self.S2H_H / (math.sqrt(math.pi))
        s2s3w =  sum([math.exp(((wind-d)/self.S2w_H)**2/-2) for d in self.S2w_data]) / len(self.S2w_data) / self.S2w_H / (math.sqrt(math.pi))
        
        self.S2_CW = self.S2_OW * s2s1w * s2s2w * s2s3w 
        self.S2_OW = self.S2_CW 
        
        s3s1w =  sum([math.exp(((Fahrenhei-d)/self.S3F_H)**2/-2) for d in self.S3F_data]) / len(self.S3F_data) / self.S3F_H / (math.sqrt(math.pi))
        s3s2w =  sum([math.exp(((humidity-d)/self.S3H_H)**2/-2) for d in self.S3H_data]) / len(self.S3H_data) / self.S3H_H / (math.sqrt(math.pi))
        s3s3w =  sum([math.exp(((wind-d)/self.S3w_H)**2/-2) for d in self.S3w_data]) / len(self.S3w_data) / self.S3w_H / (math.sqrt(math.pi))
        
        self.S3_CW = self.S3_OW * s1s3w * s3s2w * s3s3w 
        self.S3_OW = self.S3_CW
        
        
        answer = 1;
        my_CW = self.S1_CW
        if(my_CW < self.S2_CW) :
            answer = 2 
            my_CW = self.S2_CW
        if(my_CW < self.S3_CW) :
            answer = 3 
            my_CW = self.S3_CW
        
        return answer
def init_om2m():
    xml = """<om2m:application xmlns:om2m="http://uri.etsi.org/m2m" appId="MY_SENSOR"><om2m:searchStrings><om2m:searchString>Type/sensor</om2m:searchString><om2m:searchString>Category/temperature</om2m:searchString><om2m:searchString>Location/Home</om2m:searchString></om2m:searchStrings></om2m:application>"""
    r = requests.post('http://127.0.0.1:8080/om2m/nscl/applications',data = xml, auth=('admin','admin'))
    xml = """<om2m:container xmlns:om2m="http://uri.etsi.org/m2m" om2m:id="DATA"></om2m:container>"""
    r = requests.post('http://127.0.0.1:8080/om2m/nscl/applications/MY_SENSOR/containers',data = xml, auth=('admin','admin')) 
    print 'om2m init finish'

    
if __name__ == "__main__":
    from sys import argv
	
    mydevice = J()
    
    init_om2m()
	#input("fq")
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()