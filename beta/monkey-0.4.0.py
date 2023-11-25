#########################################
###### MONKEY PROGRAMMING LANGUAGE ######
############ Version 0.4.0 ##############
#########################################

# ----------------------------------------------------- #

# Initialize

b = 0
pext = 0
pextext = 0
printok = False

import random
import sys
from time import sleep

version = "0.4.0"

# ----------------------------------------------------- #

# Message

print("Monkey "+version+"\n")
# ----------------------------------------------------- #

# Modifications
    
def getb():
    return b

# ----------------------------------------------------- #

# PrintExten  Extension

def EnablePrintExt():
    global pext
    pext = 1

def DisablePrintExt():
    global pext
    pext = 0

def PrintExten():
    print("")
    sleep(0.5)
    print(".----. .----. -.- |\\   | --.--")
    print("|    | |    |  |  | \\  |   |  ")
    print("|----. |----.  |  |  \\ |   |  ")
    print("|      |   \\   |  |   \\|   |  ")
    print("|      |    \\ _._ |    |   |  ")
    print("")
    sleep(0.2)
    print("|---- \\   / --.-- |---- |\\   |")
    print("|      \\ /    |   |     | \\  |")
    print("|----   X     |   |---- |  \\ |")
    print("|      / \\    |   |     |   \\|")
    print("|---- /   \\   |   |---- |    |")
    print("")
    sleep(0.2)
    print("[!] PrintExten will soon move to its own downloadable extension, inside the Monkey repo.")
    print("")
    sleep(0.2)
    print("PrintExten")
    print("Official Print Extension for Monkey 0.3.0 and up")
    print("")
    print("Choose what you want to do:")
    print("1. Enable PrintExten")
    print("2. Disable PrintExten")
    print("3. Leave a Review")
    print("4. About")
    print("5. Exit")
    print("")
    pxchoice = input("... ")
    
    if pxchoice == "1":
        EnablePrintExt()
    elif pxchoice == "2":
        DisablePrintExt()
    elif pxchoice == "3":
        pxreview = input("\nType your review... (No more than 128 characters)\n... ")
        if len(pxreview) > 128:
            print("\nPxError 1: Review too long! Not saved.")
            print("")
            for i in range(3):
                print("Going to Home Screen in "+str(3-i)+" second(s)...")
                sleep(1)
            PrintExt()
        elif pxreview == "":
            print("\nRating Left Blank. Going Back to Home Screen")
            sleep(1)
            PrintExt()
        else:
            pxrating = input("\nThank you. Please rate us!\n_/5 (0-5) ... ")
            print(pxrating+"/5 Thank you!") if (isinstance(pxrating, int) and pxrating >= 0 and pxrating <= 5) else (print("\nPxError 2: Invalid Rating! Not saved."))
            print("")
            for i in range(3):
                print("Going to Home Screen in "+str(3-i)+" second(s)...")
                sleep(1)
            PrintExt()
    elif pxchoice == "4":
        print("Coming Soon")
    elif pxchoice == "5":
        pxconf = input("Confirm Exit? (y/n)")
        if pxconf == "y":
            return
        else:
            PrintExten()
    else:
        print("Invalid C")
            
def PrintExt():
    PrintExten()
    
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
            pextext = 1
            sleep(0.5)
            print("Error 8: Enable PrintExten first to output text.")
            pextext = 0
    allow_print = False

def ooaa(text):
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
    global b,pextext
    if action == "add":
        b += 1
    elif action == "reset":
        b = 0
    else:
        pextext = 1
        print("Error 1: Invalid Banana Function")
        pextext = 0

# ----------------------------------------------------- #

# Loops

def mkloop(command, subcommand, times):
    global pextext
    if command == "ooaa":
        for i in range(times):
            ooaa(subcommand)
    elif command == "banana":
        for i in range(times):
            banana(subcommand)
    else:
        pextext = 1
        ooaa("Error 2: Invalid Monkey Loop Function Provided")
        pextext = 0

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
    global pextext
    if func == "add" or func == "+":
        return n1 + n2
    elif func == "subtract" or func == "-":
        return n1 - n2
    elif func == "multiply" or func == "*":
        return n1 * n2
    elif func == "divide" or func == "/":
        return n1 / n2
    else:
        pextext = 1
        ooaa("Error 3: Invalid Math Function")
        pextext = 0

