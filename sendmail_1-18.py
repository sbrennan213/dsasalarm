#!/usr/bin/python

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cruisealarm1@gmail.com", "Moves16!")
 
phone = '15169985507@vtext.com'
msg = "Testo Chango!"
server.sendmail("cruisealarm1@gmail.com", "cruisealarm1@gmail.com", msg)
server.sendmail( "cruisealarm1@gmail.com", phone, 'Test?' )
server.quit()