import webbrowser
import time
import datetime

import tkinter as tk




master = tk.Tk()
a = tk.Label(master, 
         text="Website").grid(row=0)
b = (tk.Label(master, 
         text='Times to open').grid(row=1))
c = (tk.Label(master, 
         text='Range').grid(row=2))
d = (tk.Label(master, 
         text='time').grid(row=3))

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


def run():
    #print("website: %s\nLtimes: %s" % (e1.get(), e2.get()))
    website = e1.get()
    number = ( int(e2.get())+ 1)
    therange = int(e3.get())
    stopwatch = int(e4.get())
    
    i = 0
    for i in range(0,therange):#change range to how many time loop should run for
        while i < number:
            webbrowser.open(website, new=4)
            i +=1
        time.sleep(stopwatch)
    

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=4, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Start Test', command= run).grid(row=4, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)



 

  


#sbmitbtm = run()
  


