# tcp client 
from socket import *
from time import ctime

# tcp socket
HOST = 'localhost'
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST, PORT)

from socket import *

tcpCliSock = socket(AF_INET, SOCK_STREAM)

tcpCliSock.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break;
    else:
        tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFFSIZE)
    if not data:
        break;
    else:
        print(data)
    pass

tcpCliSock.close()