# ----------------------------------------------------- #

# If-else

def ifelse(value, condition, ifcmd, ifsub, elsecmd, elsesub):
    global b,pextext
    if condition == "=" or condition == "==" or condition == "equal":
        if b == value:
            if ifcmd == "ooaa":
                ooaa(ifsub)
            elif ifcmd == "banana":
                banana(ifsub)
            else:
                pextext=1; ooaa("Error 4: Invalid Ifelse Function Provided"); pextext=0
        else:
            if elsecmd == "ooaa":
                ooaa(elsesub)
            elif elsecmd == "banana":
                banana(elsesub)
            else:
                pextext=1; ooaa("Error 4: Invalid Ifelse Function Provided"); pextext=0
    elif (
        condition == ">"
        or condition == "greater"
        or condition == "morethan"
        or condition == "more than"
    ):
        if b > value:
            if ifcmd == "ooaa":
                ooaa(ifsub)
            elif ifcmd == "banana":
                banana(ifsub)
            else:
                pextext=1; ooaa("Error 4: Invalid Ifelse Function Provided"); pextext=0
        else:
            if elsecmd == "ooaa":
                ooaa(elsesub)
            elif elsecmd == "banana":
                banana(elsesub)
            else:
                pextext=1; ooaa("Error 4: Invalid Ifelse Function Provided"); pextext=0
    elif (
        condition == "<"
        or condition == "less"
        or condition == "lessthan"
        or condition == "less than"
    ):
        if b < value:
            if ifcmd == "ooaa":
                ooaa(ifsub)
            elif ifcmd == "banana":
                banana(ifsub)
            else:
                pextext=1; ooaa("Error 4: Invalid Ifelse Function Provided"); pextext=0
        else:
            if elsecmd == "ooaa":
                ooaa(elsesub)
            elif elsecmd == "banana":
                banana(elsesub)
            else:
                pextext=1; ooaa("Error 4: Invalid Ifelse Function Provided"); pextext=0
    else:
        ooaa("Error 5: Invalid Ifelse Condition Provided")

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

# Who Test Function

def who():
    global pextext
    pextext = 1
    ooaa("da")
    pextext = 0

def whn(text):
    global pextext
    pextext = 1
    ooaa("da"+capitalize(text))
    pextext = 0

# ----------------------------------------------------- #

# True/False

def truefalse(n1, func, n2):
    if func == "=":
        if (n1 == "1" and n2 == "0") or (n2 == "0" and n1 == "1"):
            return "Maybe"
        else:
            return n1 == n2
            
    if func == ">": return n1 > n2
    if func == "<": return n1 < n2
    if func == "!=" or func == "≠": return n1 != n2
    if func == "!>" or func == "<=": return n1 <= n2a
    if func == "!<" or func == ">=": return n1 >= n2
    if func == "!!=": return "Maybe"
    if func == "!!!=": return False
    
# ----------------------------------------------------- #

# Sys Extension

def sys():
    print("")
    print("Sys Extension")
    sleep(0.2)
    print("")
    print("Official System Extension for Monkey 0.4.0 and up")
    print("")
    print("Select a function")
    print("1. Read Important Updates")
    print("2. Read Other Articles")
    print("3. Install Extensions")
    print("4. Try Monkey Beta")
    print("5. Exit")
    print("")
    syschoice = input("... ")
    print("")
    sleep(0.5)
    if syschoice == "1":
        print("[!] IMPORTANT UPDATE\nMonkey extensions will be moved to a seperate version instead of being in the file itself. It will be downloadable through the Monkey repo and available for free.")
        input("\nPress enter to go to Home Screen.")
        print("\nGoing to Home Screen in 3 seconds...\n")
        sleep(3);sys()
    if syschoice == "2":
        print("No other articles at the moment. Going back to Home Screen in 3 seconds...\n")
        sleep(3);sys()
    if syschoice == "3":
        print("Extensions are not installable through Sys at the moment. Going back to Home Screen in 3 seconds...\n")
        sleep(3);sys()
    if syschoice == "4":
        print("Monkey Beta Testing is not open at the moment. Going back to Home Screen in 3 seconds...\n")
        sleep(3);sys()
    if syschoice == "5":
        sysexit = ("Are you sure you want to exit? (y/n)")
        if sysexit == "y":
            return
        else:
            sys()
            
# ----------------------------------------------------- #
