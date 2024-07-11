# Used to generate random card
import random

# Cards in the deck
kards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Randomize cards
def shuffle():
    return random.choice(kards)

# Ace card can either be 1 or 11 depending on situation
def scoreCalculate(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

# Win, lose, tie, and game conditions
def play():
    # starting amount of money for player
    money = 2500

    while money > 0:
        # Empty lists to append cards into
        playerCards = []
        dealerCards = []

        # Validy of amount bet
        print("Your money left: " + str(money))
        playerBet = int(input("Enter your bet: "))
        
        if playerBet <= 0 or playerBet > money:
            print("Invalid bet amount. ")
            continue
        
        print("You bet: " + str(playerBet))

        # Hand out cards each round
        playerCards.append(shuffle())
        playerCards.append(shuffle())
        dealerCards.append(shuffle())
        dealerCards.append(shuffle())

        gameOver = False

        # Loop
        while gameOver == False:
            playerScore = scoreCalculate(playerCards)
            dealerScore = scoreCalculate(dealerCards)

            # Printout to inform user
            print("Your current hand: " + str(playerCards) + ", current score: " + str(playerScore))
            print("Dealer's card: " + str(dealerCards[0]))
            
            if playerScore == 21 or dealerScore == 21 or playerScore > 21:
                gameOver = True
                break

            # Hit or stand
            choice = input("Type 'h' to hit (get another card), type 's' to stand: ")
            if choice == 'h':
                playerCards.append(shuffle())
            else:
                gameOver = True

        while scoreCalculate(dealerCards) < 17:
            dealerCards.append(shuffle())
        
        playerScore = scoreCalculate(playerCards)
        dealerScore = scoreCalculate(dealerCards)
        
        print("Your final hand: " + str(playerCards) + ", final score: " + str(playerScore))
        print("Dealer's final hand: " + str(dealerCards) + ", final score: " + str(dealerScore))
        
        # Win, lose, and tie condition
        if playerScore > 21:
            print("Score above 21. YOU LOSE. ")
            money -= playerBet
        elif dealerScore > 21 or playerScore > dealerScore:
            print("You WIN! ")
            money += playerBet
        elif playerScore == dealerScore:
            print("PUSH. ")
        else:
            print("YOU LOSE. ")
            money -= playerBet

    print("No money left. GAME OVER. ")

play()
