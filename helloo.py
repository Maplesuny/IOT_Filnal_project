import random

def Scenes1():
  Fahrenhei1 = random.randint(25,27)
  humidity1 =random.randint(30,40)
  wind1 = random.randint(0,2)
#  print ('\n',Fahrenhei1,'\n',humidity1,'\n',wind1)
  return Fahrenhei1,humidity1,wind1
def Scenes2():
  Fahrenhei2 = random.randint(26,32)
  humidity2 =random.randint(40,60)
  wind2 = random.randint(3,4)
#  print ('\n',Fahrenhei2,'\n',humidity2,'\n',wind2)
  return  Fahrenhei2,humidity2,wind2 
def Scenes3():
  Fahrenhei3 = random.randint(21,24)
  humidity3 =random.randint(20,30)
  wind3 = random.randint(0,1)
#  print ('\n',Fahrenhei3,'\n',humidity3,'\n',wind3)
  return Fahrenhei3,humidity3,wind3

Scenes = input("Please input 1~3 Scenes:")

if Scenes > "3":
        print ("Excuse!\nMore than Scenes")
elif Scenes =="1":
        print ("\n",Scenes1(),"\n","Current Scenes is 宿舍")
elif Scenes == "2":
        print ("\n",Scenes2(),"\n","Current Scenes is 球場") 
elif Scenes == "3":
        print ("\n",Scenes3(),"\n","Current Scenes is LAB")
        
