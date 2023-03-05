#Battery Percentage Notifier app using Python

import psutil
from plyer import notification
import time

while(True):
    #getting the system battery
    battery=psutil.sensors_battery()
    percent=battery.percent

    print(f"{percent}& Battery remaining")

    time.sleep(60) #Notifies after 1 minute

    continue
# NB: Use CTRL + C to break out of the loop
