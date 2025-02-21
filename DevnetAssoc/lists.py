# List indexing starts at 0 for the first element. Negative indices count from the end (-1 is the last item).
# Accessing the first item (index 0)
print(hostnames[0])     # 'R1'

# Accessing the last item with negative indexing
print(hostnames[-1])    # 'S2'

# Replacing an item
hostnames[0] = "RTR1"
print(hostnames)        # ['RTR1', 'R2', 'R3', 'S1', 'S2']

# Removing an item using del
del hostnames[3]
print(hostnames)        # ['RTR1', 'R2', 'R3', 'S2']