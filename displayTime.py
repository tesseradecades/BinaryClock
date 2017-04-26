from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
#dTime = str(datetime.now()).split(" ")[1].split(".")[0]
#print(dTime)
#sense.show_message(dTime)

blue = (0, 0, 255)

#hh 10s place
sense.set_pixel(0,7,blue)
sense.set_pixel(0,6,blue)

#hh 1s place
sense.set_pixel(1,7,blue)
sense.set_pixel(1,6,blue)
sense.set_pixel(1,5,blue)
sense.set_pixel(1,4,blue)

#mm 10s place
sense.set_pixel(3,7,blue)
sense.set_pixel(3,6,blue)
sense.set_pixel(3,5,blue)

#mm 1s place
sense.set_pixel(4,7,blue)
sense.set_pixel(4,6,blue)
sense.set_pixel(4,5,blue)
sense.set_pixel(4,4,blue)

#ss 10s place
sense.set_pixel(6,7,blue)
sense.set_pixel(6,6,blue)
sense.set_pixel(6,5,blue)

#ss 1s place
sense.set_pixel(7,7,blue)
sense.set_pixel(7,6,blue)
sense.set_pixel(7,5,blue)
sense.set_pixel(7,4,blue)

#sense.clear()
