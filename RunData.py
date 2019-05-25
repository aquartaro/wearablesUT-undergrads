import socket
import numpy as np
from time import sleep

#Main loop for when Server Open!
def RunData(test, s, th, x, y):
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
            vals = [0,0,0,0]
        elif test == 1: #move the stuff in here to time out as well
          vals = [0.1,0,0,0]
          print(x ,' and ', y)

        y = np.append(y,vals[0])
        x = np.append(x,vals[1])
        y = y.astype('float')

        if np.mean(np.abs(y[-10::])) >= th:
          #print("Above threshold")
          muscle = True
        else:
          #print("did not meet conditions")
          muscle = False

        
        #sleep(1)  
        return [muscle, x, y]
   except KeyboardInterrupt:
      # quit
      print('the control c')
      s.close()
      sys.exit(0)
