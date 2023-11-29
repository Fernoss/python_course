import random
from logo import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []

player_total = 0
dealer_total = 0

player_wins = False

def deal_card():
    return random.choice(cards)

def calculate_score(card_list):
    score = sum(card_list)
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw.", user_score, computer_score
    elif computer_score == 0:
        return "You lose. Dealer has a blackjack.", user_score, computer_score
    elif user_score == 0:
        return "You win with a blackjack!", user_score, computer_score
    elif user_score > 21:
        return "You went over. You lose.", user_score, computer_score
    elif computer_score > 21:
        return "Dealer went over. You win!", user_score, computer_score
    elif user_score > computer_score:
        return "You win!", user_score, computer_score
    else:
        return "You lose.", user_score, computer_score

def restart_game():
    global player, dealer, player_total, dealer_total, player_wins
    player = []
    dealer = []
    player_total = 0
    dealer_total = 0
    player_wins = False

print(logo)

# Initial deal
for _ in range(2):
    player.append(deal_card())
    dealer.append(deal_card())

player_total = calculate_score(player)
dealer_total = calculate_score(dealer)

# Check for Blackjack in initial deal
if player_total == 21:
    result, player_score, dealer_score = compare(player_total, dealer_total)
    print(f"\n{result}")
    print(f"Player's total score: {player_score}")
    print(f"Dealer's total score: {dealer_score}")
else:
    while True:
        print(f"Player's hand: {player} - your total is: {player_total}")
        print(f"Dealer's hand: {dealer[0]}")

        decision = input("Do you want to 'draw' a card or 'stay'? ").lower()

        if decision == "draw":
            new_card = deal_card()
            player.append(new_card)
            player_total = calculate_score(player)

            if player_total > 21:
                break  # Player went over 21, exit the loop
        elif decision == "stay":
            break  # Player decided to stay, exit the loop
        else:
            print("Invalid input. Please enter 'draw' or 'stay'.")

    # Compare scores after the loop
    result, player_score, dealer_score = compare(player_total, dealer_total)
    print(f"\n{result}")
    print(f"Player's total score: {player_score}")
    print(f"Dealer's total score: {dealer_score}")
