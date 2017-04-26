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
    for i in range(4):
        if(ones[i] == "1"):
            sense.set_pixel(1,4+i,blue)

def setMinutes(mm=0):
    #mm 10s place
    tens = '{0:03b}'.format(int(str(mm)[0]))
    for y in range(3):
        if(tens[y] == "1"):
            sense.set_pixel(3, 5+y, blue)

    #mm 1s place
    ones = '{0:04b}'.format(int(str(mm)[1]))
    for i in range(4):
        if(ones[i] == "1"):
            sense.set_pixel(4,4+i,blue)

def setSeconds(ss=0):
    #ss 10s place
    tens = '{0:03b}'.format(int(str(ss)[0]))
    for y in range(3):
        if(tens[y] == "1"):
            sense.set_pixel(6, 5+y, blue)

     #ss 1s place
    ones = '{0:04b}'.format(int(str(ss)[1]))
    for i in range(4):
        if(ones[i] == "1"):
            sense.set_pixel(7,4+i,blue)

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

