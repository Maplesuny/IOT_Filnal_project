import random
import requests


def create_data():
    number = input('create how many data :')
    f = open('stat1-1.txt','w')
    ff = open('stat1-2.txt','w')
    fff = open('stat1-3.txt','w')
    b = open('stat2-1.txt','w')
    bb = open('stat2-2.txt','w')
    bbb = open('stat2-3.txt','w')
    u = open('stat3-1.txt','w')
    uu = open('stat3-2.txt','w')
    uuu = open('stat3-3.txt','w')
    for i in range(0,number):
        f.write("%s\n" % random.randint(25,27))
        ff.write("%s\n" % random.randint(30,40))
        fff.write("%s\n" % random.randint(0,2))
        b.write("%s\n" % random.randint(26,32))
        bb.write("%s\n" % random.randint(40,60))
        bbb.write("%s\n" % random.randint(3,4))
        u.write("%s\n" % random.randint(21,24))
        uu.write("%s\n" % random.randint(20,30))
        uuu.write("%s\n" % random.randint(0,1))
    
    f.close()
    ff.close()
    fff.close()

def init_om2m():
    xml = """<om2m:application xmlns:om2m="http://uri.etsi.org/m2m" appId="MY_SENSOR"><om2m:searchStrings><om2m:searchString>Type/sensor</om2m:searchString><om2m:searchString>Category/temperature</om2m:searchString><om2m:searchString>Location/Home</om2m:searchString></om2m:searchStrings></om2m:application>"""
    r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications',data = xml, auth=('admin','admin'))
    xml = """<om2m:container xmlns:om2m="http://uri.etsi.org/m2m" om2m:id="DATA"></om2m:container>"""
    r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers',data = xml, auth=('admin','admin'))
   
def dummy_device():
    print 'device simulate start'
    init_om2m()
    g = 4
    str1 = '<obj><str name="appId" val="MY_SENSOR"/><int name="Fahrenhei" val="'
    str2 = '"/><int name="humidity" val="'
    str3 = '"/><int name="wind" val="'
    str4 = '"/></obj>'
    while g != 0 :
        g = input('1) Scenes1 2)Scenes2 3)Scenes3 :')
        if g == 1 :
            Fahrenhei = random.randint(25,27)
            humidity = random.randint(30,40)
            wind = random.randint(0,2)
            xml = str1 + str(Fahrenhei) + str2 + str(humidity) + str3 + str(wind) + str4 
            r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers/DATA/contentInstances',data = xml, auth=('admin','admin'))
        elif g == 2:
            Fahrenhei = random.randint(26,32)
            humidity =random.randint(40,60)
            wind = random.randint(3,4)
            xml = str1 + str(Fahrenhei) + str2 + str(humidity) + str3 + str(wind) + str4 
            r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers/DATA/contentInstances',data = xml, auth=('admin','admin'))
        elif g == 3:
            Fahrenhei = random.randint(21,24)
            humidity =random.randint(20,30)
            wind = random.randint(0,1)
        xml = str1 + str(Fahrenhei) + str2 + str(humidity) + str3 + str(wind) + str4 
        r = requests.post('http://127.0.0.1:8181/om2m/gscl/applications/MY_SENSOR/containers/DATA/contentInstances',data = xml, auth=('admin','admin'))
            
if __name__ == "__main__":
    from sys import argv
    temp = input('1)Dummy device 2)create data  :')
    if temp == 2:
        create_data()        
    else:
        dummy_device()
    
    