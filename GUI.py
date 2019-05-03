import tkinter as tk

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




def clock():
    if signal == True:
        message = "signal recieved"
        root.configure(background='green')
    else:
        message = "no signal"
        root.configure(background='red')
        
    w.config(text=message) 
    root.after(10, clock) # run itself again after 10 ms

# run first time
clock()

root.mainloop()

