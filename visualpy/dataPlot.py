import matplotlib.pyplot as plt
import numpy as np
import time
import threading
import tcpc
import sys

tmp=[0]*100
result=[10]*100

def sensorplot():
    # loop to update the data 
    global result
    value=[3]*100
    zero=[10]*1000
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
    x = np.arange(1000)
    y = zero[0:1000]
    sen1f.set_ylabel('value')
    sen1f.set_xlabel('time')
    sen1f.set_ylim((0,20))
    sen1f.set_xlim((0,1000))
    sen1fr, = sen1f.plot(x, y)
    ###########################################
    sx = np.arange(10000)
    sy = zero[0:1000]
    sen2f.set_ylabel('value')
    sen2f.set_xlabel('time')
    sen2f.set_ylim((0,20))
    sen2f.set_xlim((0,1000))
    sen2fr, = sen2f.plot(x,y)
    ###########################################
    sen3f.set_ylabel('value')
    sen3f.set_xlabel('time')
    sen3f.set_ylim((0,20))
    sen3f.set_xlim((0,1000))
    sen3fr, = sen3f.plot(x,y)
    ###########################################
    sen4f.set_ylabel('value')
    sen4f.set_xlabel('time')
    sen4f.set_ylim((0,20))
    sen4f.set_xlim((0,1000))
    sen4fr, = sen4f.plot(x,y)
    ###########################################
    sen5f.set_ylabel('value')
    sen5f.set_xlabel('time')
    sen5f.set_ylim((0,20))
    sen5f.set_xlim((0,1000))
    sen5fr, = sen5f.plot(x,y)
    ###########################################
    sen6f.set_ylabel('value')
    sen6f.set_xlabel('time')
    sen6f.set_ylim((0,20))
    sen6f.set_xlim((0,1000))
    sen6fr, = sen6f.plot(x,y)
    ###########################################
    sen7f.set_ylabel('value')
    sen7f.set_xlabel('time')
    sen7f.set_ylim((0,20))
    sen7f.set_xlim((0,1000))
    sen7fr, = sen7f.plot(x,y)
    # draw and show it
    fig.canvas.draw()
    plt.show(block=False)
    t=threading.Thread(target=tcpc.client,args=(result,))
    t.start()
    while True:
        try:
            y[:-99] = y[99:]
            #y[-100:] = np.random.randn(100)
            #y[-100:] = np.arange(100)
            y[-99:] = result[0:99]
            # set the new data
            sen1fr.set_ydata(y)
            sen2fr.set_ydata(y)
            sen3fr.set_ydata(y)
            sen4fr.set_ydata(y)
            sen5fr.set_ydata(y)
            sen6fr.set_ydata(y)
            sen7fr.set_ydata(y)
            fig.canvas.draw()
        except KeyboardInterrupt:
            break

if __name__=="__main__":
    #t=threading.Thread(target=tcpc.client)
    #t.start()
    sensorplot()


