#!/usr/bin/python 
# -*- coding: utf-8 -*-

from socket import *
import struct
ADDR = ('192.168.211.130',8000)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
recvSock = socket(AF_INET,SOCK_STREAM)
recvSock.connect(ADDR)
#print "wait for connect..."
#conn,addr = recvSock.accept()
#print "client already connect...",addr
fhead = recvSock.recv(FILEINFO_SIZE)
filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
#print filename,temp1,filesize,temp2
print filename,len(filename),type(filename)
print filesize
filename = 'new_'+filename.strip('\00')
fp = open(filename,'wb')
restsize = filesize
print "receiving file..."
while 1:
    if restsize > BUFSIZE:
        filedata = recvSock.recv(BUFSIZE)
    else:
        filedata = recvSock.recv(restsize)
    if not filedata: break
    fp.write(filedata)
    restsize = restsize-len(filedata)
    if restsize == 0:
     break
print "Already received file，disconnecting..."
fp.close()
recvSock.close()
print "close connection..."
