#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
import os
import struct


def fileTrans():
    ADDR = ('192.168.211.130',8000)
    BUFSIZE = 1024
    filename = 'sensor1.txt'
    FILEINFO_SIZE=struct.calcsize('128s32sI8s')
    sendSock = socket(AF_INET,SOCK_STREAM)

    sendSock.bind(ADDR)
    sendSock.listen(True)
    print "waiting for client connect"
    conn,addr = sendSock.accept()
    print "server already connect client...->",addr
    fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
    conn.send(fhead)
    fp = open(filename,'rb')
    while 1:
        filedata = fp.read(BUFSIZE)
        if not filedata: break
        conn.send(filedata)
    print "Finish File Tranmit..."
    fp.close()
    sendSock.close()
    conn.close()
    print "Close socket"

def main():
    fileTrans()

if __name__=="__main__":
        main()
