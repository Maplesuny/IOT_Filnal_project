import base64
import xml.etree.ElementTree as ET

def decode(input):
    f = open('temp.txt','w')
    f.write(input)
    f.close()
    tree = ET.ElementTree(file='temp.txt')    
    root = tree.getroot()
    s = str(root[1].text)
    answer = base64.b64decode(s)
    f = open('temp.txt','w')     
    f.write(answer)
    f.close()
    tree = ET.ElementTree(file='temp.txt')
    root = tree.getroot()
    s = str(root[4].text)
    answer = base64.b64decode(s)
    f = open('temp.txt','w')     
    f.write(answer)
    f.close()
    tree = ET.ElementTree(file='temp.txt')
    return tree