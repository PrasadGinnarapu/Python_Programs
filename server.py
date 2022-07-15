#To recive the Packet or data
import socket
# udp protocol
myp = socket.SOCK_DGRAM



#net address family :ipv4
afn = socket.AF_INET



soc = socket.socket(afn,myp)



ip = "192.168.2.187"
port = 1234



soc.bind((ip,port))



inp = soc.recvfrom(1024)
print(inp)
