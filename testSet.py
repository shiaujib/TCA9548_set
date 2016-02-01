#!/usr/bin/env python
#
#
#

# imports

import sys
import time
import datetime
import random 
import TCA9548_Set
import subprocess



#/*=========================================================================
#    I2C ADDRESS/BITS
#    -----------------------------------------------------------------------*/
TCA9548_ADDRESS =                         (0x70)    # 1110011 (A0+A1=VDD)
#/*=========================================================================*/

#/*=========================================================================
#    CONFIG REGISTER (R/W)
#    -----------------------------------------------------------------------*/
TCA9548_REG_CONFIG            =          (0x00)
#    /*---------------------------------------------------------------------*/

TCA9548_CONFIG_BUS0  =                (0x01)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS1  =                (0x02)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS2  =                (0x04)  # 1 = enable, 0 = disable 
TCA9548_CONFIG_BUS3  =                (0x08)  # 1 = enable, 0 = disable 

#/*=========================================================================*/

# Main Program

print ""
print "Sample uses 0x70" 
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

tca9548 = SDL_Pi_TCA9548.SDL_Pi_TCA9548(addr=TCA9548_ADDRESS, bus_enable = TCA9548_CONFIG_BUS0)

# rotates through all 4 I2C buses and prints out what is available on each

while True:
  	print "-----------BUS 0-------------------"
		
 	tca9548.write_control_register(TCA9548_CONFIG_BUS0)
	# read the control register back
	control_register = tca9548.read_control_register()
	print "tca9548 control register B3-B0 = 0x%x"% (control_register & 0x0f )
	print "ignore Interrupts if INT3' - INT0' not connected"
	print "tca9548 control register Interrupts = 0x%x"% ((control_register & 0xf0) >> 4)
	
	i2ccommand = "sudo i2cdetect -y 1"	
	output = subprocess.check_output (i2ccommand,shell=True, stderr=subprocess.STDOUT )
	print output

  	print "-----------------------------------"
	print
	time.sleep(5.0)

  	print "-----------BUS 1-------------------"
		
 	tca9548.write_control_register(TCA9548_CONFIG_BUS1)
	# read the control register back
	control_register = tca9548.read_control_register()
	print "tca9548 control register B3-B0 = 0x%x"% (control_register & 0x0f )
	print "ignore Interrupts if INT3' - INT0' not connected"
	print "tca9548 control register Interrupts = 0x%x"% ((control_register & 0xf0) >> 4)
	
	i2ccommand = "sudo i2cdetect -y 1"	
	output = subprocess.check_output (i2ccommand,shell=True, stderr=subprocess.STDOUT )
	print output

  	print "-----------------------------------"
	print
	time.sleep(5.0)

  	print "-----------BUS 2-------------------"
		
 	tca9548.write_control_register(TCA9548_CONFIG_BUS2)
	# read the control register back
	control_register = tca9548.read_control_register()
	print "tca9548 control register B3-B0 = 0x%x"% (control_register & 0x0f )
	print "ignore Interrupts if INT3' - INT0' not connected"
	print "tca9548 control register Interrupts = 0x%x"% ((control_register & 0xf0) >> 4)
	
	i2ccommand = "sudo i2cdetect -y 1"	
	output = subprocess.check_output (i2ccommand,shell=True, stderr=subprocess.STDOUT )
	print output

  	print "-----------------------------------"
	print
	time.sleep(5.0)

  	print "-----------BUS 3-------------------"
		
 	tca9548.write_control_register(TCA9548_CONFIG_BUS3)
	# read the control register back
	control_register = tca9548.read_control_register()
	print "tca9548 control register B3-B0 = 0x%x"% (control_register & 0x0f )
	print "ignore Interrupts if INT3' - INT0' not connected"
	print "tca9548 control register Interrupts = 0x%x"% ((control_register & 0xf0) >> 4)
	
	i2ccommand = "sudo i2cdetect -y 1"	
	output = subprocess.check_output (i2ccommand,shell=True, stderr=subprocess.STDOUT )
	print output

  	print "-----------------------------------"
	print
	time.sleep(5.0)

