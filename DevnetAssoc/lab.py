# Initialize empty lists to store routers and switches
routers = []
switches = []

# List of initial devices
devices = ["RT1", "RT2", "RT3", "SW1", "SW2", "SW3"]

# Add additional devices to the list
devices = devices + ["RT4", "SW4"]

# Iterate over the list of devices and categorize them
for device in devices:
    # If the device name contains 'R', it is a router
    if "R" in device:
        routers.append(device)
    # Otherwise, it is a switch
    else:
        switches.append(device)

# Print the list of routers
print("Routers:", routers)

# Print the list of switches
print("Switches:", switches)
