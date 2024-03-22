def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if front_is_clear()==True and right_is_clear()==True:
        turn_right()
        move()
    elif wall_in_front()==True and right_is_clear()!=True:
        turn_left()
    elif front_is_clear()==True and right_is_clear()==False:
        move()
    elif wall_in_front()==True and right_is_clear()==True:
        turn_right()
        move()  
    else:
        move()

while at_goal()!=True:
    jump()