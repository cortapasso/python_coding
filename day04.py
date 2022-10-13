#Randomisation and Lists
from cmath import pi
import random
import day04_module

random_integer = random.randint(1, 10)
print(random_integer)

#import module
print(day04_module.pi)

#random float
random_float = random.random()
print(random_float)

#any random float, multiply
randomFloat = random.random() * 5
print(randomFloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")

#exercise heads or tails
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

coin = random.randint(0, 1)
if coin == 1:
    print("Heads")
else:
    print("Tails.")

# PYTHON LISTS !!!!!!!!!!!
# fruits = ["banana", "apple", "orange"] #0, 1, 2

fruits = ["banana", "apple", "orange"]
fruits[0]
fruits[-1]
fruits[1] = "banananana"
print(fruits)

#add single item to the end of the list
fruits.append("grapes")
print(fruits)
#add multiple itens
fruits.extend(["strawberry", "blueberries", "pineaple"])
print(fruits)

#exercise: split the bill
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_names = len(names)
random_name = random.randint(0, number_of_names - 1)
print(f"{names[random_name]} is going to buy the meal today!")

#Nested lists

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])

#Exeercise Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#Project: Rock, Paper, Scissors
game = ["Rock", "Paper", "Scissors"]
user_choice = int(input("0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"You chose {game[user_choice]}")

    computer_choice = random.randint(0,2)
    print(f"Computer chose {game[computer_choice]}")


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
