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
def monkey(command, subcommand, times):
  if command == "ooaa":
    for i in range(times):
      ooaa(subcommand)
  elif command == "banana":
    for i in range(times):
      banana(subcommand)
  else:
    ooaa("Error 2: Invalid Monkey Function Provided")

# Concatenation
def double(text):
  if isinstance(text, str):
    return text + text
  else:
    return str(text) + str(text)

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
    ooaa("Error 3: Invalid Math Function")

# If-else
def ifelse(value, condition, ifcmd, ifsub, elsecmd, elsesub):
  global b
  if condition == "=" or condition == "==" or condition == "equal":
    if b == value:
      if ifcmd == "ooaa":
        ooaa(ifsub)
      elif ifcmd == "banana":
        banana(ifsub)
      else:
        ooaa("Error 4: Invalid Ifelse Function Provided")
    else:
      if elsecmd == "ooaa":
        ooaa(elsesub)
      elif elsecmd == "banana":
        banana(elsesub)
      else:
        ooaa("Error 4: Invalid Ifelse Function Provided")
  elif condition == ">" or condition == "greater" or condition == "morethan" or condition == "more than":
    if b > value:
      if ifcmd == "ooaa":
        ooaa(ifsub)
      elif ifcmd == "banana":
        banana(ifsub)
      else:
        ooaa("Error 4: Invalid Ifelse Function Provided")
    else:
      if elsecmd == "ooaa":
        ooaa(elsesub)
      elif elsecmd == "banana":
        banana(elsesub)
      else:
        ooaa("Error 4: Invalid Ifelse Function Provided")
  elif condition == "<" or condition == "less" or condition == "lessthan" or condition == "less than":
    if b < value:
      if ifcmd == "ooaa":
        ooaa(ifsub)
      elif ifcmd == "banana":
        banana(ifsub)
      else:
        ooaa("Error 4: Invalid Ifelse Function Provided")
    else:
      if elsecmd == "ooaa":
        ooaa(elsesub)
      elif elsecmd == "banana":
        banana(elsesub)
      else:
        ooaa("Error 4: Invalid Ifelse Function Provided")
  else:
    ooaa("Error 5: Invalid Ifelse Condition Provided")                              
