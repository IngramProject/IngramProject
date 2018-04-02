

# This is used during testing to shut down the server if needed.

from wirelessConnection import WirelessConnection

wirelessConnection = WirelessConnection()
wirelessConnection.connectToOfficeUnit()
wirelessConnection.shutdownOfficeUnit()