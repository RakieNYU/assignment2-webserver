#RakieNYU
# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  host = "127.0.0.1"
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind((host, port))
  #Fill in start
  serverSocket.listen(1)
  #Fill in end
  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
      try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket.
        #Fill in start
        connectionSocket.send(("HTTP/1.1 200 OK\r\n\r\n").encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        # Fill in start
        connectionSocket.send(("HTTP/1.1 404 Not Found\r\n\r\n").encode())
        connectionSocket.send("<html><head></head><body><h2>Page Not Found</h2></body></html>".encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        #Fill in end
    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
