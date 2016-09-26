#!/usr/bin/python 
# -*- coding: utf-8 -*-

from socket import *
import math
import struct
SIZE=1000
sensor1=[]*SIZE
sensor2=[]*SIZE
sensor3=[]*SIZE
sensor4=[]*SIZE
sensor5=[]*SIZE
sensor6=[]*SIZE
sensor7=[]*SIZE
sensor8=[]*SIZE
sensor9=[]*SIZE
sensor10=[]*SIZE
result=[10]*100
def client(result):
    ADDR = ('192.168.211.132',8000)
    recvSock = socket(AF_INET,SOCK_STREAM)
    recvSock.connect(ADDR)
    index=0
    aindex=0
    BUFSIZE=17
    print "receiving file..."
    while 1:
        if index<100000000:
            message=recvSock.recv(BUFSIZE)
            #message2=recvSock.recv(BUFSIZE)
            #array=message.split(',')
            #print("len: %d "%len(array))
            #print array
            tvalue=message.split('\t')
            val=math.sqrt(math.pow(int(tvalue[0]),2)+math.pow(int(tvalue[1]),2)+math.pow(int(tvalue[2]),2))
            result[aindex]=val
            aindex=aindex+1
            '''
            for i in range(3):
                tvalue=array[i].split('\t')
                val=math.sqrt(math.pow(int(tvalue[0]),2)+math.pow(int(tvalue[1]),2)+math.pow(int(tvalue[2]),2))
                result[aindex]=val
                aindex=aindex+1
                #print aindex
            '''
            if aindex>=98:
                aindex=0
            '''
            for i range(3):
                accel[fileIndex].append(int(array[i]))
            '''
            #print message2
            #print ('%s index:%d \n' %(message,index))
        else:
            break
        index=index+1

    print "Already received file，disconnecting..."
    recvSock.close()
    print "close connection..."

if __name__=="__main__":
    client(result)
