# Program to show your computer CPU usage
import psutil

while True:
    print("Your CPU Usage is: " + str(psutil.cpu_percent(1))) # Updates the CPU usage after every 1 second
    print("Your RAM Usage is: " + str(psutil.virtual_memory()[3]/1000000000)) # This prints the amount of RAM usage

# NB: Use windows command = "Control + C" to escape the program's loop.