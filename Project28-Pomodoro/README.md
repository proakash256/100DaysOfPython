# Pomodoro

## Introduction

The Pomodoro Clock is a Python program that implements a timer based on the Pomodoro Technique. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This technique aims to improve productivity and focus by dividing work into manageable chunks.

## Constants

The program uses the following constants:

- `PINK`: A string representing the color pink used in the user interface.
- `RED`: A string representing the color red used in the user interface.
- `GREEN`: A string representing the color green used in the user interface.
- `YELLOW`: A string representing the color yellow used in the user interface.
- `FONT_NAME`: A string representing the font name used in the user interface.
- `WORK_MIN`: An integer representing the duration of a work interval in minutes (default: 25 minutes).
- `SHORT_BREAK_MIN`: An integer representing the duration of a short break interval in minutes (default: 5 minutes).
- `LONG_BREAK_MIN`: An integer representing the duration of a long break interval in minutes (default: 20 minutes).

## Timer Reset

The program provides a function `reset_timer()` to reset the timer. When called, it cancels the current timer, resets the timer text to "00:00", resets the title label text to "Timer" with the color set to green, clears the check label, and resets the `reps` counter to 0.

## Timer Mechanism

The program provides a function `start_timer()` to handle the timer mechanism. When called, it increments the `reps` counter by 1. If the `reps` counter is divisible by 8, indicating the completion of a full work cycle, the title label is set to "Break" with the color set to red, and the `LONG_BREAK_MIN` duration is passed to the `count_timer()` function. If the `reps` counter is divisible by 2, indicating the completion of a work interval, the title label is set to "Break" with the color set to pink, and the `SHORT_BREAK_MIN` duration is passed to the `count_timer()` function. Otherwise, the title label is set to "Work" with the color set to green, and the `WORK_MIN` duration is passed to the `count_timer()` function.

## Countdown Mechanism

The program provides a function `count_timer(seconds)` to handle the countdown mechanism. It takes the number of seconds as input and updates the timer text on the canvas accordingly. The function uses recursion to decrement the number of seconds by 1 every second using the `after()` method of the Tkinter window. When the countdown reaches zero, the `start_timer()` function is called to initiate the next interval, and the check label is updated with checkmarks corresponding to the number of completed work intervals.

## User Interface Setup

The program creates a graphical user interface (GUI) using the Tkinter library. The GUI consists of a main window with a title label, a canvas displaying a tomato image, a timer text, start and reset buttons, and a check label. The timer text, start button, reset button, and check label are all part of a grid layout within the main window.

The GUI elements are styled with appropriate fonts, colors, and sizes. The canvas displays a tomato image, and the timer text initially shows "00:00". The start button is connected to the `start_timer()` function, and the reset button is connected to the `reset_timer()` function.

## Conclusion

The Pomodoro Clock program provides a simple and user-friendly interface for implementing the Pomodoro Technique. By setting the work, short break, and long break durations, users can effectively manage their time and improve productivity. The program's graphical user interface allows for easy interaction and provides visual feedback on the progress of work intervals and breaks.

This documentation serves as a reference for understanding the functionality and structure of the Pomodoro Clock program.