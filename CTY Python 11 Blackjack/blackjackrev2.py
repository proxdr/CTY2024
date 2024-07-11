import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
money = 2500

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def play_blackjack():
    global money

    while money > 0:
        player_cards = []
        dealer_cards = []

        print(f"Your money left: {money}")
        user_bet = int(input("Enter your bet: "))
        
        if user_bet <= 0 or user_bet > money:
            print("Invalid bet amount.")
            continue

        print(f"You bet: {user_bet}")

        # Deal initial cards
        player_cards.append(deal_card())
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
        dealer_cards.append(deal_card())

        print(f"Your first card: {player_cards[0]}")
        print(f"Your second card: {player_cards[1]}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        print("Dealer's second card: ?")

        game_over = False

        while not game_over:
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)

            print(f"Your current hand: {player_cards}, current score: {player_score}")
            
            if player_score == 21 or dealer_score == 21 or player_score > 21:
                game_over = True
                break

            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

        while calculate_score(dealer_cards) < 17:
            dealer_cards.append(deal_card())
        
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

        if player_score > 21:
            print("You went over 21. You lose.")
            money -= user_bet
        elif dealer_score > 21 or player_score > dealer_score:
            print("You win!")
            money += user_bet
        elif player_score == dealer_score:
            print("It's a draw!")
        else:
            print("You lose.")
            money -= user_bet

    print("You are out of money. Game over.")

play_blackjack()
