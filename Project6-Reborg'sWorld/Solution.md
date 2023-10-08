# Solution

The secret is to have Reeborg follow along the right edge of the maze,  
turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```
The above might run into an infinite loop, if it's all three sides are clear.  
So first we need to get reborg near a wall. The first while loop helps to get reborg near a wall,  
after which the previous logic will work well.

### Updated Solution:
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
    
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```