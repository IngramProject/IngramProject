
# This script runs on the RetPondPi twice a day at 10am and 2pm. 
# The code to establish a socket connection and send the data is 
# found in wirelessConnection.py which is imported into this script. 
# The batteryLogFile below is the location and 
# name of the log file that will be stored on the OfficePi. 
# The code sleeps for one second three different times to give the 
# code plenty of time to finish each function before moving on. 


import time
import datetime
from wirelessConnection import WirelessConnection
from battery import Battery


# This is the name of the log file and the folder location on the 
# OfficePi where the data sent by this Python script will be stored. 
batteryLogFile = "/home/pi/Desktop/testBatteryLogFile.log"


# This establishes a connection with the OfficePi
wirelessConnection = WirelessConnection()
wirelessConnection.connectToOfficeUnit()

time.sleep(1)


# This gets the current date and time and sends it to the OfficePi
timeStamp = str(datetime.datetime.now())
wirelessConnection.sendData(timeStamp, batteryLogFile)

time.sleep(1)


# This gets the current battery charge and sends it to the OfficePi.
battery = Battery()
batteryLife = battery.getBatteryLife()
wirelessConnection.sendData(batteryLife, batteryLogFile)

time.sleep(1)


# This ends the connection with the OfficePi.
wirelessConnection.endOutflowUnitConnection()


