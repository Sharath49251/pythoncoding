import pyscreenshot as ImageGrab
import os
import time

def screenGrab():
       box=(x_pad+1,y_pad+1,x_pad+640,y_pad+749)
       im=ImageGrab.grab()
       im.save(os.getcwd() + '\\SNAPSHOT'+str(int(time.time())) +'.png','PNG')
def main():
       screenGrab()
if __name__ =='__main__':
       main()
