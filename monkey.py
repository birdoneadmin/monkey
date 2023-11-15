# MONKEY PROGRAMMING LANGUAGE
# Version 0.1.0

# Initialize
b = 0

# Print Commands
def oohoohahah(text):
    if isinstance(text, str):
        print(text)
    else:
        print(str(text))

def ooaa(text):
    oohoohahah(text)
  
def monkey(text):
    ooaa("Danunai " + text)

# Bananas
def banana(action):
    global b
    if action == "add":
        b += 1
    elif action == "reset":
        b = 0
    else:
        ooaa("Error 1: Invalid Banana Function")

# Loops
