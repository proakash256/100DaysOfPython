# Etch A Sketch

**Introduction:**

The Etch-A-Sketch program is a Python program that simulates the functionality of the classic Etch-A-Sketch toy. It utilizes the turtle module to create a drawing interface and allows the user to draw by controlling the turtle using keyboard inputs.

**Logic:**

The program uses the turtle module to create a turtle object named `tim` and a screen object named `s`. It sets up keyboard listeners to respond to specific keys and execute corresponding functions for moving the turtle, turning it, and clearing the drawing.

**Functionality:**

The program provides the following functionality:

1. Moving Forward: Pressing the "W" key moves the turtle forward by 10 units.

2. Moving Backward: Pressing the "S" key moves the turtle backward by 10 units.

3. Turning Left: Pressing the "A" key turns the turtle left by 10 degrees.

4. Turning Right: Pressing the "D" key turns the turtle right by 10 degrees.

5. Clearing the Drawing: Pressing the "C" key clears the drawing by resetting the turtle's position, clearing the screen, and putting the pen down again.

**Python Code:**

Here's a breakdown of the Python code:

1. The required modules, `Turtle` and `Screen`, are imported from the turtle module.

2. A turtle object named `tim` is created using `Turtle()`.

3. A screen object named `s` is created using `Screen()`.

4. The program sets up keyboard listeners using the `listen()` method of the screen object to listen for keyboard inputs.

5. Functions are defined for each movement and clearing action: `move_forward()`, `move_backward()`, `turn_left()`, `turn_right()`, and `clear()`.

6. The `onkey()` method of the screen object is used to associate each function with a specific key press event. For example, `s.onkey(move_forward, "w")` associates the `move_forward()` function with the "W" key press event.

7. The program waits for the user to click the screen to exit with `s.exitonclick()`.

**Functions and Python Concepts:**

The code demonstrates the use of the turtle module for creating a turtle object, controlling its movements, and responding to keyboard inputs using the screen object. It also utilizes Python concepts such as importing modules, defining functions, conditional statements, and event handling.

Overall, the Etch-A-Sketch program provides a simple and interactive way to draw using the turtle module. Users can control the turtle's movements and create drawings by pressing specific keys on the keyboard, emulating the experience of using an Etch-A-Sketch toy.