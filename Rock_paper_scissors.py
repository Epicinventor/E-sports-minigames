### importing random ###

import random


### Rock paper scissors battle introduction

print("Welcome to Rock-Paper-Scissors\n")
print("Choose your material\n")


### Choosing the Material ###
print("For Rock type letter 'r' \n")
print("For Rock ")
option = input("Choose > ").lower()

### bot function ###
list = [1,2,3]


print(random.choice(list))

print()
print()
print()
print()

### Code for Bot and Player using same ###
if list == 1 and option == "r":
    print("Draw!")

elif list == 2 and option == "p":
    print("Draw!")

elif list == 3 and option == "s":
    print("Draw!")

### Code for Bot using Rock ###
elif list == 1 and option == "p":
    print("You Win!")

elif list == 1 and option == "s":
    print("Bot Wins!")

### Code for Both using Paper ###
elif list == 2 and option == "r":
    print("Bot Wins!")

elif list == 2 and option == "s":
    print("You Win!")

### Code for Bot using Scissors ###
elif list == 3 and option == "r":
    print("You Win!")

elif list == 3 and option == "p":
    print("Bot Wins!")
