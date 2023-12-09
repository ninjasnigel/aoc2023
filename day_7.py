def format_data(raw):
    new_data = [line.split(" ") for line in raw.split("\n")]
    return new_data, new_data

#values = {"2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

values = {"J": 1, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":11, "K":12, "A":13}

# Super unclean, only works for part 2 please dont look at this
# Super unclean, only works for part 2 please dont look at this
# Super unclean, only works for part 2 please dont look at this
# Super unclean, only works for part 2 please dont look at this
# Super unclean, only works for part 2 please dont look at this
# Super unclean, only works for part 2 please dont look at this

def hand_to_values(hand):
    return [values[card] for card in hand]

def high_card(hand):
    return 1, False

def pair(hand):
    for card in hand:
        if hand.count(card) == 2:
            return 2, False
    if "J" in hand:
        return 2, "J"
    return False, False

def two_pair(hand):
    pairs = []
    for card in hand:
        if hand.count(card) == 2:
            pairs += card
    if len(pairs) == 4:
        return 3, False
    return False, False

def three_of_a_kind(hand):
    # count amounts of Jokers in hand for example two for "JJXAD"
    if(hand.count("J") >= 2): return 4, "J"
    for card in hand:
        if card == "J": continue
        if hand.count(card) == 3:
            return 4, False
        elif hand.count(card) == 2 and "J" in hand:
            return 4, "J"
    return False, False

def full_house(hand):
    joker_count = hand.count("J")
    pair_type = pair(hand)
    three = three_of_a_kind(hand)
    two_pair_type = two_pair(hand)
    if two_pair_type[0] and "J" in hand:
        return 5, "J"
    if pair_type[0] and three[0] and "J" not in hand:
        return 5, False
    for card in hand:
        if card == "J": continue
        if hand.count(card) == 3 and joker_count == 2:
            return 5, "J"
        if hand.count(card) == 2 and joker_count == 3:
            return 5, "J"
    
    return False, False

def four_of_a_kind(hand):
    jokers = hand.count("J")
    if(jokers >= 3): return 6, "J"
    for card in hand:
        if card == "J": continue
        if hand.count(card) == 4:
            return 6, False
        elif hand.count(card) == 3 and "J" in hand:
            return 6, "J"
        elif hand.count(card) == 2 and jokers >=2:
            return 6, "J"
        
    return False, False

def five_of_a_kind(hand):
    jokers = hand.count("J")
    if(jokers >= 4): return 7, "J"
    for card in hand:
        if card == "J": continue
        if hand.count(card) == 5:
            return 7, False
        elif hand.count(card) == 4 and "J" in hand:
            return 7, "J"
        elif hand.count(card) == 3 and jokers >= 2:
            return 7, "J"
        elif hand.count(card) == 2 and jokers >= 3:
            return 7, "J"
    return False, False

win_types = [five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, pair, high_card]

def star1(data):
    best_hands = []
    for i in range(len(data)):
        hand = data[i][0]
        wager = data[i][1]
        wins = []
        for win in win_types:
            hand_scores = win(hand)
            if hand_scores[0]:
                wins += [hand_scores[0]]
        wins_sorted = sorted(wins, reverse=True)
        best_hands += [(wins_sorted[0], hand, wager)]
    best_hands_sorted = sorted(best_hands, key=lambda x: (x[0], hand_to_values(x[1])))
    sum = 0
    for i in range(len(best_hands_sorted)):
        sum += (i+1) * int(best_hands_sorted[i][2])
    return sum

def star2(data):
    best_hands = []
    for i in range(len(data)):
        hand = data[i][0]
        wager = data[i][1]
        wins = []
        for win in win_types:
            hand_scores = win(hand)
            if hand_scores[0]:
                wins += [hand_scores[0]]
        wins_sorted = sorted(wins, reverse=True)
        best_hands += [(wins_sorted[0], hand, wager)]
    best_hands_sorted = sorted(best_hands, key=lambda x: (x[0], hand_to_values(x[1])))
    sum = 0
    for i in range(len(best_hands_sorted)):
        sum += (i+1) * int(best_hands_sorted[i][2])
    return sum

from elis_script import *

if __name__ == '__main__':
    main(format_data, star1, star2) # add year, day if not done on puzzle day