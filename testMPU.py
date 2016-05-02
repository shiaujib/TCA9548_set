import smbus
import MPU6050Read
import math
import time

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


mpu6050=MPU6050Read.MPU6050Read(address=0x68)
count=0


while True:
    count+=1
#    gyro_xout = mpu6050.read_word_2c(0x43)
#    gyro_yout = mpu6050.read_word_2c(0x45)
#    gyro_zout = mpu6050.read_word_2c(0x47)

#    print "gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131)
#    print "gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131)
#    print "gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131)

    accel_xout = mpu6050.read_word_2c(0x3b)
    accel_yout = mpu6050.read_word_2c(0x3d)
    accel_zout = mpu6050.read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
    print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
    print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled
    time.sleep(0.5)
    print "total num ",count
#    print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
#    print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)


