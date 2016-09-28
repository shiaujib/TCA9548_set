import matplotlib.pyplot as plt
import numpy as np
import time
import threading
import tcpc
import sys

tmp=[0]*100
result=[10]*100
accel=[[10 for x in range(100)] for y in range(7)]

def sensorplot():
    # loop to update the data 
    global accel
    value=[3]*100
    zero=[10]*1000
    x = np.arange(1000)
    sensor1 = zero[0:1000]
    sensor2 = zero[0:1000]
    sensor3 = zero[0:1000]
    sensor4 = zero[0:1000]
    sensor5= zero[0:1000]
    sensor6 = zero[0:1000]
    sensor7 = zero[0:1000]
    fig = plt.figure(figsize=(12,12))
    sen1f = fig.add_subplot(711)
    sen2f = fig.add_subplot(712)
    sen3f = fig.add_subplot(713)
    sen4f = fig.add_subplot(714)
    sen5f = fig.add_subplot(715)
    sen6f = fig.add_subplot(716)
    sen7f = fig.add_subplot(717)
    fig.tight_layout()
    fig.title="Sensor Data"
    # some X and Y data
    sen1f.set_ylabel('value')
    sen1f.set_xlabel('time')
    sen1f.set_ylim((0,20))
    sen1f.set_xlim((0,1000))
    sen1fr, = sen1f.plot(x,sensor1)
    ###########################################
    sx = np.arange(10000)
    sy = zero[0:1000]
    sen2f.set_ylabel('value')
    sen2f.set_xlabel('time')
    sen2f.set_ylim((0,20))
    sen2f.set_xlim((0,1000))
    sen2fr, = sen2f.plot(x,sensor2)
    ###########################################
    sen3f.set_ylabel('value')
    sen3f.set_xlabel('time')
    sen3f.set_ylim((0,20))
    sen3f.set_xlim((0,1000))
    sen3fr, = sen3f.plot(x,sensor3)
    ###########################################
    sen4f.set_ylabel('value')
    sen4f.set_xlabel('time')
    sen4f.set_ylim((0,20))
    sen4f.set_xlim((0,1000))
    sen4fr, = sen4f.plot(x,sensor4)
    ###########################################
    sen5f.set_ylabel('value')
    sen5f.set_xlabel('time')
    sen5f.set_ylim((0,20))
    sen5f.set_xlim((0,1000))
    sen5fr, = sen5f.plot(x,sensor5)
    ###########################################
    sen6f.set_ylabel('value')
    sen6f.set_xlabel('time')
    sen6f.set_ylim((0,20))
    sen6f.set_xlim((0,1000))
    sen6fr, = sen6f.plot(x,sensor6)
    ###########################################
    sen7f.set_ylabel('value')
    sen7f.set_xlabel('time')
    sen7f.set_ylim((0,20))
    sen7f.set_xlim((0,1000))
    sen7fr, = sen7f.plot(x,sensor7)
    # draw and show it
    fig.canvas.draw()
    plt.show(block=False)
    t=threading.Thread(target=tcpc.client,args=(accel,))
    t.start()
    while True:
        try:
            sensor1[:-99] = sensor1[99:]
            sensor2[:-99] = sensor2[99:]
            sensor3[:-99] = sensor3[99:]
            sensor4[:-99] = sensor4[99:]
            sensor5[:-99] = sensor5[99:]
            sensor6[:-99] = sensor6[99:]
            sensor7[:-99] = sensor7[99:]
            #y[-100:] = np.random.randn(100)
            #y[-100:] = np.arange(100)
            sensor1[-99:] = accel[0][0:99]
            sensor2[-99:] = accel[1][0:99]
            sensor3[-99:] = accel[2][0:99]
            sensor4[-99:] = accel[3][0:99]
            sensor5[-99:] = accel[4][0:99]
            sensor6[-99:] = accel[5][0:99]
            sensor7[-99:] = accel[6][0:99]
                
            # set the new data
            sen1fr.set_ydata(sensor1)
            sen2fr.set_ydata(sensor2)
            sen3fr.set_ydata(sensor3)
            sen4fr.set_ydata(sensor4)
            sen5fr.set_ydata(sensor5)
            sen6fr.set_ydata(sensor6)
            sen7fr.set_ydata(sensor7)
            fig.canvas.draw()
        except KeyboardInterrupt:
            break

if __name__=="__main__":
    #t=threading.Thread(target=tcpc.client)
    #t.start()
    sensorplot()


