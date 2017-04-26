__author__ = "Nathan Evans"

from sense_hat import SenseHat
from datetime import datetime
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)

def getTime():
    return str(datetime.now()).split(" ")[1].split(".")[0].split(":")

"""
Sets the pixels for the hour

hh - integer representation of the hour to be set

"""
def setHours(hh=0):
    #hh 10s place
    tens = '{0:03b}'.format(int(str(hh)[0]))
    setTens(tens,0)

    #hh 1s place
    ones = '{0:04b}'.format(int(str(hh)[1]))
    setOnes(ones, 1)

(":")

"""
Sets the pixels for the minute

mm - integer representation of the minute to be set

"""
def setMinutes(mm=0):
    #mm 10s place
    tens = '{0:03b}'.format(int(str(mm)[0]))
    setTens(tens, 3)

    #mm 1s place
    ones = '{0:04b}'.format(int(str(mm)[1]))
    setOnes(ones, 4)

"""
Sets the pixels for the second

ss - integer representation of the second to be set

"""
def setSeconds(ss=0):
    #ss 10s place
    tens = '{0:03b}'.format(int(str(ss)[0]))
    setTens(tens,6)
    
    #ss 1s place
    ones = '{0:04b}'.format(int(str(ss)[1]))
    setOnes(ones, 7)


"""
Sets the appropriate pixels for the ones column of the number entered

oneString - A binary representation of the number belonging in the ones column
    ex)"1001" = 8

pixelColumn - the column value of the pixels used to represent the ones place
    seconds -> 7, minutes -> 4, hours -> 1
"""
def setOnes(oneString="",pixelColumn=0):
    for i in range(4):
        if(oneString[i] == "1"):
            sense.set_pixel(pixelColumn, 4+i, blue)

"""
Sets the appropriate pixels for the ones column of the number entered

oneString - A binary representation of the number belonging in the ones column
    ex)"1001" = 8

pixelColumn - the column value of the pixels used to represent the ones place
    seconds -> 6, minutes -> 3, hours -> 0
"""
def setTens(tenString="", pixelColumn=0):
    for i in range(3):
        if(tenString[i] == "1"):
            sense.set_pixel(pixelColumn,5+i, blue)

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

