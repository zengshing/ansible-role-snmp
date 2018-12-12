#!/usr/bin/env python
import sys
import netsnmp

if __name__ == '__main__':
    ip = '127.0.0.1'
    snmp = netsnmp.SNMPSession(ip, 'RJKJ')
    if snmp.is_alive():
        snmp.close()
print 'test import netsnmp ok'