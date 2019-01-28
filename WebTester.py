#!/usr/bin/python
# -*- coding: utf-8 -*-

# /usr/bin/python

import urllib.request
import time
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

def send_email(subject, body, toaddr="valentin.kummert@webdesign-coburg.de"):
	
	with open('config.txt') as fileline:
		configlines = fileline.readlines()
	
	fromaddr = configlines[0].rstrip()
	msg = MIMEText(body, 'plain')
	msg['To'] = toaddr
	msg['Subject'] = subject
	server = SMTP(configlines[1].rstrip())
	server.login(fromaddr, configlines[2].rstrip())
	server.sendmail(fromaddr, toaddr, msg.as_string())
	server.quit()

while True:
    with open('links.txt') as f:
        lines = f.readlines()
    counter = 0
    logfile = open('log.txt', 'w')

    try:
        for val in lines:
            try:
                response = \
                    urllib.request.urlopen(lines[counter]).getcode()
            except urllib.error.URLError:
                response = '0'

            if response != 200:
            	send_email("Web-Alert!", lines[counter]+"is Offline!")
            	logfile.write('OFFLINE;' + lines[counter])
            else:
            	logfile.write('ONLINE;' + lines[counter])
            counter = counter + 1
    except ValueError:
        print ('Error in the Links!')
    time.sleep(60)