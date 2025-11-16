# Blackjack Full Game
# Shep Trundle
# 5/29/24

import bj_score as bj
import random as rd
import time


def results():
    print('Player has ' + simple(player) + ' (' + str(bj.score(player)) + ')')
    print('Dealer shows ' + str(dealer[0]))


def player_results():
    print('Player has ' + simple(player) + ' (' + str(bj.score(player)) + ')')


def dealer_results():
    print('Dealer has ' + simple(dealer) + ' (' + str(bj.score(dealer)) + ')')


def simple(hand):
    return ', '.join(hand)


def dealer_draw():
    time.sleep(1)  # wait
    dealer_results()
    time.sleep(1)  # wait
    while bj.score(dealer) != 'bust' and bj.score(dealer) < 17:
        print('Dealer hits')
        dealer.append(rd.choice(cards))
        time.sleep(1.5)  # wait
        dealer_results()
        print('')
        time.sleep(1.5)  # wait
    if bj.score(dealer) == 'bust':
        print('Dealer ends busted')
    else:
        print('Dealer ends with ' + str(bj.score(dealer)))


def determine_winner(player_param, dealer_param):
    global result
    global going
    if bj.score(player_param) == 'bust':
        print('Player busts, dealer wins with ' + bj.score(dealer_param))
        result = 'l'
        going = False
    elif bj.score(dealer_param) == 'bust' or bj.score(player_param) > bj.score(dealer_param):
        print('Player wins! ' + str(bj.score(player_param)) + ' over ' + str(bj.score(dealer_param)))
        result = 'w'
        going = False
    elif bj.score(player_param) < bj.score(dealer_param):
        print('Dealer wins: ' + str(bj.score(dealer_param)) + ' over ' + str(bj.score(player_param)))
        result = 'l'
        going = False
    else:
        print('Push: Tied at ' + str(bj.score(player_param)))
        result = 'p'
        going = False


def determine_winner_no_print(player_param, dealer_param):
    if bj.score(player_param) == 'bust':
        return 'b'
    elif bj.score(dealer_param) == 'bust' or bj.score(player_param) > bj.score(dealer_param):
        return 'w'
    elif bj.score(player_param) < bj.score(dealer_param):
        return 'l'
    else:
        return 'p'


def split_hand_results(card, check_for_first):
    if check_for_first:
        print('First hand has ' + simple(card) + ' (' + str(bj.score(card)) + ')')
    else:
        print('Second hand has ' + simple(card) + ' (' + str(bj.score(card)) + ')')


def split(card1, card2):
    global total
    global option
    global able
    total = 0
    able = False
    if bj.card_to_value(card1) == bj.card_to_value(card2) and wager <= bank/2:     # ensures able to split
        able = True
        first_card = True
        both_hands = [card1, card2]
        for card in both_hands:          # splits apart cards
            print('')
            on = True
            hand = [card]
            if first_card:  # runs process for first card
                already_hit = False
                while on:
                    if not already_hit:
                        print('~For first hand~')
                        split_hand_results(hand, first_card)
                        already_hit = True
                    option = input('Hit or Stand: ')
                    if option.lower() == 'hit' or option.lower() == 'h':  # player hits
                        hand.append(rd.choice(cards))
                        print('')
                        split_hand_results(hand, first_card)
                        if bj.score(hand) == 'bust':
                            print('First Hand Busts')
                            time.sleep(1)
                            final1 = hand
                            first_card = False
                            on = False
                    if option.lower() == 'stand' or option.lower() == 's':  # player stands
                        print('First Hand stands on ' + str(bj.score(hand)))
                        final1 = hand
                        on = False
                        first_card = False
            else:                         # runs process for second card, exact same as above
                already_hit = False
                while on:
                    if not already_hit:
                        print('~For second hand~')
                        split_hand_results(hand, first_card)
                        already_hit = True
                    option = input('Hit or Stand: ')
                    if option.lower() == 'hit' or option.lower() == 'h':  # player hits
                        hand.append(rd.choice(cards))
                        print('')
                        split_hand_results(hand, first_card)
                        if bj.score(hand) == 'bust':
                            print('Second Hand Busts')
                            print('')
                            final2 = hand
                            on = False
                    if option.lower() == 'stand' or option.lower() == 's':  # player stands
                        print('Second Hand stands on ' + str(bj.score(hand)))
                        print('')
                        final2 = hand
                        on = False
        dealer_draw()
        print('')
        i = 0
        for hand in [final1, final2]:              # used for adding wager to bank
            i += 1
            if determine_winner_no_print(hand, dealer) == 'w':
                total += 1
                script = 'Hand ' + str(i) + ' wins'
                print(script)
            if determine_winner_no_print(hand, dealer) == 'l':
                total -= 1
                script = 'Hand ' + str(i) + ' loses'
                print(script)
            if determine_winner_no_print(hand, dealer) == 'b':
                total -= 1
                script = 'Hand ' + str(i) + ' busts and loses'
                print(script)
            if determine_winner_no_print(hand, dealer) == 'p':
                script = 'Hand ' + str(i) + ' pushes'
                print(script)
    else:
        print('Cannot Split Cards')


cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
live = True
bank = 100
max_stack = 0

while live:                            # while loop for entire game
    if bank > max_stack:               # calculates high point during game
        max_stack = bank
    first_hit = True
    going = True
    splitted = False
    print('')
    print('Bank = ' + str(bank))
    if bank <= 0:                      # ends game if bank is 0 or negative
        print('Insufficient Funds')
        print('Max Stack: ' + str(max_stack))
        break
    wager = int(input('Bet size: '))
    if wager > bank:                   # ensures wager isnt too large
        print('Bet Size Too Large')
        result = 'redo'
        going = False
    if wager == 'stop':              # ERROR: code crashes because it cant turn "stop" into an int, otherwise would work
        print('Game Ended with ' + str(bank))
        print('Max Stack: ' + str(max_stack))
        break
    player = [rd.choice(cards), rd.choice(cards)]
    dealer = [rd.choice(cards), rd.choice(cards)]
    initial_cards = True
    while going:                        # while loop for one singular hand
        if initial_cards:               # only shows both player and dealer results together at start
            results()
        if initial_cards and bj.score(player) == 21:      # checking for player blackjack
            if bj.score(dealer) == 21:
                time.sleep(1.5)
                dealer_results()
                print('Push: Tied at Blackjack')
                result = 'p'
                going = False
            else:
                time.sleep(1.5)
                print('Blackjack!')
                wager = int(wager*1.5)
                result = 'w'
                going = False
        if initial_cards and bj.score(dealer) == 21 and going:      # checking for dealer blackjack
            time.sleep(1)
            dealer_results()
            print('Dealer has Blackjack')
            result = 'l'
            going = False
        initial_cards = False           # enters the hit/stand phase
        if going:                       # ensures no blackjacks before asking hit/stand
            option = input('Hit or Stand: ')
            if option.lower() == 'hit' or option.lower() == 'h':    # player hits
                first_hit = False
                player.append(rd.choice(cards))
                print('')
                player_results()
                if bj.score(player) == 'bust':
                    time.sleep(1)  # wait
                    dealer_results()
                    time.sleep(1)  # wait
                    print('Player busts, dealer wins')
                    result = 'l'
                    going = False
            if option.lower() == 'stand' or option.lower() == 's':  # player stands
                print('Player stands on ' + str(bj.score(player)))
                print('')
                dealer_draw()
                determine_winner(player, dealer)
            if option.lower() == 'double down' or option.lower() == 'dd' or option.lower() == 'd':  # player doubles down
                if wager*2 <= bank and first_hit:
                    wager *= 2
                    print('Player doubles down')
                    player.append(rd.choice(cards))
                    print('')
                    player_results()
                    if bj.score(player) == 'bust':
                        time.sleep(1)  # wait
                        dealer_results()
                        time.sleep(1)  # wait
                        print('Player busts, dealer wins')
                        result = 'l'
                        going = False
                    else:
                        dealer_draw()
                        determine_winner(player, dealer)
                else:
                    print('Cannot Double Down')
            if option.lower() == 'split' or option.lower() == 'sp':                # player splits
                card_first = player[0]
                card_second = player[1]
                split(card_first, card_second)
                if able:
                    splitted = True
                    going = False
    if not splitted:
        if result == 'w':               # checking for win
            bank += wager
        if result == 'l':               # checking for loss
            bank -= wager
    if splitted:                        # activates only for split hands
        bank += (wager*total)


# to do list:
# add an option to type 'help'/'h' that gives a list of inputs
# add a prompt telling player they can type 'help'/'h'
# make sure no double splitting/double downing
# split should deal second card automatically (instead of players having to hit)

# Personal High: 3040
