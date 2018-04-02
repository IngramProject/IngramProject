import time
import datetime
from wirelessConnection import WirelessConnection
from battery import Battery


batteryLogFile = "/home/pi/Desktop/testSendBatteryLogFileEachMin.log"


wirelessConnection = WirelessConnection()
wirelessConnection.connectToOfficeUnit()

time.sleep(1)

timeStamp = str(datetime.datetime.now())
wirelessConnection.sendData(timeStamp, batteryLogFile)

time.sleep(1)

# This is for demo purposes
officeReply = wirelessConnection.receiveData()
print(officeReply)

time.sleep(1)

battery = Battery()
batteryLife = battery.getBatteryLife()
wirelessConnection.sendData(batteryLife, batteryLogFile)

time.sleep(1)

# This is for demo purposes
officeReply = wirelessConnection.receiveData()
print(officeReply)

time.sleep(1)

wirelessConnection.endOutflowUnitConnection()
