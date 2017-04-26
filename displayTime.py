from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()
dTime = str(datetime.now()).split(" ")[1].split(".")[0]
print(dTime)
sense.show_message(dTime)
