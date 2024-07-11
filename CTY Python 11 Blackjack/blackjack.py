# 7/9/2024 - Blackjack Card Game

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerCards = []
money = 2500

num = random.choice(cards)

# Enter bet
print("Your money left: " + money)
userBet = int(input("Enter your bet: "))
if userBet % 5 or userBet % 1 or userBet <= money:
    print("You bet: " + userBet)

# User
print("Your first card: ", end="")
print(num)
playerCards.append(num)
print("Your second card: ", end="")
print(num)

# Dealer
print("Dealer first card: ", end="")
print(num)
print("Dealer second card: ", end="")
#print(num)
print("?", end="")
