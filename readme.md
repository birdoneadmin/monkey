# Monkey Programming Language

![GitHub release (with filter)](https://img.shields.io/github/v/release/:birdoneadmin/:monkey)

Monkey is a simple programming language designed for basic operations. It includes functions for printing, looping, string concatenation, arithmetic operations, conditional statements, random number generation, and banana operations.

# Functions

## Print Commands

- `oohoohahah(text)`: Prints the provided text. If the input is not a string, it converts it to a string before printing.
- `ooaa(text)`: A shorthand for the `oohoohahah` function.

## Banana

- `banana(action)`: Manipulates a variable `b`. If the action is "add", it increments `b` by 1. If the action is "reset", it sets `b` to 0.

## Loops

- `monkey(command, subcommand, times)`: Repeats a command a specified number of times. The command can be "ooaa" or "banana".

## Concatenation

- `double(text)`: Concatenates a string with itself. If the input is not a string, it converts it to a string before concatenation.

## Math

- `math(n1, func, n2)`: Performs basic arithmetic operations. The `func` parameter can be "add", "subtract", "multiply", or "divide".

## If-else

- `ifelse(value, condition, ifcmd, ifsub, elsecmd, elsesub)`: Performs different commands based on a condition and the value of `b`. The condition can be "=", ">", or "<".

## Random Number Generation

- `random(min, max)`: Returns a random integer between `min` and `max`.
- `randomrandom(min, max)`: Returns a random integer between two random values that are themselves between `min` and `max`.

## Comments

- `comment()`: Write a comment to annotate your code.

**Monkey is still in the very early stages of development, and more features are set to come.**

# Installation
To install Monkey, first install Python 3.9 or later.\
Then, create a folder for all your monkey code. Then, copy the `monkey.py` file and paste it into your folder.\
Start a Monkey file by creating a document and name it with the extension `.mky`.\
Add this code to the first line: `import monkey as m`.\
and add a `m.` prefix to every command.