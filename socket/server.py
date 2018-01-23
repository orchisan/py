# tcp sockect
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpSrvSock = socket(socket.AF_INET, SOCK_STREAM)

tcpSrvSock.bind(ADDR)

tcpSrvSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSrvSock.accept()
    print('...connected from : ', addr)
    
while TRUE:
    data = tcpCliSock.recv(BUFFSIZE)
    if not data:
        break;
    tcpCliSock.send('[%s] %s' %(ctime(), data))

tcpCliSock.close()
tcpSrvSock.close()