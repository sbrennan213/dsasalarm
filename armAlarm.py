#!/usr/bin/python

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

    
#Create & Configure root 
root = Tk()
root.wm_title("Arm Alarm")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

def setup():
    add = address.get()
    f = open('/home/pi/Desktop/dsasalarm/RaspberryPi/address.txt','w')
    f.write(add)
    f.close()
    
    emp = employee.get()
    f = open('/home/pi/Desktop/dsasalarm/RaspberryPi/employee.txt','w')
    f.write(emp)
    f.close()
    
    em = email.get()
    f = open('/home/pi/Desktop/dsasalarm/RaspberryPi/email.txt','w')
    f.write(em)
    f.close()
    
    ph = phone.get()
    f = open('/home/pi/Desktop/dsasalarm/RaspberryPi/phone.txt','w')
    f.write(ph)
    f.close()

def arm():
    f = open('/home/pi/Desktop/dsasalarm/RaspberryPi/armState.txt','r')
    f = f.read()
    if f == '1':
        f = open('/home/pi/Desktop/dsasalarm/RaspberryPi/armState.txt','w')
        f.write('0')
        f.close()
    else:
        f = open('/home/pi/Desktop/dsasalarm/RaspberryPi/armState.txt','w')
        f.write('1')
        f.close()

Label(frame, text= "Address:").grid(row=0)
Label(frame, text= "Employee Name:").grid(row=1)
Label(frame, text= "Notification email:").grid(row=2)
Label(frame, text="Notification phone number:").grid(row=3)

address = Entry(frame)
employee = Entry(frame)
email = Entry(frame)
phone = Entry(frame)

setup = Button(frame, text = 'Setup', command = setup)
arm = Button(frame, text = 'Arm', command = arm)

address.grid(row=0, column=1)
employee.grid(row=1, column=1)
email.grid(row=2, column=1)
phone.grid(row=3, column=1)
setup.grid(row=4)
arm.grid(row=4, column=1)

root.mainloop()
