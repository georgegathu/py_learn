"""
    === BUILD A CAR GAME ====
    when you type help
    1. start - to start the car : "Car started.. Ready to go!"
    2. stop - to stop the car : "Car stopped."
    3. quit - to exit the game
    else print: "i dont understand that"
"""
command = ""

while True:
    command = input("> ").lower
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
    Start - Start the car
    Stop -  Stop the car
    quit - Quit the game
        """)
    elif command == "quit":
        break
