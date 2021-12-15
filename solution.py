# import socket module
from socket import *
# In order to terminate the program
import sys
import unicodedata
def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end
    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr =  serverSocket.accept()      #Fill in e
        try:
            message =  connectionSocket.recv(1024).decode()# Fill in start    #Fill in end
            filename = message.split()[1]
                #with open(path, encoding="utf8", errors='ignore') as f:
            f = open(filename, encoding = 'utf-8', errors = 'ignore')
                
            outputdata = f.read()# Fill in start     #Fill in end
            #print(outputdata)
                # Send one HTTP header line into socket.
            connectionSocket.send("HTTP/1.1 404 file not found\r\n\r\n".encode())
                # Fill in start
                # Fill in end
                # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
                #i = i + 1
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
        # Send response message for file not found (404)
        # Fill in start
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            connectionSocket.send("<html><head></head><body><h1>200 OK/h1></body></html>\r\n".encode())
        #    connectionSocket.send("HTTP/1.1 404 file not found\r\n\r\n".encode())

           # connectionSocket.send("<html><head></head><body><h1>404 file not found</h1></body></html>\r\n".encode())
                
        # Fill in end

        # Close client socket
            connectionSocket.close()
        # Fill in start
        # Fill in end
        except (ConnectionResetError, BrokenPipeError):
            pass
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
if __name__ == "__main__":
    webServer(13331)
