# Pong Game

## Introduction

The Pong Game is a classic arcade game where two players control paddles on opposite sides of the screen. The objective is to hit the ball with the paddles and prevent it from reaching the edges of the screen. Players earn points when the opponent fails to return the ball. This Python program uses the turtle module to create the game's graphical interface.

## Modules Used

The following modules and classes are used in this program:

- `turtle`: Used to create the game's graphics, handle user input, and control the movement of objects on the screen.
- `paddle`: A custom module that defines the `Paddle` class, responsible for creating and controlling the paddles.
- `ball`: A custom module that defines the `Ball` class, responsible for creating and controlling the ball.
- `scoreboard`: A custom module that defines the `ScoreBoard` class, responsible for keeping track of and displaying the scores.
- `time`: Used to introduce a delay between each iteration of the game loop.

## Game Initialization

The game is initialized by performing the following steps:

1. The required modules and classes are imported.
2. Constants such as paddle positions, score positions, alignment, and font settings are defined.
3. The screen object is created using `Screen()` and configured with a title, background color, and size.
4. The `tracer()` method is called with a value of `0` to turn off animation updates for faster performance.
5. Instances of the `Paddle`, `Ball`, and `ScoreBoard` classes are created.
6. Event handlers are registered for the arrow keys to control the paddles.
7. An event handler is registered for the space key to handle game over.
8. The game loop is started.

## `Paddle` Class

The `Paddle` class represents the paddles in the game. It has the following methods and attributes:

- `__init__`: The constructor method that initializes the paddle's appearance and position.
- `up`: A method that moves the paddle up.
- `down`: A method that moves the paddle down.

## `Ball` Class

The `Ball` class represents the ball in the game. It has the following methods and attributes:

- `__init__`: The constructor method that initializes the ball's appearance, position, and movement properties.
- `move`: A method that updates the ball's position.
- `bounce_y`: A method that changes the ball's vertical direction when it collides with the top or bottom wall.
- `bounce_x`: A method that changes the ball's horizontal direction when it collides with a paddle.
- `restart`: A method that resets the ball's position and speed when it goes out of bounds.

## `ScoreBoard` Class

The `ScoreBoard` class represents the score display in the game. It has the following methods and attributes:

- `__init__`: The constructor method that initializes the score value, appearance, and position.
- `update_score`: A method that updates the score display with the current score.
- `increase_score`: A method that increments the score by one and updates the score display.

## Game Loop

The game loop is responsible for updating the game state and handling collisions. It performs the following steps:

1. A delay of `ball.move_speed` seconds is introduced using the `time.sleep()` method to control the speed of the game.
2. The `update()` method of the screen object is called to refresh the screen.
3. The `move()` method of the ball object is called to update the ball's position.
4. Collision detection is performed:
   - If the ball collides with the top or bottom wall, its vertical direction is changed using the `bounce_y()` method.
   - If the ball collides with a paddle, its horizontal direction is changed using the `bounce_x()` method.
   - If the ball goes out of bounds on the right or left side, the corresponding player's score is increased, and the ball is reset using the `restart()` method.
5. The game loop continues until the game is over, indicated by the `game_is_on` variable becoming `False`.
6. The program waits for a click on the screen to exit using `s.exitonclick()`.

## Game Over

The `game_over()` function is called when the game is over. It displays the "Game Over" message in the center of the screen using a turtle object.

## Conclusion

The Pong Game program provides a classic gaming experience where players control paddles to hit the ball and earn points. The program demonstrates the use of the turtle module for creating graphics, handling user input, and managing game objects. It also utilizes concepts such as object-oriented programming, event handling, collision detection, and game loop.