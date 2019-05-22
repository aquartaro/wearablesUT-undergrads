import tkinter as tk
import RunData as rd
import socket
import numpy as np
from time import sleep

root = tk.Tk()
root.maxsize(400, 400)

#global signal recieved for example
signal = True

# based on EMG signals, we could change background color

w = tk.Label(root)
w.pack()

#for i in range(6):
#    sleep(1) # Need this to slow the changes down
#    var.set('goodbye' if i%2 else 'hello')
#    root.update_idletasks()

#SOCKET AND BOOLEAN STUFF
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
th = 0.1
x = np.array([1,1])
y = np.array([0,0])

####


def clock():
    global x, y
    data = rd.RunData(test, s, th, x, y)
    muscle = data[0]
    x = data[1]
    y = data[2]
    print(muscle)

    if muscle == True:
        message = "signal recieved"
        root.configure(background='green')
    else:
        message = "no signal"
        root.configure(background='red')
        
    w.config(text=message) 
    root.after(500, clock) # run itself again after 10 ms

# run first time
clock()

root.mainloop()

