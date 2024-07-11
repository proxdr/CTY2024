import random

kards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def shuffle():
    return random.choice(kards)

def scoreCalculate(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def play():
    money = 2500

    while money > 0:
        playerCards = []
        dealerCards = []

        print("Your money left: " + money)
        playerBet = int(input("Enter your bet: "))
        
        if playerBet <= 0 or playerBet > money:
            print("Invalid bet amount. ")
        
        print("You bet: " + playerBet)

        playerCards.append(shuffle())
        playerCards.append(shuffle())
        dealerCards.append(shuffle())
        dealerCards.append(shuffle())

        gameOver = False

        while not gameOver:
            playerScore = scoreCalculate(playerCards)
            dealerScore = scoreCalculate(dealerCards)

            print("Your current hand: " + playerCards + ", current score: " + playerScore)
            print("Dealer's card: " + dealerCards[0])
            
            if playerScore == 21 or dealerScore == 21 or playerScore > 21:
                gameOver = True
                break

            choice = input("Type 'h' to hit (get another card), type 's' to stand: ")
            if choice == 'h':
                playerCards.append(shuffle())
            else:
                gameOver = True

        while scoreCalculate(dealerCards) < 17:
            dealerCards.append(shuffle())
        
        playerScore = scoreCalculate(playerCards)
        dealerScore = scoreCalculate(dealerCards)
        
        print("Your final hand: " + playerCards + ", final score: " + playerScore)
        print("Dealer's final hand: " + dealerCards + ", final score: " + dealerScore)

        if playerScore > 21:
            print("You went over 21. You lose.")
            money -= playerBet
        elif dealerScore > 21 or playerScore > dealerScore:
            print("You win!")
            money += playerBet
        elif playerScore == dealerScore:
            print("It's a draw!")
        else:
            print("You lose.")
            money -= playerBet

    print("You are out of money. Game over.")

play()