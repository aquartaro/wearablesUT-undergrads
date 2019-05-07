import socket
import binascii
# import matplotlib.pyplot as plt
import numpy as np
from time import sleep

#OPTING NOT TO MESS WITH PLOTTING RIGHT NOW IN FAVOR OF USING TKINTER GUI

print("i tried")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(1.0)
# Match with OpenBCI_GUI
host = "127.0.0.1"
port = 12345
s.bind((host,port))

# 0 for data stream
# 1 for rand testing
test = 1

#threshold for ON ::: Need to test for this
th = 0.5
x = np.array([1,1])
y = np.array([0,0])
# fig = plt.figure()

#Main loop for when Server Open!
while True:
   try:
        if test == 0:
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
        elif test == 1: #move the stuff in here to time out as well
          vals = [0.1,0,0,0]
          print(x ,' and ', y)

        y = np.append(y,vals[0])
        x = np.append(x,[vals[1]])

        if np.mean(y[-10::]) >= th:
          print("Above threshold")
          muscle = True
        else:
          print("did not meet conditions")
          muscle = False


        sleep(1)  




        #print("runnin'")
     




   except KeyboardInterrupt:
      # quit
      print('the control c')
      s.close()
      sys.exit(0)



   
