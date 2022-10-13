#conditional statements
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride!")
else:
    print("You can't ride!")

# we can include >= or <=, yet == or !=

#Odd or Even exercise
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("Your number is even!")
else:
    print("your number is odd")


#ifelse inside ifelse and elif conditions

height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride!")
    age = int(input("what is your age? "))
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("Please pay 12")
else:
    print("You can't ride!")


#exercise BMI calculator
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / height ** 2
bmi_round = "{:.2f}".format(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi_round}, you're underwight")
elif bmi < 25:
    print(f"Your bmi is {bmi_round}, you're normal")
elif bmi < 30:
    print(f"Your bmi is {bmi_round}, you're overwight")
elif bmi < 35:
    print(f"Your bmi is {bmi_round}, you're obese")
else:
    print(f"Your bmi is {bmi_round}, you're diyng")

#exercise leap year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year.")
        else:
            print("not leap year.")
    else:
        print("leap year")
else:
    print("not leap year.")

#multiple if

height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken by aditional $3? Y or N")
    if wants_photo == "Y":
        #add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("You can't ride!")

#Exercise: Pizza Delivery
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"You choose a {size} pizza, with {add_pepperoni} and {extra_cheese}, your final bill is: ${bill}")

#Logical Operators
# and, or, not
# and only need one condition to be true
# or need both
# not reserve the condition

height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("have a free ride!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken by aditional $3? Y or N")
    if wants_photo == "Y":
        #add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("You can't ride!")


#Exercise: Love calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true)) + int(str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, dont work")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, alright")
else:
    print(f"Your love score is {love_score}")


# Adventure game
print('''Game''')
print("Welcome!")
input('You\'re at crossroad, "left" or "right"?')


