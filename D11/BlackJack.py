import BlackJackArt
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []

def deal_cards():
    hand = random.choice(cards)
    return hand

def starting_hand():
    hand = [] 
    cards_dealt = 0
    while cards_dealt < 2:
        hand.append(deal_cards())
        cards_dealt += 1
    
    return hand

def player_wins(player_hand, dealer_hand):
    if sum(player_hand) > 21:
        return f"You went bust with {sum(player_hand)}. You lose."
    elif sum(dealer_hand) > 21:
        return f"The dealer went bust with {sum(dealer_hand)}. You win!"
    elif sum(player_hand) > sum(dealer_hand):
        return f"The dealer only had {sum(dealer_hand)}. While you have {sum(player_hand)}. You win!"
    elif sum(player_hand) == sum(dealer_hand):
        return f"Both you and the dealer has value of total {sum(dealer_hand)}. It's a draw!"
    else:
        return f"You only had {sum(player_hand)}. While the dealer has {sum(dealer_hand)}. You lose"


def bust(hand):
    if sum(hand) > 21:
        return True

def black_jack():
    print(BlackJackArt.logo)
    player_hand = starting_hand()
    dealer_hand = starting_hand()
    print(f"Player hand: {player_hand}, dealer hand = {dealer_hand[0]}")

    game_continues = True

    while game_continues:
        choice = input('Would you like to take another hit or stand? "Y" to get hit, "N" for stand: ').lower()
        if choice == "n":
            game_continues = False
        else:
            player_hand.append(deal_cards())
            print(f"Your hand: {player_hand}, Dealer's hand: {dealer_hand[0]}")
            if bust(player_hand):
                break

    while sum(dealer_hand) < 16 and not bust(player_hand):
        dealer_hand.append(deal_cards())
        print("Dealer's hands: ")
        print(dealer_hand)
    result = player_wins(player_hand, dealer_hand)
    print(result)

black_jack()
while input('Would you like to play again? Type "Y" for yes, type "N" for no: ').lower() == "y":
    black_jack()