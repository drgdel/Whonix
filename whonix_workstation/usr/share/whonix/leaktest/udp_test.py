#! /usr/bin/env python

## This file is part of Whonix.
## Copyright (C) 2012 - 2014 Patrick Schleizer <adrelanos@riseup.net>
## See the file COPYING for copying conditions.

import sys
from scapy.all import *

#define the target gateway & data payload
target = "scanme.nmap.org"
data = "testing"

#define packets
ip = IP()
udp = UDP()

#define packet parameters
ip.dst = target

#loop through all TCP ports
for udp_port in range(0,65535):
        udp.dport = udp_port
        send(ip/udp/data)
