import socket
import binascii

print("i tried")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(1.0)
# Match with OpenBCI_GUI
host = "127.0.0.1"
port = 12345
s.bind((host,port))


#Main loop for when Server Open!
while True:
   try:
        try:
            data, addr = s.recvfrom(1024)
            #print ('Got connection from', addr)
            print ("the data is below:")
            #BCIData = s.recv(2048)
            #decode = BCIData.decode('UTF-8')
            print (data, addr)
            print(type(data))
            decode_all = data.decode("UTF-8")
            decode_all = decode_all.split("[")
            decode_all[1] = decode_all[1].strip()
            decode_all[1] = decode_all[1].strip(']}')
            vals = decode_all[1].split(',')
            print(vals)
            #print (vals[0], '|',vals[1])
        except socket.timeout:
            print('REQUEST TIMED OUT')

        #print("runnin'")
     




   except KeyboardInterrupt:
      # quit
      print('the control c')
      s.close()
      sys.exit(0)

   
