
# The first six functions are used in the code. The code begins 
# at the very bottom with the line 
# “time.sleep(60)”

# This script establishes a socket at a given port number on the OfficePi. 
# The OfficePi will wait and listen at the port number for the RetPondPi 
# to initiate a connection. Once a connection is established, the OfficePi 
# will receive data from the RetPondPi and save the data to the SD card.

# The RetPondPi can control the OfficePi by sending commands to the OfficePi. 

# Example of how to control the OfficePi from the RetPondPi:

# The following example string will be sent to the OfficePi:
# “SEND /home/pi/Desktop/logFile.log your_Sensor_Data”

# How pythonServer.py processes this example string:
# In the function dataTransfer(), there is a line of code that reads 
# “dataMessage = data.split(‘ ‘,1)”
# This line of code splits the string sent to the OfficePi into 2 parts. 
# Everything up until the first space will be stored in dataMessage[0] and 
# everything after the first space will be stored in dataMessage[1].
# For our example: dataMessage[0] will contain the word “SEND” and dataMessage[1] 
# will contain the rest of the string “/home/pi/Desktop/logFile.log your_Sensor_Data”.

# The code then checks the word stored in dataMessage[0]. 
# If it equals “SEND” which it does for our example, then the string 
# stored in dataMessage[1] is split again separating 
# “/home/pi/Desktop/logFile.log” and “your_Sensor_Data” in two. 
# The function SEND() is then called and the logFile and sensor_data is 
# passed into the function.

# The SEND() function saves the data to the logFile name that was passed to it. 
# Then it calls the PROCESS() function. 

# For the our project, we used the PROCESS() function to check the “data_message” 
# that was sent. If “LOW” was sent, then the OfficePi will play a file that uses a 
# speaker to say “Low Battery” for the office employees to hear. 

# For a future sensor team, you will use the PROCESS() file to check 
# your “sensor_data_message” to see if outflow has occurred. (When outflow occurs, 
# you will probably send a message to the OfficePi that says something like “OUTFLOW”). 
# You will add an if statement to the PROCESS() function that checks to see if the 
# sent message = “OUTFLOW”. If it does, do what is needed. 


import time
import socket
import os


host = ''
port = 7823


# This function creates a socket and binds it to a port number
def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete")
    return s


# Using this function, the server waits and listens at the port
# for the RetPondPi to initiate a connection 
def setupConnection():
    s.listen(1)  #Allows one connection at a time
    connection, address = s.accept()
    print("Connected to: " + address[0])
    return connection


# This function is used for Senior Design demo purposes only
def PRINT(dataMessage):
    print(dataMessage[1])
    reply = "Data displayed"
    return reply


# This function checks the dataMessage that is sent to the OfficePi
# and reacts accordingly. 
# Example: when the battery data sent = "LOW", this function plays 
# a .wav file that uses a speaker to say "Low Battery". 
def PROCESS(dataMessage, logFile):
    if logFile == "/home/pi/Desktop/testBatteryLogFileEachMin.log":
        if dataMessage == "LOW":
            os.system("aplay /home/pi/Desktop/lowBattery.wav")


    # Future Ingram Teams: 
    # this is where you alert that outflow has occurred
    # WRITE CODE HERE!

    # elif logFile == "your log file name":
    #    if dataMessage = "OUTFLOW":
    #       do whatever


    # For some reason the code wouldn't work without this function
    # containing a return statement so it was included here. 
    reply = "Data Saved"
    return reply
    

# This function saves the dataMessage to the SD card on the 
# OfficePi. It saves it to a file named in logFile.
def SEND(dataMessage, logFile):
    with open(logFile, "a") as theLogFile:
        theLogFile.write(dataMessage + '\n')

    reply = PROCESS(dataMessage, logFile)

    return reply


# This function receives the data from the RetPondPi. It then
# splits the first word off of the data and uses it to determine
# what to do next. 
def dataTransfer(connection):

    # Sends/receives data until told not to
    while True:
        data = connection.recv(1024)
        data = data.decode('utf-8')

        # Split data into command word and rest of data
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]

        if command == 'PRINT':
            reply = PRINT(dataMessage)

        elif command == 'SEND':
            dataMessage = dataMessage[1].split(' ', 1)
            logFile = dataMessage[0]
            dataMessage = dataMessage[1]
            reply = SEND(dataMessage, logFile)

        elif command == 'EXIT':
            print("Client has left")
            break

        elif command == 'KILL':
            print("Server is shutting down")
            file.close()
            s.close()
            break
            
        else:
            reply = 'Unknown command'

        # Send reply back to client
        connection.sendall(str.encode(reply))

    connection.close()




# THIS IS WHERE THE CODE BEGINS

time.sleep(60)
s = setupServer()

while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        break
