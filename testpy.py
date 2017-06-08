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
        print 'get post'
        self._set_headers()
        self.wfile.write(post_data)
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    xml = """<om2m:subscription xmlns:om2m="http://uri.etsi.org/m2m"><om2m:contact>http://127.0.0.1:1400/monitor</om2m:contact></om2m:subscription>"""
    r = request.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers/DATA/contentInstances/subscriptions',data = xml,auth=('admin','admin'))
    
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv
    xml = """<om2m:application xmlns:om2m="http://uri.etsi.org/m2m" appId="MY_SENSOR"><om2m:searchStrings><om2m:searchString>Type/sensor</om2m:searchString><om2m:searchString>Category/temperature</om2m:searchString><om2m:searchString>Location/Home</om2m:searchString></om2m:searchStrings></om2m:application>"""
    r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications',data = xml, auth=('admin','admin'))
    xml = """<om2m:container xmlns:om2m="http://uri.etsi.org/m2m" om2m:id="DATA"></om2m:container>"""
    r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers',data = xml, auth=('admin','admin'))
    xml = """<obj><str name="appId" val="MY_SENSOR"/><str name="category" val="temperature "/><int name="data" val="27"/><int name="unit" val="celsius"/></obj>"""
    r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers/DATA/contentInstances',data = xml, auth=('admin','admin'))
    
    #if len(argv) == 2:
    #    run(port=int(argv[1]))
    #else:
    #    run()