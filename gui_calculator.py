import curses
from random import randint

# Initialize the window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Initialize the snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)
win.addch(food[0], food[1], '*')

# Initialize the game variables
score = 0

# Game loop
while True:
    # Get the user input
    key = win.getch()
    if key == curses.KEY_LEFT:
        direction = 'left'
    elif key == curses.KEY_RIGHT:
        direction = 'right'
    elif key == curses.KEY_UP:
        direction = 'up'
    elif key == curses.KEY_DOWN:
        direction = 'down'
    else:
        direction = 'right'

    # Move the snake
    head = snake[0]
    if direction == 'left':
        new_head = (head[0], head[1] - 1)
    elif direction == 'right':
        new_head = (head[0], head[1] + 1)
    elif direction == 'up':
        new_head = (head[0] - 1, head[1])
    elif direction == 'down':
        new_head = (head[0] + 1, head[1])
    snake.insert(0, new_head)

    # Check if the snake has hit the wall
    if (new_head[0] == 0 or new_head[0] == 19 or
        new_head[1] == 0 or new_head[1] == 59):
        curses.endwin()
        quit()

    # Check if the snake has hit itself
    if new_head in snake[1:]:
        curses.endwin()
        quit()

    # Check if the snake has eaten the food
    if new_head == food:
        score += 1
        food = None
        while food is None:
            nf = (randint(1, 18), randint(1, 58))
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    # Display the snake and score
    win.addch(snake[0][0], snake[0][1], '#')
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.timeout(150 - (len(snake)//5 + len(snake)//10)%120)

# End the game
curses.endwin()
print("Final Score : ",score)
