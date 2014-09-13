#!/usr/bin/env python
import os, urllib2, signal, time
from private import *
#ip_pub = urllib2.urlopen('http://ipecho.net/plain').read()
#ip_pub = urllib2.urlopen('http://ip.42.pl/raw').read()
# Change this to your process name

while True:

    ip_pub = urllib2.urlopen('http://ipecho.net/plain').read()
    #print ip_pub
    if ip_pub != ip_vpn:
        #print 'vpnIP not match'
        #processname = 'transmission-daemon'
        for line in os.popen("ps xa"):
            fields = line.split()
            pid = fields[0]
            process = fields[4]
            if process.find(processname) > 0:
            # Kill the Process. Change signal.SIGHUP to signal.SIGKILL if you like
                os.kill(int(pid), signal.SIGKILL)
            # Do something else here
                print 'transmission closed!'
            # Restart the process
            #os.system(processname)
            # Hop out of loop
                break

    time.sleep(5)
