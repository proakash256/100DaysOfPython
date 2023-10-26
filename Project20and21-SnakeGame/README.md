# Snake Game Documentation

## Introduction

The Snake Game is a classic arcade game where the player controls a snake that moves around the screen, eating food and growing longer. The objective is to avoid colliding with the walls or the snake's own body. The game ends when the snake collides with any of these obstacles. This Python program uses the turtle module to create the game's graphical interface.

## Modules Used

The following modules are used in this program:

- turtle: Used to create the game's graphics, handle user input, and control the movement of objects on the screen.
- time: Used to introduce a delay between each iteration of the game loop.
- food: A custom module that defines the Food class, responsible for creating and managing the food objects.
- scoreboard: A custom module that defines the ScoreBoard class, responsible for keeping track of and displaying the player's score.

## Game Initialization

The game is initialized by performing the following steps:

1. The required modules and classes are imported.
2. Constants such as font and alignment settings are defined.
3. The screen object is created using `Screen()` and configured with a title, background color, and size.
4. The `tracer()` method is called with a value of `0` to turn off animation updates for faster performance.
5. Instances of the Snake, Food, and ScoreBoard classes are created.
6. The `listen()` method is called on the screen object to enable key event handling.
7. Event handlers are registered for the arrow keys to control the snake's movement.
8. An event handler is registered for the space key to handle game over.

## Snake Class

The Snake class represents the snake object in the game. It has the following methods and attributes:

- `__init__`: The constructor method that initializes the snake's segments, creates the snake, and sets the initial head.
- `create_snake`: A method that creates the initial segments of the snake at the starting positions.
- `add_segment`: A method that adds a new segment to the snake's body.
- `extend_snake`: A method that adds a new segment to the snake's body when it eats food.
- `reset`: A method that resets the snake's segments, position, and direction to the starting state.
- `move`: A method that moves the snake forward by updating the positions of its segments.
- `up`, `down`, `left`, `right`: Methods that handle the snake's movement in different directions based on user input.

## Food Class

The Food class represents the food object in the game. It has the following methods and attributes:

- `__init__`: The constructor method that initializes the food's appearance and position.
- `refresh`: A method that moves the food to a random position within the game screen.

## ScoreBoard Class

The ScoreBoard class represents the score display in the game. It has the following methods and attributes:

- `__init__`: The constructor method that initializes the score and high score values, sets up the appearance of the score display, and loads the previous high score from a file.
- `update_score`: A method that updates the score display with the current score and high score.
- `reset`: A method that resets the score to zero and updates the high score if necessary.
- `increase_score`: A method that increments the score by one and updates the score display.

## Game Loop

The game loop is responsible for updating the game state and handling collisions. It performs the following steps:

1. The `update()` method of the screen object is called to refresh the screen.
2. A delay of 0.1 seconds is introduced using the `time.sleep()` method to control the speed of the game.
3. The `move()` method of the snake object is called to move the snake forward.
4. Collision detection is performed:
   - If the snake's head collides with the food, the score is increased, the food is refreshed, and the snake grows.
   - If the snake's head collides with the walls, the score is reset, and the snake is reset to its initial state.
   - If the snake's head collides with its own body, the score is reset, and the snake is reset to its initial state.
5. The game loop continues until the game is over, indicated by the `game_is_on` variable becoming `False`.
6. The program waits for a click on the screen to exit using `s.exitonclick()`.

## Conclusion

The Snake Game program provides a fun and interactive experience where players control a snake and try to achieve the highest score by eating food without colliding with any obstacles. The program demonstrates the use of the turtle module for creating graphics, handling user input, and managing game objects. It also utilizes concepts such as object-oriented programming, event handling, collision detection, and file I/O.