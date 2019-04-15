import socket

print("i tried")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# host = socket.gethostname()
host = "127.0.0.1"
port = 12345
s.bind((host,port))
while True:
   try:
      #c, addr = s.accept()     # Establish connection with client.
      #data, addr = s.recvfrom(1024)
      #print ('Got connection from', addr)
      print ("the data is below:")
      #BCIData = s.recv(2048)
      #decode = BCIData.decode('UTF-8')

      print (repr(s.recv(2048)))
      print("runnin'")
      
   except KeyboardInterrupt:
      # quit
      print('the control c')
      s.close()
      sys.exit(0)

   
