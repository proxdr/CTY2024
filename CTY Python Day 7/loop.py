# 7/1/2024 - Additional practice with loops

myName = "Ryan"
for i in myName:
    print(i)



import random

randomInt = random.random()
userInput = input("Enter a number between 1 and 100: ")

if userInput > randomInt:
    print("To High. ")
elif userInput < randomInt:
    print("To Low. ")
else:
    print("Correct. ")