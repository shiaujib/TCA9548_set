#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
import os
import time
import struct
import threading
import sys
import numpy as np
index=0
dataNum=0

def fileTrans(sendsock,sockflag):
    global index
    global dataNum
    while 1:
        #time.sleep(1)
        if dataNum<10000000:
            conn.send("%5s\t%5s\t%5s"%(str(np.random.randint(-10,10)),str(np.random.randint(-10,10)),str(np.random.randint(-10,10))))
            #conn.send("%5s\t%5s\t%5s,"%(str(np.random.randint(-10,10)),str(np.random.randint(-10,10)),str(np.random.randint(-10,10))))
        dataNum=dataNum+1
        if sockflag==1 and dataNum>100000000:
            sendsock.close()
            conn.close()
            print "Close socket"
            sys.exit()

def main():
    fileTrans()

if __name__=="__main__":
        addr = ('192.168.211.132',8000)
        bufsize = 1024
        filename = 'sensor1.txt'
        sendsock = socket(AF_INET,SOCK_STREAM)
        sendsock.bind(addr)
        sendsock.listen(5)
        print "waiting for client connect"
        conn,addr = sendsock.accept()
        print "server already connect client...->",addr
        try:
            t=threading.Thread(target=fileTrans,args=(sendsock,1,))
            t.start()
        except KeyboardInterrupt:
            sys.exit()
             
  #      while(1):
  #          print("live")
