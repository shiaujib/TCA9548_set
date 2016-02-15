#!/usr/bin/env python
#
#
#


import sys,getopt
import time
import datetime
import random 
import TCA9548_Set
import MPU6050Read
import subprocess



#/*=========================================================================
#    I2C ADDRESS/BITS
#    -----------------------------------------------------------------------*/
TCA9548_ADDRESS =                         (0x70)    # 1110000 (A0+A1=VDD)

#/*=========================================================================*/

#/*=========================================================================
#    CONFIG REGISTER (R/W) ADDRESS WILL FOLLOW A READ/WRITE BIT
#    -----------------------------------------------------------------------*/
TCA9548_REG_CONFIG            =          (0x00)
#    /*---------------------------------------------------------------------*/

TCA9548_CONFIG_BUS0  =                (0x01)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS1  =                (0x02)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS2  =                (0x04)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS3  =                (0x08)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS4  =                (0x10)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS5  =                (0x20)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS6  =                (0x40)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS7  =                (0x80)  # 1 = enable, 0 = disable

BusChannel=[0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
fileName=['sensor0','sensor1','sensor2','sensor3','sensor4','sensor5','sensor6','sensor7']

#/*=========================================================================*/

def findElement(list,key):
    for i in list:
        if i==key:
            return 1
    return 0

    
# Main Program
def main(argv):
    try:
        opts,args=getopt.getopt(argv,"h:n:",["help=","deviceNumber"])
    except getopt.GetoptError:
        print 'usage:muti_accelerometer.py -n <deviceNumber>'
        sys.exit(2)
    if findElement(argv,'-n')==0:
        print 'usage:muti_accelerometer.py -n <deviceNumber>'
        sys.exit(2)
    for opt,arg in opts:
        if opts=='-h':
            print 'usage:muti_accelerometer.py -i <deviceNumber>'
        elif opt in ("-n","--deviceNumber"):
            deviceNum=arg
        
    print ""
    print "Sample uses 0x70" 
    print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
    print ""

    starttime = datetime.datetime.utcnow()


    tca9548 = TCA9548_Set.TCA9548_Set(addr=TCA9548_ADDRESS, bus_enable = TCA9548_CONFIG_BUS0)
    mpu6050 = MPU6050Read.MPU6050Read(0x68,1)

    file0=open(fileName[0])
    file1=open(fileName[1])
    file2=open(fileName[2])
    file3=open(fileName[3])
    file4=open(fileName[4])
    file5=open(fileName[5])
    file6=open(fileName[6])
    file7=open(fileName[7])
    fileList=[file0,file1,file2,file3,file4,file5,file6,file7]
        

    # rotates through all 4 I2C buses and prints out what is available on each

    while True:
        print "-----------BUS 0-------------------"
        for channel in BusChannel:
            tca9548.write_control_register(BusChannel[channel])
            #get gyro and accelerometer value
            gyro_xout = mpu6050.read_word_2c(0x43)
            gyro_yout = mpu6050.read_word_2c(0x45)
            gyro_zout = mpu6050.read_word_2c(0x47)
            accel_xout = mpu6050.read_word_2c(0x3b)
            accel_yout = mpu6050.read_word_2c(0x3d)
            accel_zout = mpu6050.read_word_2c(0x3f)
            fileLisy[channel].write("gyrox = %f gyroy = %f gyroz = %f \naccelx = %f accely = %f accelz = %f" %(gyro_xout,gyro_yout,gyro_zout,accel_xout,accel_yout,accel_zout))
            


if __name__=="__main__":
    main(sys.argv[1:])

