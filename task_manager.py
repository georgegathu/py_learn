# Program to show your computer CPU usage
import psutil

while True:
    print("Your CPU Usage is: " + str(psutil.cpu_percent(1))) # Updates the CPU usage after every 1 second

# NB: Use windows command = "Control + C" to escape the program's loop.