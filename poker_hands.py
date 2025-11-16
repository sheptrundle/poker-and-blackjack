# Poker hand reader test / winning hand calculator
# Shep Trundle
# May 2024

import random as rd
live = True

numerical_order = 'A23456789TJQKA'
names = {'high_card': 0, 'pair': 1, 'two pair': 2, 'trips': 3, 'straight': 4, 'flush': 5, 'full house': 6, 'quads': 7, 'straight flush': 8}
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
all_cards = ('2-s', '2-h', '2-c', '2-d', '3-s', '3-h', '3-c', '3-d', '4-s', '4-h', '4-c', '4-d', '5-s', '5-h', '5-c', '5-d', '6-s', '6-h', '6-c', '6-d',
             '7-s', '7-h', '7-c', '7-d', '8-s', '8-h', '8-c', '8-d', '9-s', '9-h', '9-c', '9-d', 'T-s', 'T-h', 'T-c', 'T-d', 'Q-s', 'Q-h', 'Q-c', 'Q-d',
             'K-s', 'K-h', 'K-c', 'K-d', 'A-s', 'A-h', 'A-c', 'A-d', )

def only_numbers(hand, list):
    for card in hand:
        num = card.split('-')[0]
        list.append(num)


def value(card):
    return card_values.get(card)


def flush(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    suit = hand[0].split('-')[1]
    flush_count = 0
    for card in hand:
        info = card.split('-')
        if info[1] == suit:
            flush_count += 1
    if flush_count == 5:
        return True
    else:
        return False


def straight(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    nums_in_hand = []
    only_numbers(hand, nums_in_hand)
    sorted_order = sorted(nums_in_hand, key=value)
    order = ''.join(sorted_order)
    if order in numerical_order:
        return True
    else:
        return False


def straight_flush(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    if straight(hand) and flush(hand):
        return True
    else:
        return False


def quads(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    nums_in_hand = []
    only_numbers(hand, nums_in_hand)
    for num in nums_in_hand:
        if nums_in_hand.count(num) == 4:
            return True
    return False


def full_house(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    nums_in_hand = []
    only_numbers(hand, nums_in_hand)
    for num in nums_in_hand:
        if nums_in_hand.count(num) == 3:
            for next_num in nums_in_hand:
                if nums_in_hand.count(next_num) == 2:
                    return True
    return False


def trips(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    nums_in_hand = []
    only_numbers(hand, nums_in_hand)
    for num in nums_in_hand:
        if nums_in_hand.count(num) == 3:
            for next_num in nums_in_hand:
                if nums_in_hand.count(next_num) == 1:
                    return True
    return False


def two_pair(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    nums_in_hand = []
    only_numbers(hand, nums_in_hand)
    for num in nums_in_hand:
        if nums_in_hand.count(num) == 2:
            nums_in_hand.remove(num)
            for next_num in nums_in_hand:
                if nums_in_hand.count(next_num) == 2:
                    return True
    return False


def pair(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    nums_in_hand = []
    pair_count = 0
    only_numbers(hand, nums_in_hand)
    for num in nums_in_hand:
        if nums_in_hand.count(num) == 2:
            pair_count += 1
            nums_in_hand.remove(num)
            for next_num in nums_in_hand:
                if nums_in_hand.count(next_num) > 1:
                    return False
    if pair_count == 1:
        return True
    else:
        return False


def get_name(hand=('A-s', 'K-s', 'Q-s', 'J-s', 'T-s')):
    if straight_flush(hand):
        return 'straight_flush'
    if quads(hand):
        return 'quads'
    if full_house(hand):
        return 'full_house'
    if flush(hand):
        return 'flush'
    if straight(hand):
        return 'straight'
    if trips(hand):
        return 'trips'
    if two_pair(hand):
        return 'two_pair'
    if pair(hand):
        return 'pair'
    else:
        return 'high_card'


def generate_random_hand(allow_print = 0):
    random_deck = list(all_cards)
    rd.shuffle(random_deck)
    hand = random_deck[0:5]
    if allow_print:
        print(hand)
        print(get_name(hand))
    return hand


def run_test(runs):
    i = 0
    high_card = 0
    pair = 0
    two_pair = 0
    trips = 0
    straight = 0
    flush = 0
    full_house = 0
    quads = 0
    straight_flush = 0
    while i < int(runs):
        hand = generate_random_hand()
        if get_name(hand) == 'high_card':
            high_card += 1
        if get_name(hand) == 'pair':
            pair += 1
        if get_name(hand) == 'two_pair':
            two_pair += 1
        if get_name(hand) == 'trips':
            trips += 1
        if get_name(hand) == 'straight':
            straight += 1
        if get_name(hand) == 'flush':
            flush += 1
        if get_name(hand) == 'full_house':
            full_house += 1
        if get_name(hand) == 'quads':
            quads += 1
        if get_name(hand) == 'straight_flush':
            straight_flush += 1
        i += 1
    print('High Card: ' + str(high_card))
    print('Pair: ' + str(pair))
    print('Two Pair: ' + str(two_pair))
    print('Trips: ' + str(trips))
    print('Straight: ' + str(straight))
    print('Flush: ' + str(flush))
    print('Full House: ' + str(full_house))
    print('Quads: ' + str(quads))
    print('Straight Flush: ' + str(straight_flush))


while live:
    entry = input('~')
    if entry == 'test':
        user_choice_runs = input('How many hands should be generated: ')
        run_test(user_choice_runs)
    elif entry != 'stop':
        generate_random_hand(1)
    else:
        live = False
