from sense_hat import SenseHat
from datetime import datetime
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)

def getTime():
    return str(datetime.now()).split(" ")[1].split(".")[0].split(":")

def setHours(hh=0):
    #hh 10s place
    tens = '{0:02b}'.format(int(str(hh)[0]))
    if(tens[1] == "1"):
        sense.set_pixel(0,7,blue)
    if(tens[0] == "1"):
        sense.set_pixel(0,6,blue)

    #hh 1s place
    ones = '{0:04b}'.format(int(str(hh)[1]))
    if(ones[3] == "1"):
        sense.set_pixel(1,7,blue)
    if(ones[2] == "1"):
        sense.set_pixel(1,6,blue)
    if(ones[1] == "1"):
        sense.set_pixel(1,5,blue)
    if(ones[0] == "1"):
        sense.set_pixel(1,4,blue)

def setMinutes(mm=0):
    #mm 10s place
    tens = '{0:03b}'.format(int(str(mm)[0]))
    if(tens[2] == "1"):
        sense.set_pixel(3,7,blue)
    if(tens[1] == "1"):
        sense.set_pixel(3,6,blue)
    if(tens[0] == "1"):
        sense.set_pixel(3,5,blue)

    #mm 1s place
    ones = '{0:04b}'.format(int(str(mm)[1]))
    if(ones[3] == "1"):
        sense.set_pixel(4,7,blue)
    if(ones[2] == "1"):
        sense.set_pixel(4,6,blue)
    if(ones[1] == "1"):
        sense.set_pixel(4,5,blue)
    if(ones[0] == "1"):
        sense.set_pixel(4,4,blue)

def setSeconds(ss=0):
    #ss 10s place
    tens = '{0:03b}'.format(int(str(ss)[0]))
    if(tens[2] == "1"):
        sense.set_pixel(6,7,blue)
    if(tens[1] == "1"):
        sense.set_pixel(6,6,blue)
    if(tens[0] == "1"):
        sense.set_pixel(6,5,blue)

     #ss 1s place
    ones = '{0:04b}'.format(int(str(ss)[1]))
    if(ones[3] == "1"):
        sense.set_pixel(7,7,blue)
    if(ones[2] == "1"):
        sense.set_pixel(7,6,blue)
    if(ones[1] == "1"):
        sense.set_pixel(7,5,blue)
    if(ones[0] == "1"):
        sense.set_pixel(7,4,blue)

white = (255,255,255)
while True:
    sense.clear()
    x = 0
    while x < 8:
        sense.set_pixel(2,x,white)
        sense.set_pixel(5,x,white)
        x+=1
    dTime = getTime()
    print(dTime)
    setHours(dTime[0])
    setMinutes(dTime[1])
    setSeconds(dTime[2])
    sleep(1)

