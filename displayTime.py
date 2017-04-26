__author__ = "Nathan Evans"

from sense_hat import SenseHat
from datetime import datetime
from time import sleep

sense = SenseHat()

blue = (0, 0, 255)

def getTime():
    return str(datetime.now()).split(" ")[1].split(".")[0].split(":")

"""
Returns the string representation of the ones digit of a number in binary
    ex) getOnes(9 -> 1001)

num - the number to convert
"""
def getOnes(num):
    strNum = str(num)
    return '{0:04b}'.format(int(strNum[len(strNum)-1]))

"""
Returns the string representation of the tens digit of a number <=79 in binary
    ex) getTens(79 -> 111)

num - the number to convert
"""
def getTens(num):
    strNum = str(num)
    if(int(num) < 10):
        strNum = "0"
    return '{0:03b}'.format(int(strNum[len(strNum)-2]))

"""
Sets the pixels for the hour

hh - string representation of the hour to be set

"""
def setHours(hh=0):
    #hh 10s place
    setTens(hh,0)

    #hh 1s place
    setOnes(hh, 1)


"""
Sets the pixels for the minute

mm - string representation of the minute to be set

"""
def setMinutes(mm=0):
    #mm 10s place
    setTens(mm, 3)

    #mm 1s place
    setOnes(mm, 4)

"""
Sets the pixels for the second

ss - string representation of the second to be set

"""
def setSeconds(ss=0):
    #ss 10s place
    setTens(ss,6)
    
    #ss 1s place
    setOnes(ss, 7)


"""
Sets the appropriate pixels for the ones column of the number entered

num - string representation of the number to be set

pixelColumn - the column value of the pixels used to represent the ones place
    seconds -> 7, minutes -> 4, hours -> 1
"""
def setOnes(num="",pixelColumn=0):
    oneString = getOnes(num)
    for i in range(4):
        if(oneString[i] == "1"):
            sense.set_pixel(pixelColumn, 4+i, blue)

"""
Sets the appropriate pixels for the ones column of the number entered

num - string representation of the number to be set

pixelColumn - the column value of the pixels used to represent the ones place
    seconds -> 6, minutes -> 3, hours -> 0
"""
def setTens(num="", pixelColumn=0):
    tenString = getTens(num)
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

