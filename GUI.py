__author__ = "Matthew Dunn"

import Tkinter
# import displayTime

#set variables
auto=True
root = Tkinter.Tk()

#import images for buttons
play=Tkinter.PhotoImage(file="play.gif")
pause=Tkinter.PhotoImage(file="pause.gif")
reset=Tkinter.PhotoImage(file="reset.gif")
uparrow=Tkinter.PhotoImage(file="uparrow.gif")
downarrow=Tkinter.PhotoImage(file="downarrow.gif")
send=Tkinter.PhotoImage(file="send.gif")




def getAutoStatus(var):
    if var:
        return play
    else:
        return pause

def updateAuto():
    global auto #displayTime.auto
    auto = not auto #displayTime.toggleAuto
    print(auto)
    newimage = getAutoStatus(auto)
    toggleAutoButton.config(image=newimage)

def resetTime():
    print("reset")

def incrementHours():
    print("ihour")

def decrementHours():
    print("dhour")

def incrementMinutes():
    print("imin")

def decrementMinutes():
    print("dmin")

def incrementSeconds():
    print("isec")

def decrementSeconds():
    print("dsec")

def sendValue():
    print("send")

upArrowHours = Tkinter.Button(root, command=incrementHours)
upArrowHours.config(image=uparrow)
upArrowHours.grid(row=0, column=0)

downArrowHours = Tkinter.Button(root, command=decrementHours)
downArrowHours.config(image=downarrow)
downArrowHours.grid(row=2, column=0)


upArrowMinutes = Tkinter.Button(root, command=incrementMinutes)
upArrowMinutes.config(image=uparrow)
upArrowMinutes.grid(row=0, column=1)

downArrowMinutes = Tkinter.Button(root, command=decrementMinutes)
downArrowMinutes.config(image=downarrow)
downArrowMinutes.grid(row=2, column=1)


upArrowSeconds = Tkinter.Button(root, command=incrementSeconds)
upArrowSeconds.config(image=uparrow)
upArrowSeconds.grid(row=0, column=2)

downArrowSeconds = Tkinter.Button(root, command=decrementSeconds)
downArrowSeconds.config(image=downarrow)
downArrowSeconds.grid(row=2, column=2)


resetButton= Tkinter.Button(root, command=resetTime) #get Datetime then play
resetButton.config(image=reset)
resetButton.grid(row=1, column=3)


toggleAutoButton = Tkinter.Button(root, command=updateAuto)
toggleAutoButton.config(image=play)
toggleAutoButton.grid(row=1, column=4)


sendButton=Tkinter.Button(root, command=sendValue)
sendButton.config(image=send)
sendButton.grid(row=1,column=5)

root.title("Binary Clock GUI")
root.mainloop()
