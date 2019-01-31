#!/usr/bin/python
# -*- coding: utf-8 -*-

# /usr/bin/python

import urllib.request
import time
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

firststart = 0
alertmail = []

with open('config.txt') as fileline:
        configlines = fileline.readlines()

def send_email(subject, body, toaddr=configlines[3].rstrip()):

    fromaddr = configlines[0].rstrip()
    msg = MIMEText(body, 'plain')
    msg['To'] = toaddr
    msg['Subject'] = subject
    server = SMTP(configlines[1].rstrip())
    server.login(fromaddr, configlines[2].rstrip())
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()


while True:
    counter = 0
    logfile = open('log.txt', 'w')

    with open('links.txt') as f:
        lines = f.readlines()        
    
    if firststart == 0:
        for x in range(0, 100):
            alertmail.append(0)
        firststart = 1

    try:
        for val in lines:
            try:
                response = urllib.request.urlopen(lines[counter]).getcode()
            except urllib.error.URLError:
                response = '0'
                
            if response != 200:
                if alertmail[counter] == 3:
                    send_email('Web-Alert!', lines[counter] + 'is Offline!')
                alertmail[counter] = alertmail[counter] + 1 
                logfile.write('OFFLINE;' + lines[counter])
            else:
                logfile.write('ONLINE;' + lines[counter])
                if alertmail[counter] > 0:
                    alertmail[counter] = 0
            counter = counter + 1
    except ValueError:
        print ('Error in the Links!')
    time.sleep(5)