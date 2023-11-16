# Monkey Programming Language Documentation

Monkey is a simple programming language designed for basic operations. It includes functions for printing, looping, string concatenation, arithmetic operations, conditional statements, random number generation, and a unique 'banana' operation.

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