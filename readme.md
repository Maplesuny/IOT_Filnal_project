python version 2.7

need to install requests packet

Dstat.py can create 3 type sensor data (author define)

httpserver.py will auto to notify GSCL and judge state of sensor data , then server will post data to NSCL

Dstat.py has two mode 
1) Dummy device
	user choise which type of sensor data then device will upload data one time to GSCL repeat

	auto create app and data container at GSCL(fixed name , fixed URL)

2) create test data

	user choise the mode the decide number of sensor data

	Dstat.py will create 3 stat data and each stat has three file with one sensor

if need to change GSCL URL , user need to change the code


httpserver.py

1)auto subscribe GSCL data container , create app & container at NSCL

2)get data from GSCL the use paper algorithm to judge state

3)post sensor state to NSCL data container

it fixed monitor (subcribe) port 8383 
	it can change in code if needed

NSCL GSCL url name is fixed
	it can change in code if needed	