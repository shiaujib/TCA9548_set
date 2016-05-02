#!/usr/bin/env python
#


import sys,getopt
import time
import datetime
import random 
import TCA9548_Set
import MPU6050Read
import subprocess
import RPi.GPIO as GPIO


#=========================================================================
# button control
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#=========================================================================

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

BusChannel=[TCA9548_CONFIG_BUS0,TCA9548_CONFIG_BUS1,TCA9548_CONFIG_BUS2]
fileName=['sensor0','sensor1','sensor2','sensor3','sensor4','sensor5','sensor6','sensor7']

#accel=[[] for i in range(int(1))]  #create dynamic list
#gyro=[[] for i in range(int(1))]

timeArray=[None]*100000000
#/*=========================================================================*/

def findElement(list,key):
    for i in list:
        if i==key:
            return 1
    return 0


def writeFile(accel , gyro ,deviceNum,count):
    file0=open(fileName[0],'w')
    file1=open(fileName[1],'w')
    file2=open(fileName[2],'w')
    file3=open(fileName[3],'w')
    file4=open(fileName[4],'w')
    file5=open(fileName[5],'w')
    file6=open(fileName[6],'w')
    file7=open(fileName[7],'w')
    timeFile=open("dataTime",'w')
    fileList=[file0,file1,file2,file3,file4,file5,file6,file7]
    for i in range (int(deviceNum)):
        for j in range(0,count*3,3):
            fileList[i].write("accelx = %f accely = %f accelz = %f\n" %(accel[i][j],accel[i][j+1],accel[i][j+2]))
    for i in range(count):
    	timeFile.write("%s\n" %timeArray[i])
    print "Experimental done"
    for i in range(int(deviceNum)):
	fileList[i].close()
    timeFile.close()
    sys.exit(2)
            
            
            
        
    
    
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

    accel=[[] for i in range(int(deviceNum))]  #create dynamic list
    gyro=[[] for i in range(int(deviceNum))]
        
    print ""
    print "Sample uses 0x70" 
    print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
    print ""

    starttime = datetime.datetime.utcnow()


    tca9548 = TCA9548_Set.TCA9548_Set(addr=TCA9548_ADDRESS, bus_enable = TCA9548_CONFIG_BUS1)
    mpu6050 = MPU6050Read.MPU6050Read(0x68,1)

    file0=open(fileName[0],'w')
    file1=open(fileName[1],'w')
    file2=open(fileName[2],'w')
    file3=open(fileName[3],'w')
    file4=open(fileName[4],'w')
    file5=open(fileName[5],'w')
    file6=open(fileName[6],'w')
    file7=open(fileName[7],'w')
    fileList=[file0,file1,file2,file3,file4,file5,file6,file7]
        

    # rotates through all 4 I2C buses and prints out what is available on each
    count=0
    flag=0
    while True:
        fileIndex=0
        input_state=GPIO.input(4)   #get switch state
	if flag==0:
	    print "getting data please press button to stop........"
	    flag+=1
        for channel in BusChannel:
   	    mpu6050 = MPU6050Read.MPU6050Read(0x68,1)
            tca9548.write_control_register(BusChannel[fileIndex])
	    #print "-----------------BUS"+str(fileIndex)+"-------------"
            #get gyro and accelerometer value
            #gyro_xout = mpu6050.read_word_2c(0x43)
            #gyro_yout = mpu6050.read_word_2c(0x45)
            #gyro_zout = mpu6050.read_word_2c(0x47)
            #accel_xout = mpu6050.read_word_2c(0x3b)
            #accel_yout = mpu6050.read_word_2c(0x3d)
            #accel_zout = mpu6050.read_word_2c(0x3f)
            #print "accelx = %f accely = %f accelz = %f\n" %(accel_xout,accel_yout,accel_zout)
            gyro[fileIndex].append(mpu6050.read_word_2c(0x43))
            gyro[fileIndex].append(mpu6050.read_word_2c(0x45))
            gyro[fileIndex].append(mpu6050.read_word_2c(0x47))
            accel[fileIndex].append(mpu6050.read_word_2c(0x3b))
            accel[fileIndex].append(mpu6050.read_word_2c(0x3d))
            accel[fileIndex].append(mpu6050.read_word_2c(0x3f))
	    if fileIndex==0 or fileIndex==1:
 	        mpu6050_sla=MPU6050Read.MPU6050Read(0x69,1)
            	gyro[fileIndex+3].append(mpu6050_sla.read_word_2c(0x43))
            	gyro[fileIndex+3].append(mpu6050_sla.read_word_2c(0x45))
            	gyro[fileIndex+3].append(mpu6050_sla.read_word_2c(0x47))
            	accel[fileIndex+3].append(mpu6050_sla.read_word_2c(0x3b))
            	accel[fileIndex+3].append(mpu6050_sla.read_word_2c(0x3d))
            	accel[fileIndex+3].append(mpu6050_sla.read_word_2c(0x3f))
	    
		
            #fileList[fileIndex].write("gyrox = %f gyroy = %f gyroz = %f \naccelx = %f accely = %f accelz = %f\n" %(gyro_xout,gyro_yout,gyro_zout,accel_xout,accel_yout,accel_zout))
            #fileList[fileIndex].write("accelx = %f accely = %f accelz = %f\n" %(accel_xout,accel_yout,accel_zout))
            #print "accelx = %f accely = %f accelz = %f\n" %(accel_xout,accel_yout,accel_zout)
	    
	    timeTmp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	    timeArray[count]=timeTmp 

            fileIndex+=1
            if fileIndex>int(deviceNum):
		fileIndex=0
                break
        count+=1
        if input_state==False:
            print "Button Pressed experimental stop"
            print "count Num = %d" %count
            break 
    writeFile(accel,gyro,deviceNum,count)
        



if __name__=="__main__":
    main(sys.argv[1:])


