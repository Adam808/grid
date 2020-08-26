import random

#make grid
grid = [[0 for i in range(10)] for i in range(10)]

#set starting position
player = [random.randrange(10), random.randrange(10)]
grid[player[0]][player[1]] = 1

#set target
target = (random.randrange(10), random.randrange(10))
grid[target[0]][target[1]] = 8
while list(target) == player:
    target = (random.randrange(10), random.randrange(10))
    grid[target[0]][target[1]] = 8

for i in grid:
    print(i)

def move_up():
    global grid, player
    if player[0] > 0:
        grid[player[0]][player[1]] = 0
        player[0] -= 1
        grid[player[0]][player[1]] = 1
        for i in grid:
            print(i)
    else:
        print("Can't move up")

def move_right():
    global grid, player
    if player[1] < 9:
        grid[player[0]][player[1]] = 0
        player[1] += 1
        grid[player[0]][player[1]] = 1
        for i in grid:
            print(i)
    else:
        print("Can't move right")

def move_left():
    global grid, player
    if player[1] > 0:
        grid[player[0]][player[1]] = 0
        player[1] -= 1
        grid[player[0]][player[1]] = 1
        for i in grid:
            print(i)
    else:
        print("Can't move up")

def move_down():
    global grid, player
    if player[0] < 9:
        grid[player[0]][player[1]] = 0
        player[0] += 1
        grid[player[0]][player[1]] = 1
        for i in grid:
            print(i)
    else:
        print("Can't move down")

def move():
    global grid, player
    direction = input("Left, Right, Up, or Down? ")
    if direction == 'l':
        move_left()
        if list(target) == player:
            print("You reached the target!")
    elif direction == 'r':
        move_right()
        if list(target) == player:
            print("You reached the target!")
    elif direction == 'u':
        move_up()
        if list(target) == player:
            print("You reached the target!")
    elif direction == 'd':
        move_down()
        if list(target) == player:
            print("You reached the target!")
    else:
        print("Enter a valid direction.")
        move()

while list(target) != player:
    move()
