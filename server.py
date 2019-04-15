import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# host = socket.gethostname()
host = "127.0.0.1"
port = 12345
s.bind((host,port))

while True:
   #c, addr = s.accept()     # Establish connection with client.
   #data, addr = s.recvfrom(1024)
   #print ('Got connection from', addr)
   #print ("the data is below:")
   print (repr(s.recv(2048)))