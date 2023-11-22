#########################################
###### MONKEY PROGRAMMING LANGUAGE ######
############ Version 0.2.0 ##############
#########################################

# ----------------------------------------------------- #

# Initialize
b = 0
pext = 0
pextext = 0
import random

# ----------------------------------------------------- #

# Block Outside Commands
def mkyprint(*args, **kwargs):
    if allow_print:
        print(*args, **kwargs)
    else:
        raise ValueError("Error 6: Invalid Function. Use ooaa() or oohoohahah() instead.")

print = mkyprint

def getb():
    return b

# ----------------------------------------------------- #

# Print Extension
def EnablePrintExt():
    global pext
    pext = 1

def DisablePrintExt():
    global pext
    pext = 0

# ----------------------------------------------------- #

# Print Commands
allow_print = False

def oohoohahah(text):
    global allow_print
    global pext
    allow_print = True
    if pext == 1:
        print(str(text))
    else:
        print("Ooh Ooh Ah Ah")
        if text != "":
            ooaaa("Error 8: Enable Print Exten first to output text.")
    allow_print = False

def ooaaa(text):
    oohoohahah(text)

def ooaaa(text):
    global allow_print
    global pextext
    allow_print = True
    if pextext == 1:
        print(str(text))
    else:
        raise ValueError("Error 7: Invalid Function. Use oohoohahah() or ooaa() instead.")
    allow_print = False

# ----------------------------------------------------- #

# Bananas
def banana(action):
    global b
    if action == "add":
        b += 1
    elif action == "reset":
        b = 0
    else:
        ooaaa("Error 1: Invalid Banana Function")

# ----------------------------------------------------- #

# Loops
def monkey(command, subcommand, times):
    if command == "ooaa":
        for i in range(times):
            ooaaa(subcommand)
    elif command == "banana":
        for i in range(times):
            banana(subcommand)
    else:
        ooaaa("Error 2: Invalid Monkey Loop Function Provided")

# ----------------------------------------------------- #

# Concatenation
def double(text):
    if isinstance(text, str):
        return text + text
    else:
        return str(text) + str(text)

# ----------------------------------------------------- #

# Math
def math(n1, func, n2):
    if func == "add" or func == "+":
        return n1 + n2
    elif func == "subtract" or func == "-":
        return n1 - n2
    elif func == "multiply" or func == "*":
        return n1 * n2
    elif func == "divide" or func == "/":
        return n1 / n2
    else:
        ooaaa("Error 3: Invalid Math Function")

# ----------------------------------------------------- #

# If-else
def ifelse(value, condition, ifcmd, ifsub, elsecmd, elsesub):
    global b
    if condition == "=" or condition == "==" or condition == "equal":
        if b == value:
            if ifcmd == "ooaa":
                ooaaa(ifsub)
            elif ifcmd == "banana":
                banana(ifsub)
            else:
                ooaaa("Error 4: Invalid Ifelse Function Provided")
        else:
            if elsecmd == "ooaa":
                ooaaa(elsesub)
            elif elsecmd == "banana":
                banana(elsesub)
            else:
                ooaaa("Error 4: Invalid Ifelse Function Provided")
    elif (
        condition == ">"
        or condition == "greater"
        or condition == "morethan"
        or condition == "more than"
    ):
        if b > value:
            if ifcmd == "ooaa":
                ooaaa(ifsub)
            elif ifcmd == "banana":
                banana(ifsub)
            else:
                ooaaa("Error 4: Invalid Ifelse Function Provided")
        else:
            if elsecmd == "ooaa":
                ooaaa(elsesub)
            elif elsecmd == "banana":
                banana(elsesub)
            else:
                ooaaa("Error 4: Invalid Ifelse Function Provided")
    elif (
        condition == "<"
        or condition == "less"
        or condition == "lessthan"
        or condition == "less than"
    ):
        if b < value:
            if ifcmd == "ooaa":
                ooaaa(ifsub)
            elif ifcmd == "banana":
                banana(ifsub)
            else:
                ooaaa("Error 4: Invalid Ifelse Function Provided")
        else:
            if elsecmd == "ooaa":
                ooaaa(elsesub)
            elif elsecmd == "banana":
                banana(elsesub)
            else:
                ooaaa("Error 4: Invalid Ifelse Function Provided")
    else:
        ooaaa("Error 5: Invalid Ifelse Condition Provided")

# ----------------------------------------------------- #

# Random Number Generation
def random(min, max):
    return random.randint(min, max)

def randomrandom(min, max):
    return random.randint(random.randint(min, max), random.randint(min, max))

# ----------------------------------------------------- #

# Comments
def comment():
    pass

# ----------------------------------------------------- #

# Test Function
def whn():
    ooaaa("da")