
#Print Function
print("Hello World!")

#Print with repeat
print("Hello World!\nHello World!\nHello World!")

#Combine Strings
print("Hello" + "Joao")
print("Hello" + " " + "Joao")

#Debuging exercise
#Fix the code below 👇

#print(Day 1 - String Manipulation")
#print("String Concatenation is done with the "+" sign.")
#  print('e.g. print("Hello " + "world")')
#print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#Input function
input("What is your name?")
print("Hello " + input("What is your name? "))

#Print number of characters in name
print("Your name has " + str(len(input("What is your name?"))) + " characters")

#Answer
print(len(input("What is your name? ")))


#Variables

name = input("What is your name? ")
print(name)

#Change variables value
name = "joao"
print(name)

name = "nina"
print(name)

#Functions inside variables
name = input("What is your name?")
length = len(name)
print(length)

#drop variables
del name
del length
#clear all
# %reset

#Exercise: switches de values stored in the variables a
# and b

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#variables name:

#can't use space: name user
#use underline: name_user
#can't use functions name

#-----Day 1 Project:------

#1. Create a greeting for your program.
name = input("What is your name? ")
print("Hello " + name + "!")

#2. Ask the user for the city that they grew up in.
city = input("Which city did you grew up, " + name + "?")

#3. Ask the user for the name of a pet.
pet = input("What is the name of your pet, " + name + "?")

#4. Combine the name of their city and pet and show them their band name.
print("Your band name should be: " + city + " " + pet + "!")

#5. Make sure the input cursor shows on a new line:

#Answer:
print("Welcome to the band generator!")
#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up?\n")
#3. Ask the user for the name of a pet.
pet = input("What is the name of a pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)