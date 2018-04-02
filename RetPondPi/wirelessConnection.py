
# This class implements all the functions necessary to establish a socket 
# connection with the OfficePi, send and receive data, end the connection, and 
# shutdown the server on the OfficePi. This code does not run or do anything on 
# its own. It must be imported into another script like sendBatteryCharge.py where 
# the code can be used. There is comments above each function that describes what 
# the functions do. 


import socket


class WirelessConnection:

	# This is the constructor. This function runs automatically when
	# an instance of this class's object is called. An example of calling
	# an instance of theis class's object is found in sendBatteryCharge.py
	# where it reads: wirelessConnection = WirelessConnection().
	# self.host is the OfficePi server's IP address.
	# self.port is the port number that the OfficePi server is listening at.
	# self.s sets up TCP communication
	def __init__(self):
		self.host = '172.24.1.1'
		self.port = 7823
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


	# This function establishes a connection to the OfficePi server. 
	# If a connection is established, it breaks out of the loop so the 
	# program can continue running. If the server is down and a connection
	# cannot be established, it will continue to try to connect until
	# the connection is established. 
	def connectToOfficeUnit(self):
		while True:
			try:
				self.s.connect((self.host, self.port))	
				break
			except:
				continue


	# This function will send data to the OfficePi and save the data to the 
	# OfficePi's SD card. The data will then be processed to determine if
	# an alarm or alert must be made. 
	def sendData(self, data, logFile):
		self.s.send(str.encode('SEND ') + str.encode(logFile) + str.encode(' ') + str.encode(data)) 


	# This function end the RetPondPi's connection with the OfficePi. It should
	# be called after data has been sent to the OfficePi.
	def endOutflowUnitConnection(self):
		self.s.send(str.encode('EXIT'))
		self.s.close()



	# THE FOLLOWING THREE FUNCTIONS ARE FOR DEMO AND TESTING PURPOSES ONLY!!


	# This function is used for Senior Design demo purposes. It tells
	# the OfficePi the print the data that was sent to it to its console.
	def printDataToConsole(self, data):
		self.s.send(str.encode('PRINT ') + str.encode(data))  


	# This function is used for Senior Desgin demo purposes. It receives 
	# a response from the OfficePi letting the RetPondPi know that data
	# was received correctly. 
	def receiveData(self):
		reply = self.s.recv(1024) 
		return reply.decode('utf-8')


	# This function is used to shutdown the OfficePi server. This should 
	# NEVER be used during normal operation. This function is only used during 
	# the writing code stage if you need to shutdown the server for some reason.
	# If you need to remotely shutdown the server, just run the python script
	# called shutDownServer.py instead of calling this function. 
	def shutdownOfficeUnit(self):
		self.s.send(str.encode('KILL'))


