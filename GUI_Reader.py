import tkinter as tk
from tkinter import filedialog
import RunData as rd
import socket
import numpy as np
from time import sleep

root = tk.Tk()
root.geometry('400x400')

#global signal recieved for example
signal = True

# based on EMG signals, we could change background color

#Set Text indicator
w = tk.Label(root, text = 'Not Running')
w.pack()

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
run = None

#threshold for ON ::: Need to test for this
th = 0.1
x = np.array([1,1])
y = np.array([0,0])

####


def clock():
    global x, y, run
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
    startStop.configure(text='Stop Stream', command=stopStream)
    run = root.after(500, clock) # run itself again after X ms


def file_save():
    f = filedialog.asksaveasfilename(defaultextension=".txt")
    if f is None:
        return
    np.savetxt(f,np.transpose((x,y)),delimiter=',', header=' Set 1  ,  Set 2  ,', fmt = '%.4e')

def stopStream():
    #If already running, stop the data reading
    root.after_cancel(run)
    w.config(text = 'Not Running')
    startStop.configure(text='Start Stream', command=clock)
    root.configure(background='DarkOrchid3')




#Set Buttons
save = tk.Button(root, text='SAVE DATA', command=file_save)
save.pack(pady=10)
startStop = tk.Button(root,text='Start Stream', command=clock)
startStop.pack()


root.mainloop()

