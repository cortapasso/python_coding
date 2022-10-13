#Data types

#String
"Hello"[0] #Returns H
"Hello"[1] #Returns e

print("123" + "345")

#Integer

print(123 + 345)

123_456_789

#Float

print(3.14159)

#Boolean

True
False


#Lesson 20
num_char = len(input("What is your name?"))
#print("your name has " + num_char + " characters.")

print(type(num_char))

#convertion

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")

a = 123
print(type(a))

a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

#Exercise
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))

#mathematical operations

3 + 5
7 - 4
3 * 2
print(6 / 3)
2 ** 2 #power

#PEMDASLR
()
**
* /
+ -

print(3 * 3 + 3 / 3 - 3) # 7
print(3 * (3 + 3) / 3 - 3) # 3

#Exercise
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

#round numbers
print(round(8/3, 2)) #round 2 digits

#float division
print(8 // 3)

result = 4 / 2
result /= 2

print(result)

#use scores a point
score = 0
score += 1
print(score)

#printing variables
print("your score is: " + score) #error
print("your score is: " + str(score)) #not the best way

score = 0
height = 1.8
isWinning = True

#f-string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#exercise

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)
years = 60 - age
day = years * 365
week = years * 52
month = years * 12

print(f"You have {day} days, {week} weeks, and {month} months left.")


#tip calculator

#inputs
total = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? "))
people = int(input("How many poeple to split the bill? "))

pay = (total * (1 + (tip/100))) / people
pay_round = "{:.2f}".format(pay) #format to show zero

print(f"Each person should pay: ${pay_round}")