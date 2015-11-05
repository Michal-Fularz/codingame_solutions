__author__ = 'Amin'

import sys
import math


class Player:
    def __init__(self, number):
        self.number = number
        self.deck = []

    def get_deck_as_text(self):
        deck_as_text = ""
        for card in self.deck:
            deck_as_text += str(card)
            deck_as_text += ", "

        return deck_as_text

    def get_top_card(self):
        return self.deck.pop(0)

    def get_top_three_cards(self):
        cards = []
        for i in range(3):
            cards.append(self.deck.pop(0))

        return cards

    def add_won_cards(self, my_cards, opponent_cards):
        if len(my_cards) == len(opponent_cards):
            self.deck += my_cards + opponent_cards

            #for my_card, opponent_card in zip(my_cards, opponent_cards):
                #self.deck.append(my_card)
                #self.deck.append(opponent_card)
        else:
            print("Wrong number of cards from players!")


def convert_card_name_to_value(card_name):
    card_value = -1

    if len(card_name) == 3:
        # special case - 10
        card_value = 10
    else:
        # card name format: XY
        # X - one of 1/2/3/4/5/6/7/8/9/J/Q/K/A
        # Y - one of D/H/C/S - this does not matter for card value
        if card_name[0] == "2" or \
            card_name[0] == "3" or \
            card_name[0] == "4" or \
            card_name[0] == "5" or \
            card_name[0] == "6" or \
            card_name[0] == "7" or \
            card_name[0] == "8" or \
            card_name[0] == "9":

            card_value = int(card_name[0])
        elif card_name[0] == "J":
            card_value = 11
        elif card_name[0] == "Q":
            card_value = 12
        elif card_name[0] == "K":
            card_value = 13
        elif card_name[0] == "A":
            card_value = 14
        else:
            card_value = -2

    return card_value


def play_war(p1, p2, used_cards_p1, used_cards_p2):
    if len(p1.deck) < 4 or len(p2.deck) < 4:
        return -1

    used_cards_p1 += p1.get_top_three_cards()
    used_cards_p2 += p2.get_top_three_cards()

    card_from_p1 = p1.get_top_card()
    card_from_p2 = p2.get_top_card()

    if card_from_p1 > card_from_p2:
        winner_of_war = 1
    elif card_from_p1 < card_from_p2:
        winner_of_war = 2
    else:
        winner_of_war = play_war(p1, p2, used_cards_p1, used_cards_p2)

    used_cards_p1.append(card_from_p1)
    used_cards_p2.append(card_from_p2)

    return winner_of_war

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

player_1 = Player(1)
player_2 = Player(2)

n = int(input())        # the number of cards for player 1
for i in range(n):         # the n cards of player 1
    card_value = convert_card_name_to_value(input())
    player_1.deck.append(card_value)
m = int(input())        # the number of cards for player 2
for i in range(m):         # the m cards of player 2
    card_value = convert_card_name_to_value(input())
    player_2.deck.append(card_value)

flag_war_has_ended = False
number_of_rounds = 0

while not flag_war_has_ended:
    #print(player_1.get_deck_as_text(), file=sys.stderr)
    #print(player_2.get_deck_as_text(), file=sys.stderr)

    # draw cards
    card_from_player_1 = player_1.get_top_card()
    card_from_player_2 = player_2.get_top_card()
    # compare
    used_cards_from_player_1 = []
    used_cards_from_player_2 = []
    used_cards_from_player_1.append(card_from_player_1)
    used_cards_from_player_2.append(card_from_player_2)
    winner = -1
    if card_from_player_1 > card_from_player_2:
        winner = 1
    elif card_from_player_1 < card_from_player_2:
        winner = 2
    else:
        # if a draw - play a sub-war
        winner = play_war(player_1, player_2, used_cards_from_player_1, used_cards_from_player_2)

    # distribute the winnings
    if winner == 1:
        player_1.add_won_cards(used_cards_from_player_1, used_cards_from_player_2)
    elif winner == 2:
        player_2.add_won_cards(used_cards_from_player_1, used_cards_from_player_2)
    else:
        # end of cards during the war - PAT
        flag_war_has_ended = True

    number_of_rounds += 1

    print("Winner of round " + str(number_of_rounds) + ": " + str(winner) + ", P1 number of cards " + str(len(player_1.deck)) + ", P2 number of cards " + str(len(player_2.deck)), file=sys.stderr)

    # check if game should be continued
    if len(player_1.deck) == 0 or len(player_2.deck) == 0:
        flag_war_has_ended = True

if len(player_1.deck) == 0:
    r = "2 " + str(number_of_rounds)
elif len(player_2.deck) == 0:
    r = "1 " + str(number_of_rounds)
else:
    r = "PAT"

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print(r)
