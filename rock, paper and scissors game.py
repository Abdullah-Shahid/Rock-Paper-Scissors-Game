import random

# Computer choice
computer = random.choice([-1,0,1])

# Game title
print("\t\t\tRock, Paper and Scissor Game")

# User choice
you_string = input("Enter your Choice (rock/paper/scissor): ")

# Dictionary
youDict = {'rock':1, 'paper':-1, 'scissor':0}

# Reverse Dictionary
reverse_dict = {1:'rock',-1:'paper',0:'scissor'}

# Convarting user input(rock/paper/scissor) into integers(-1, 0, 1)
you = youDict[you_string.lower()]

# Showing both choices
print(f"You chose {reverse_dict[you].capitalize()}")
print(f"Computer chose {reverse_dict[computer].capitalize()}")

# Using nested if elif(5) else statements
if(computer==you):
    print("Its a DRAW.")
else:
    if(computer==-1 and you==0):
        print("You WIN!")
    elif(computer==-1 and you==1):
        print("You LOSE!")
    elif(computer==1 and you==-1):
        print("You WIN!")
    elif(computer==1 and you==0):
        print("You LOSE!")
    elif(computer==0 and you==-1):
        print("You LOSE!")
    elif(computer==0 and you==1):
        print("You WIN!")
    else:
        print("Something went WRONG.")