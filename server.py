import socket

print("i tried")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(1.0)
# Match with OpenBCI_GUI
host = "127.0.0.1"
port = 12345
s.bind((host,port))

while True:
   try:
        try:
            data, addr = s.recvfrom(1024)
            #print ('Got connection from', addr)
            print ("the data is below:")
            #BCIData = s.recv(2048)
            #decode = BCIData.decode('UTF-8')
            print (data)
        except socket.timeout:
            print('REQUEST TIMED OUT')

        print("runnin'")
      
   except KeyboardInterrupt:
      # quit
      print('the control c')
      s.close()
      sys.exit(0)

   
