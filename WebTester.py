#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import time

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
                response = "0"

            if response != 200:
                logfile.write('OFFLINE;' + lines[counter])
            else:
                logfile.write('ONLINE;' + lines[counter])
            counter = counter + 1
    except ValueError:
        print ("Error in the Links!")
    time.sleep(5)
    print ("ende")