#!/usr/bin/python

import smtplib
import time, datetime
import RPi.GPIO as GPIO
from email.mime.text import MIMEText


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.output(14, GPIO.HIGH)

hostName = "cruisealarm1@gmail.com"
hostPassword = "Moves16!"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(hostName, hostPassword)

smsGateway = ["txt.att.net", "sms.myboostmobile.com", "messaging.sprintpcs.com", "tmomail.net", "vtext.com",
              "vmobl.com"]


phone = open("/home/pi/Desktop/dsasalarm/RaspberryPi/phone.txt","r")
phone = phone.read()
address = open("/home/pi/Desktop/dsasalarm/RaspberryPi/address.txt","r")
address = address.read()
employeeName = open("/home/pi/Desktop/dsasalarm/RaspberryPi/employee.txt","r")
employeeName = employeeName.read()
email = open("/home/pi/Desktop/dsasalarm/RaspberryPi/email.txt","r")
email = email.read()
armState = open("/home/pi/Desktop/dsasalarm/RaspberryPi/armState.txt","r")
armState = armState.read()
localTime = time.localtime()
dateTime = str(localTime[1] )+ "/" + str(localTime[2]) + "/" + str(localTime[0])

clockTime = datetime.datetime.now().strftime("%I:%M %p")




if armState == '1':

   
    msg = "Motion has been detected at " + address + " on " + dateTime + ". This house alarm system was set up by " + employeeName
    txtMSG = MIMEText(msg).as_string()
    
    headers = ['From: {}'.format(hostName),
               'Subject: {}'.format("Motion Detected"),
               'To: {}'.format(email)]

    msg_body = '\r\n'.join(headers) + '\r\n\r\n' + msg




    server.sendmail(hostName, email, msg_body)

    for i in range(0,5):
        server.sendmail( "cruisealarm1@gmail.com", phone + "@" + smsGateway[i], txtMSG)

GPIO.output(14, GPIO.LOW)


server.quit()


