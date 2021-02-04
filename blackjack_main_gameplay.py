
import blackjack_milestone2
from blackjack_milestone2 import *
print("\n\t*******BLACK JACK*******")
print("\t********CARD GAME********")
print("\t*********2021*********")
# CREATING PLAYER PROFILE

# Taking player names
print('\n'*2)
name1 = player_name()

# Player instances created
first_hand = Player(name1)
print(f"\n\n\t\t{first_hand.name}'s profile created")

# Dummy player_instances created
# In case of SPLIT
second_hand = Player("2nd_hand")

third_hand = Player("3rd_hand")

fourth_hand = Player("4th_hand")

fifth_hand = Player("5th_hand")

sixth_hand = Player("6th_hand")

seventh_hand = Player("7th_hand")

eighth_hand = Player("8th_hand")

ninth_hand = Player("9th_hand")

tenth_hand = Player("10th_hand")


# Creating Computer instance
comp = Player("Computer")


# Setting up player account
print(f"\n\n\t\t\t\t{first_hand.name}'s Account has Been Bankrolled")
first_hand.bankroll_account(1000)
first_hand.get_balance()

round_no = 0
game_on = True

while game_on:
    round_no += 1
    print(f"\n\n\t\tRound {round_no} BEGINS!")

    # CREATING DEALER PROFILE
    # Dealer instance created
    dealer = Dealer()

    # Dealer brings out deck of 52 cards
    dealer.deck_up()

    # Dealer shuffles his deck
    print('\n' * 2)
    dealer.deck_shuffle()
    dealer.get_deck()


    # Player places bet
    first_hand.place_bet()

    # Dealer deals card to player
    first_hand.receive_card(dealer.deal_card())
    first_hand.receive_card(dealer.deal_card())
    first_hand.get_hand()

    # Dealer deals card to computer
    comp.receive_card(dealer.deal_card())
    comp.receive_card(dealer.deal_card())
    comp.get_hand()

    # Number of cards in the dealer's deck
    dealer.get_deck()

    # Checking for presence of Aces
    # Reduce the card total by 10 * Number of aces (if ace is present)
    first_hand.ace_adjust()

    # Check for BLACKJACK
    # PLAYER SCORES A BLACKJACK
    if len(first_hand.hand) < 3 and (first_hand.card_sum == 21) and (comp.card_sum != 21):
        print(f"\n\t\t{first_hand.name} WINS THE ROUND!")
        first_hand.view_hand()
        comp.view_hand()
        print(f"\n\n\t\t*****BLACKJACK for {first_hand.name}*****")
        first_hand.add_cash(2.5 * first_hand.bet)
        first_hand.get_balance()
        first_hand.hand.clear()
        comp.hand.clear()
        continue

    # COMPUTER SCORES A BLACKJACK
    elif len(comp.hand) < 3 and (first_hand.card_sum != 21) and (comp.card_sum == 21):
        first_hand.view_hand()
        comp.view_hand()
        print(f"\n\n\t\t{first_hand.name} LOSES THE ROUND!")
        print(f"\n\n\t\t*****BLACKJACK for {comp.name}*****\n")
        first_hand.get_balance()
        first_hand.hand.clear()
        comp.hand.clear()
        if first_hand.account == 0:
            first_hand.get_balance()
            print(f"\n\n\n\t\t{first_hand.name} is OUT OF CASH!")
            print("\n\t\tGAME OVER!!!")
            game_on = False
        continue

    waiting = True
    first_turn = True

    # PLAYER'S TURN
    # Wait for player to eventually stand, double, or surrender (after hit)
    while waiting or first_turn:

        # Check for first split
        first_split = first_hand.split()
        second_split = False
        third_split = False

        first_hand.ace_adjust()

        # Player splits for the first time
        while first_split:

            # When second hand is occupied
            if len(second_hand.hand) > 0:

                if len(seventh_hand.hand) < 1:
                    seventh_hand.split_done(first_hand, first_hand)

                    # To continue playing or exit game
                    first_hand.play_on()

                    seventh_split_time = True

                    while True:

                        # Making the necessary adjustments
                        seventh_hand.ace_adjust()

                        # Check for BLACKJACK
                        # PLAYER SCORES A BLACKJACK
                        if  len(seventh_hand.hand) < 3 and (seventh_hand.card_sum == 21) and (comp.card_sum != 21):
                            print(f"\n\t\t{seventh_hand.name} WINS!")
                            seventh_hand.view_hand()
                            print(f"\n\n\t\t*****BLACKJACK for {seventh_hand.name}*****")
                            seventh_hand.add_cash(2.5 * seventh_hand.bet)
                            first_hand.account = seventh_hand.account
                            first_hand.get_balance()
                            seventh_hand.hand.clear()
                            first_split = False
                            break

                        # Computer's sixth card exposed
                        comp.computer_faceup()

                        # PLAYER'S SECOND HAND TURN
                        # Second hand makes sixth move
                        if seventh_split_time:
                            response = seventh_hand.four_options()
                        else:
                            response = seventh_hand.two_options()

                        answer = seventh_hand.player_action(dealer, response)

                        # To continue playing or exit game
                        first_hand.play_on()

                        # PLAYER HITS
                        if answer == 'hit':
                            seventh_split_time = False
                            continue

                        # PLAYER DOUBLES
                        elif answer == 'double':
                            seventh_hand.ace_adjust()
                            seventh_hand.view_hand()
                            first_hand.account = seventh_hand.account
                            first_hand.get_balance()
                            break

                        elif answer == 'ask':
                            continue

                        elif answer == 'wave':
                            break

                        # PLAYER SURRENDERS
                        else:
                            print(f"\n\n\t{seventh_hand.name} SURRENDERS!")
                            seventh_hand.view_hand()
                            first_hand.account = seventh_hand.account
                            first_hand.get_balance()
                            seventh_hand.hand.clear()
                            seventh_hand.bet = 0
                            break


                elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) < 1):
                    eighth_hand.split_done(first_hand, first_hand)

                    # To continue playing or exit game
                    first_hand.play_on()


                    eighth_split_time = True

                    while True:

                        # Making the necessary adjustments
                        eighth_hand.ace_adjust()

                        # Check for BLACKJACK
                        # PLAYER SCORES A BLACKJACK
                        if  len(eighth_hand.hand) < 3 and (eighth_hand.card_sum == 21) and (comp.card_sum != 21):
                            print(f"\n\t\t{eighth_hand.name} WINS!")
                            eighth_hand.view_hand()
                            print(f"\n\n\t\t*****BLACKJACK for {eighth_hand.name}*****")
                            eighth_hand.add_cash(2.5 * eighth_hand.bet)
                            first_hand.account = eighth_hand.account
                            first_hand.get_balance()
                            eighth_hand.hand.clear()
                            first_split = False
                            break

                        # Computer's sixth card exposed
                        comp.computer_faceup()

                        # PLAYER'S SECOND HAND TURN
                        # Second hand makes sixth move
                        if eighth_split_time:
                            response = eighth_hand.four_options()
                        else:
                            response = eighth_hand.two_options()

                        answer = eighth_hand.player_action(dealer, response)

                        # To continue playing or exit game
                        first_hand.play_on()

                        # PLAYER HITS
                        if answer == 'hit':
                            eighth_split_time = False
                            continue

                        # PLAYER DOUBLES
                        elif answer == 'double':
                            eighth_hand.ace_adjust()
                            eighth_hand.view_hand()
                            first_hand.account = eighth_hand.account
                            first_hand.get_balance()
                            break

                        elif answer == 'ask':
                            continue

                        elif answer == 'wave':

                            break

                        # PLAYER SURRENDERS
                        else:
                            print(f"\n\n\t{eighth_hand.name} SURRENDERS!")
                            eighth_hand.view_hand()
                            first_hand.account = eighth_hand.account
                            first_hand.get_balance()
                            eighth_hand.hand.clear()
                            eighth_hand.bet = 0
                            break

                elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) < 1):
                    ninth_hand.split_done(first_hand, first_hand)

                    # To continue playing or exit game
                    first_hand.play_on()


                    ninth_split_time = True

                    while True:

                        # Making the necessary adjustments
                        ninth_hand.ace_adjust()

                        # Check for BLACKJACK
                        # PLAYER SCORES A BLACKJACK
                        if  len(ninth_hand.hand) < 3 and (ninth_hand.card_sum == 21) and (comp.card_sum != 21):
                            print(f"\n\t\t{ninth_hand.name} WINS!")
                            ninth_hand.view_hand()
                            print(f"\n\n\t\t*****BLACKJACK for {ninth_hand.name}*****")
                            ninth_hand.add_cash(2.5 * ninth_hand.bet)
                            first_hand.account = ninth_hand.account
                            first_hand.get_balance()
                            ninth_hand.hand.clear()
                            first_split = False
                            break

                        # Computer's sixth card exposed
                        comp.computer_faceup()

                        # PLAYER'S SECOND HAND TURN
                        # Second hand makes sixth move
                        if ninth_split_time:
                            response = ninth_hand.four_options()
                        else:
                            response = ninth_hand.two_options()

                        answer = ninth_hand.player_action(dealer, response)

                        # To continue playing or exit game
                        first_hand.play_on()

                        # PLAYER HITS
                        if answer == 'hit':
                            ninth_split_time = False
                            continue

                        # PLAYER DOUBLES
                        elif answer == 'double':
                            ninth_hand.ace_adjust()
                            ninth_hand.view_hand()
                            first_hand.account = ninth_hand.account
                            first_hand.get_balance()
                            break

                        elif answer == 'ask':
                            continue

                        elif answer == 'wave':

                            break

                        # PLAYER SURRENDERS
                        else:
                            print(f"\n\n\t{ninth_hand.name} SURRENDERS!")
                            ninth_hand.view_hand()
                            first_hand.account = ninth_hand.account
                            first_hand.get_balance()
                            ninth_hand.hand.clear()
                            ninth_hand.bet = 0
                            break

                elif (len(tenth_hand) < 1) and (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) > 0):
                    tenth_hand.split_done(first_hand, first_hand)

                    # To continue playing or exit game
                    first_hand.play_on()


                    tenth_split_time = True

                    while True:

                        # Making the necessary adjustments
                        tenth_hand.ace_adjust()

                        # Check for BLACKJACK
                        # PLAYER SCORES A BLACKJACK
                        if  len(tenth_hand.hand) < 3 and (tenth_hand.card_sum == 21) and (comp.card_sum != 21):
                            print(f"\n\t\t{tenth_hand.name} WINS!")
                            tenth_hand.view_hand()
                            print(f"\n\n\t\t*****BLACKJACK for {tenth_hand.name}*****")
                            tenth_hand.add_cash(2.5 * tenth_hand.bet)
                            first_hand.account = tenth_hand.account
                            first_hand.get_balance()
                            tenth_hand.hand.clear()
                            first_split = False
                            break

                        # Computer's sixth card exposed
                        comp.computer_faceup()

                        # PLAYER'S SECOND HAND TURN
                        # Second hand makes sixth move
                        if tenth_split_time:
                            response = tenth_hand.four_options()
                        else:
                            response = tenth_hand.two_options()

                        answer = tenth_hand.player_action(dealer, response)

                        # To continue playing or exit game
                        first_hand.play_on()

                        # PLAYER HITS
                        if answer == 'hit':
                            tenth_split_time = False
                            continue

                        # PLAYER DOUBLES
                        elif answer == 'double':
                            tenth_hand.ace_adjust()
                            tenth_hand.view_hand()
                            first_hand.account = tenth_hand.account
                            first_hand.get_balance()
                            break

                        elif answer == 'ask':
                            continue

                        elif answer == 'wave':
                            break

                        # PLAYER SURRENDERS
                        else:
                            print(f"\n\n\t{tenth_hand.name} SURRENDERS!")
                            tenth_hand.view_hand()
                            first_hand.account = tenth_hand.account
                            first_hand.get_balance()
                            tenth_hand.hand.clear()
                            tenth_hand.bet = 0
                            break

            second_hand.split_done(first_hand, first_hand)

            # To continue playing or exit game
            first_hand.play_on()


            first_split_time = True

            while True:

                # Making the necessary adjustments
                second_hand.ace_adjust()

                # Check for BLACKJACK
                # PLAYER SCORES A BLACKJACK
                if  len(second_hand.hand) < 3 and (second_hand.card_sum == 21) and (comp.card_sum != 21):
                    print(f"\n\t\t{second_hand.name} WINS!")
                    second_hand.view_hand()
                    print(f"\n\n\t\t*****BLACKJACK for {second_hand.name}*****")
                    second_hand.add_cash(2.5 * second_hand.bet)
                    first_hand.account = second_hand.account
                    first_hand.get_balance()
                    second_hand.hand.clear()
                    first_split = False
                    break

                # Check second hand for matching card occurrence
                second_split = second_hand.split()

                # Player splits for the first time
                while second_split:

                    if len(third_hand.hand) > 0:
                        if len(seventh_hand.hand) < 1:
                            seventh_hand.split_done(second_hand, first_hand)

                            # To continue playing or exit game
                            first_hand.play_on()


                            seventh_split_time = True

                            while True:

                                # Making the necessary adjustments
                                seventh_hand.ace_adjust()

                                # Check for BLACKJACK
                                # PLAYER SCORES A BLACKJACK
                                if  len(seventh_hand.hand) < 3 and (seventh_hand.card_sum == 21) and (comp.card_sum != 21):
                                    print(f"\n\t\t{seventh_hand.name} WINS!")
                                    seventh_hand.view_hand()
                                    print(f"\n\n\t\t*****BLACKJACK for {seventh_hand.name}*****")
                                    seventh_hand.add_cash(2.5 * seventh_hand.bet)
                                    first_hand.account = seventh_hand.account
                                    first_hand.get_balance()
                                    seventh_hand.hand.clear()
                                    first_split = False
                                    break

                                # Computer's sixth card exposed
                                comp.computer_faceup()

                                # PLAYER'S SECOND HAND TURN
                                # Second hand makes sixth move
                                if seventh_split_time:
                                    response = seventh_hand.four_options()
                                else:
                                    response = seventh_hand.two_options()

                                answer = seventh_hand.player_action(dealer, response)

                                # To continue playing or exit game
                                first_hand.play_on()

                                # PLAYER HITS
                                if answer == 'hit':
                                    seventh_split_time = False
                                    continue

                                # PLAYER DOUBLES
                                elif answer == 'double':
                                    seventh_hand.ace_adjust()
                                    seventh_hand.view_hand()
                                    first_hand.account = seventh_hand.account
                                    first_hand.get_balance()
                                    break

                                elif answer == 'ask':
                                    continue

                                elif answer == 'wave':

                                    break

                                # PLAYER SURRENDERS
                                else:
                                    print(f"\n\n\t{seventh_hand.name} SURRENDERS!")
                                    seventh_hand.view_hand()
                                    first_hand.account = seventh_hand.account
                                    first_hand.get_balance()
                                    seventh_hand.hand.clear()
                                    seventh_hand.bet = 0
                                    break


                        elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) < 1):
                            eighth_hand.split_done(second_hand, first_hand)

                            # To continue playing or exit game
                            first_hand.play_on()


                            eighth_split_time = True

                            while True:

                                # Making the necessary adjustments
                                eighth_hand.ace_adjust()

                                # Check for BLACKJACK
                                # PLAYER SCORES A BLACKJACK
                                if  len(eighth_hand.hand) < 3 and (eighth_hand.card_sum == 21) and (comp.card_sum != 21):
                                    print(f"\n\t\t{eighth_hand.name} WINS!")
                                    eighth_hand.view_hand()
                                    print(f"\n\n\t\t*****BLACKJACK for {eighth_hand.name}*****")
                                    eighth_hand.add_cash(2.5 * eighth_hand.bet)
                                    first_hand.account = eighth_hand.account
                                    first_hand.get_balance()
                                    eighth_hand.hand.clear()
                                    first_split = False
                                    break

                                # Computer's sixth card exposed
                                comp.computer_faceup()

                                # PLAYER'S SECOND HAND TURN
                                # Second hand makes sixth move
                                if eighth_split_time:
                                    response = eighth_hand.four_options()
                                else:
                                    response = eighth_hand.two_options()

                                answer = eighth_hand.player_action(dealer, response)

                                # To continue playing or exit game
                                first_hand.play_on()

                                # PLAYER HITS
                                if answer == 'hit':
                                    eighth_split_time = False
                                    continue

                                # PLAYER DOUBLES
                                elif answer == 'double':
                                    eighth_hand.ace_adjust()
                                    eighth_hand.view_hand()
                                    first_hand.account = eighth_hand.account
                                    first_hand.get_balance()
                                    break

                                elif answer == 'ask':
                                    continue

                                elif answer == 'wave':

                                    break

                                # PLAYER SURRENDERS
                                else:
                                    print(f"\n\n\t{eighth_hand.name} SURRENDERS!")
                                    eighth_hand.view_hand()
                                    first_hand.account = eighth_hand.account
                                    first_hand.get_balance()
                                    eighth_hand.hand.clear()
                                    eighth_hand.bet = 0
                                    break

                        elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) < 1):
                            ninth_hand.split_done(second_hand, first_hand)

                            # To continue playing or exit game
                            first_hand.play_on()


                            ninth_split_time = True

                            while True:

                                # Making the necessary adjustments
                                ninth_hand.ace_adjust()

                                # Check for BLACKJACK
                                # PLAYER SCORES A BLACKJACK
                                if  len(ninth_hand.hand) < 3 and (ninth_hand.card_sum == 21) and (comp.card_sum != 21):
                                    print(f"\n\t\t{ninth_hand.name} WINS!")
                                    ninth_hand.view_hand()
                                    print(f"\n\n\t\t*****BLACKJACK for {ninth_hand.name}*****")
                                    ninth_hand.add_cash(2.5 * ninth_hand.bet)
                                    first_hand.account = ninth_hand.account
                                    first_hand.get_balance()
                                    ninth_hand.hand.clear()
                                    first_split = False
                                    break

                                # Computer's sixth card exposed
                                comp.computer_faceup()

                                # PLAYER'S SECOND HAND TURN
                                # Second hand makes sixth move
                                if ninth_split_time:
                                    response = ninth_hand.four_options()
                                else:
                                    response = ninth_hand.two_options()

                                answer = ninth_hand.player_action(dealer, response)

                                # To continue playing or exit game
                                first_hand.play_on()

                                # PLAYER HITS
                                if answer == 'hit':
                                    ninth_split_time = False
                                    continue

                                # PLAYER DOUBLES
                                elif answer == 'double':
                                    ninth_hand.ace_adjust()
                                    ninth_hand.view_hand()
                                    first_hand.account = ninth_hand.account
                                    first_hand.get_balance()
                                    break

                                elif answer == 'ask':
                                    continue

                                elif answer == 'wave':

                                    break

                                # PLAYER SURRENDERS
                                else:
                                    print(f"\n\n\t{ninth_hand.name} SURRENDERS!")
                                    ninth_hand.view_hand()
                                    first_hand.account = ninth_hand.account
                                    first_hand.get_balance()
                                    ninth_hand.hand.clear()
                                    ninth_hand.bet = 0
                                    break

                        elif (len(tenth_hand) < 1) and (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) > 0):
                            tenth_hand.split_done(second_hand, first_hand)

                            # To continue playing or exit game
                            first_hand.play_on()


                            tenth_split_time = True

                            while True:

                                # Making the necessary adjustments
                                tenth_hand.ace_adjust()

                                # Check for BLACKJACK
                                # PLAYER SCORES A BLACKJACK
                                if  len(tenth_hand.hand) < 3 and (tenth_hand.card_sum == 21) and (comp.card_sum != 21):
                                    print(f"\n\t\t{tenth_hand.name} WINS!")
                                    tenth_hand.view_hand()
                                    print(f"\n\n\t\t*****BLACKJACK for {tenth_hand.name}*****")
                                    tenth_hand.add_cash(2.5 * tenth_hand.bet)
                                    first_hand.account = tenth_hand.account
                                    first_hand.get_balance()
                                    tenth_hand.hand.clear()
                                    first_split = False
                                    break

                                # Computer's sixth card exposed
                                comp.computer_faceup()

                                # PLAYER'S SECOND HAND TURN
                                # Second hand makes sixth move
                                if tenth_split_time:
                                    response = tenth_hand.four_options()
                                else:
                                    response = tenth_hand.two_options()

                                answer = tenth_hand.player_action(dealer, response)

                                # To continue playing or exit game
                                first_hand.play_on()

                                # PLAYER HITS
                                if answer == 'hit':
                                    tenth_split_time = False
                                    continue

                                # PLAYER DOUBLES
                                elif answer == 'double':
                                    tenth_hand.ace_adjust()
                                    tenth_hand.view_hand()
                                    first_hand.account = tenth_hand.account
                                    first_hand.get_balance()
                                    break

                                elif answer == 'ask':
                                    continue

                                elif answer == 'wave':
                                    break

                                # PLAYER SURRENDERS
                                else:
                                    print(f"\n\n\t{tenth_hand.name} SURRENDERS!")
                                    tenth_hand.view_hand()
                                    first_hand.account = tenth_hand.account
                                    first_hand.get_balance()
                                    tenth_hand.hand.clear()
                                    tenth_hand.bet = 0
                                    break

                    third_hand.split_done(second_hand, first_hand)

                    # To continue playing or exit game
                    first_hand.play_on()


                    second_split_time = True

                    while True:

                        # Making the necessary adjustments
                        third_hand.ace_adjust()

                        # Check for BLACKJACK
                        # PLAYER SCORES A BLACKJACK
                        if  len(third_hand.hand) < 3 and (third_hand.card_sum == 21) and (comp.card_sum != 21):
                            print(f"\n\t\t{third_hand.name} WINS!")
                            third_hand.view_hand()
                            print(f"\n\n\t\t*****BLACKJACK for {third_hand.name}*****")
                            third_hand.add_cash(2.5 * third_hand.bet)
                            first_hand.account = third_hand.account
                            first_hand.get_balance()
                            third_hand.hand.clear()
                            second_split = False
                            break

                        # Check second hand for matching card occurrence
                        third_split = third_hand.split()

                        # Player splits for the first time
                        while third_split:

                            if len(fourth_hand.hand) > 0:
                                if len(seventh_hand.hand) < 1:
                                    seventh_hand.split_done(third_hand, first_hand)

                                    # To continue playing or exit game
                                    first_hand.play_on()


                                    seventh_split_time = True

                                    while True:

                                        # Making the necessary adjustments
                                        seventh_hand.ace_adjust()

                                        # Check for BLACKJACK
                                        # PLAYER SCORES A BLACKJACK
                                        if  len(seventh_hand.hand) < 3 and (seventh_hand.card_sum == 21) and (comp.card_sum != 21):
                                            print(f"\n\t\t{seventh_hand.name} WINS!")
                                            seventh_hand.view_hand()
                                            print(f"\n\n\t\t*****BLACKJACK for {seventh_hand.name}*****")
                                            seventh_hand.add_cash(2.5 * seventh_hand.bet)
                                            first_hand.account = seventh_hand.account
                                            first_hand.get_balance()
                                            seventh_hand.hand.clear()
                                            first_split = False
                                            break

                                        # Computer's sixth card exposed
                                        comp.computer_faceup()

                                        # PLAYER'S SECOND HAND TURN
                                        # Second hand makes sixth move
                                        if seventh_split_time:
                                            response = seventh_hand.four_options()
                                        else:
                                            response = seventh_hand.two_options()

                                        answer = seventh_hand.player_action(dealer, response)

                                        # To continue playing or exit game
                                        first_hand.play_on()

                                        # PLAYER HITS
                                        if answer == 'hit':
                                            seventh_split_time = False
                                            continue

                                        # PLAYER DOUBLES
                                        elif answer == 'double':
                                            seventh_hand.ace_adjust()
                                            seventh_hand.view_hand()
                                            first_hand.account = seventh_hand.account
                                            first_hand.get_balance()
                                            break

                                        elif answer == 'ask':
                                            continue

                                        elif answer == 'wave':
                                            break

                                        # PLAYER SURRENDERS
                                        else:
                                            print(f"\n\n\t{seventh_hand.name} SURRENDERS!")
                                            seventh_hand.view_hand()
                                            first_hand.account = seventh_hand.account
                                            first_hand.get_balance()
                                            seventh_hand.hand.clear()
                                            seventh_hand.bet = 0
                                            break


                                elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) < 1):
                                    eighth_hand.split_done(third_hand, first_hand)

                                    # To continue playing or exit game
                                    first_hand.play_on()


                                    eighth_split_time = True

                                    while True:

                                        # Making the necessary adjustments
                                        eighth_hand.ace_adjust()

                                        # Check for BLACKJACK
                                        # PLAYER SCORES A BLACKJACK
                                        if  len(eighth_hand.hand) < 3 and (eighth_hand.card_sum == 21) and (comp.card_sum != 21):
                                            print(f"\n\t\t{eighth_hand.name} WINS!")
                                            eighth_hand.view_hand()
                                            print(f"\n\n\t\t*****BLACKJACK for {eighth_hand.name}*****")
                                            eighth_hand.add_cash(2.5 * eighth_hand.bet)
                                            first_hand.account = eighth_hand.account
                                            first_hand.get_balance()
                                            eighth_hand.hand.clear()
                                            first_split = False
                                            break

                                        # Computer's sixth card exposed
                                        comp.computer_faceup()

                                        # PLAYER'S SECOND HAND TURN
                                        # Second hand makes sixth move
                                        if eighth_split_time:
                                            response = eighth_hand.four_options()
                                        else:
                                            response = eighth_hand.two_options()

                                        answer = eighth_hand.player_action(dealer, response)

                                        # To continue playing or exit game
                                        first_hand.play_on()

                                        # PLAYER HITS
                                        if answer == 'hit':
                                            eighth_split_time = False
                                            continue

                                        # PLAYER DOUBLES
                                        elif answer == 'double':
                                            eighth_hand.ace_adjust()
                                            eighth_hand.view_hand()
                                            first_hand.account = eighth_hand.account
                                            first_hand.get_balance()
                                            break

                                        elif answer == 'ask':
                                            continue

                                        elif answer == 'wave':
                                            break

                                        # PLAYER SURRENDERS
                                        else:
                                            print(f"\n\n\t{eighth_hand.name} SURRENDERS!")
                                            eighth_hand.view_hand()
                                            first_hand.account = eighth_hand.account
                                            first_hand.get_balance()
                                            eighth_hand.hand.clear()
                                            eighth_hand.bet = 0
                                            break

                                elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) < 1):
                                    ninth_hand.split_done(third_hand, first_hand)

                                    # To continue playing or exit game
                                    first_hand.play_on()


                                    ninth_split_time = True

                                    while True:

                                        # Making the necessary adjustments
                                        ninth_hand.ace_adjust()

                                        # Check for BLACKJACK
                                        # PLAYER SCORES A BLACKJACK
                                        if  len(ninth_hand.hand) < 3 and (ninth_hand.card_sum == 21) and (comp.card_sum != 21):
                                            print(f"\n\t\t{ninth_hand.name} WINS!")
                                            ninth_hand.view_hand()
                                            print(f"\n\n\t\t*****BLACKJACK for {ninth_hand.name}*****")
                                            ninth_hand.add_cash(2.5 * ninth_hand.bet)
                                            first_hand.account = ninth_hand.account
                                            first_hand.get_balance()
                                            ninth_hand.hand.clear()
                                            first_split = False
                                            break

                                        # Computer's sixth card exposed
                                        comp.computer_faceup()

                                        # PLAYER'S SECOND HAND TURN
                                        # Second hand makes sixth move
                                        if ninth_split_time:
                                            response = ninth_hand.four_options()
                                        else:
                                            response = ninth_hand.two_options()

                                        answer = ninth_hand.player_action(dealer, response)

                                        # To continue playing or exit game
                                        first_hand.play_on()

                                        # PLAYER HITS
                                        if answer == 'hit':
                                            ninth_split_time = False
                                            continue

                                        # PLAYER DOUBLES
                                        elif answer == 'double':
                                            ninth_hand.ace_adjust()
                                            ninth_hand.view_hand()
                                            first_hand.account = ninth_hand.account
                                            first_hand.get_balance()
                                            break

                                        elif answer == 'ask':
                                            continue

                                        elif answer == 'wave':
                                            break

                                        # PLAYER SURRENDERS
                                        else:
                                            print(f"\n\n\t{ninth_hand.name} SURRENDERS!")
                                            ninth_hand.view_hand()
                                            first_hand.account = ninth_hand.account
                                            first_hand.get_balance()
                                            ninth_hand.hand.clear()
                                            ninth_hand.bet = 0
                                            break

                                elif (len(tenth_hand) < 1) and (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) > 0):
                                    tenth_hand.split_done(third_hand, first_hand)

                                    # To continue playing or exit game
                                    first_hand.play_on()

                                    tenth_split_time = True

                                    while True:

                                        # Making the necessary adjustments
                                        tenth_hand.ace_adjust()

                                        # Check for BLACKJACK
                                        # PLAYER SCORES A BLACKJACK
                                        if  len(tenth_hand.hand) < 3 and (tenth_hand.card_sum == 21) and (comp.card_sum != 21):
                                            print(f"\n\t\t{tenth_hand.name} WINS!")
                                            tenth_hand.view_hand()
                                            print(f"\n\n\t\t*****BLACKJACK for {tenth_hand.name}*****")
                                            tenth_hand.add_cash(2.5 * tenth_hand.bet)
                                            first_hand.account = tenth_hand.account
                                            first_hand.get_balance()
                                            tenth_hand.hand.clear()
                                            first_split = False
                                            break

                                        # Computer's sixth card exposed
                                        comp.computer_faceup()

                                        # PLAYER'S SECOND HAND TURN
                                        # Second hand makes sixth move
                                        if tenth_split_time:
                                            response = tenth_hand.four_options()
                                        else:
                                            response = tenth_hand.two_options()

                                        answer = tenth_hand.player_action(dealer, response)

                                        # To continue playing or exit game
                                        first_hand.play_on()

                                        # PLAYER HITS
                                        if answer == 'hit':
                                            tenth_split_time = False
                                            continue

                                        # PLAYER DOUBLES
                                        elif answer == 'double':
                                            tenth_hand.ace_adjust()
                                            tenth_hand.view_hand()
                                            first_hand.account = tenth_hand.account
                                            first_hand.get_balance()
                                            break

                                        elif answer == 'ask':
                                            continue

                                        elif answer == 'wave':
                                            break

                                        # PLAYER SURRENDERS
                                        else:
                                            print(f"\n\n\t{tenth_hand.name} SURRENDERS!")
                                            tenth_hand.view_hand()
                                            first_hand.account = tenth_hand.account
                                            first_hand.get_balance()
                                            tenth_hand.hand.clear()
                                            tenth_hand.bet = 0
                                            break


                            fourth_hand.split_done(third_hand, first_hand)

                            # To continue playing or exit game
                            first_hand.play_on()


                            third_split_time = True

                            while True:

                                # Making the necessary adjustments
                                fourth_hand.ace_adjust()

                                # Check for BLACKJACK
                                # PLAYER SCORES A BLACKJACK
                                if  len(fourth_hand.hand) < 3 and (fourth_hand.card_sum == 21) and (comp.card_sum != 21):
                                    print(f"\n\t\t{fourth_hand.name} WINS!")
                                    fourth_hand.view_hand()
                                    print(f"\n\n\t\t*****BLACKJACK for {fourth_hand.name}*****")
                                    fourth_hand.add_cash(2.5 * fourth_hand.bet)
                                    first_hand.account = fourth_hand.account
                                    first_hand.get_balance()
                                    fourth_hand.hand.clear()
                                    third_split = False
                                    break

                                # Check second hand for matching card occurrence
                                fourth_split = fourth_hand.split()

                                # Player splits for the first time
                                while fourth_split:

                                    if len(fifth_hand.hand) > 0:
                                        if len(seventh_hand.hand) < 1:
                                            seventh_hand.split_done(fourth_hand, first_hand)

                                            # To continue playing or exit game
                                            first_hand.play_on()

                                            seventh_split_time = True

                                            while True:

                                                # Making the necessary adjustments
                                                seventh_hand.ace_adjust()

                                                # Check for BLACKJACK
                                                # PLAYER SCORES A BLACKJACK
                                                if  len(seventh_hand.hand) < 3 and (seventh_hand.card_sum == 21) and (comp.card_sum != 21):
                                                    print(f"\n\t\t{seventh_hand.name} WINS!")
                                                    seventh_hand.view_hand()
                                                    print(f"\n\n\t\t*****BLACKJACK for {seventh_hand.name}*****")
                                                    seventh_hand.add_cash(2.5 * seventh_hand.bet)
                                                    first_hand.account = seventh_hand.account
                                                    first_hand.get_balance()
                                                    seventh_hand.hand.clear()
                                                    first_split = False
                                                    break

                                                # Computer's sixth card exposed
                                                comp.computer_faceup()

                                                # PLAYER'S SECOND HAND TURN
                                                # Second hand makes sixth move
                                                if seventh_split_time:
                                                    response = seventh_hand.four_options()
                                                else:
                                                    response = seventh_hand.two_options()

                                                answer = seventh_hand.player_action(dealer, response)

                                                # To continue playing or exit game
                                                first_hand.play_on()

                                                # PLAYER HITS
                                                if answer == 'hit':
                                                    seventh_split_time = False
                                                    continue

                                                # PLAYER DOUBLES
                                                elif answer == 'double':
                                                    seventh_hand.ace_adjust()
                                                    seventh_hand.view_hand()
                                                    first_hand.account = seventh_hand.account
                                                    first_hand.get_balance()
                                                    break

                                                elif answer == 'ask':
                                                    continue

                                                elif answer == 'wave':
                                                    break

                                                # PLAYER SURRENDERS
                                                else:
                                                    print(f"\n\n\t{seventh_hand.name} SURRENDERS!")
                                                    seventh_hand.view_hand()
                                                    first_hand.account = seventh_hand.account
                                                    first_hand.get_balance()
                                                    seventh_hand.hand.clear()
                                                    seventh_hand.bet = 0
                                                    break


                                        elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) < 1):
                                            eighth_hand.split_done(fourth_hand, first_hand)

                                            # To continue playing or exit game
                                            first_hand.play_on()


                                            eighth_split_time = True

                                            while True:

                                                # Making the necessary adjustments
                                                eighth_hand.ace_adjust()

                                                # Check for BLACKJACK
                                                # PLAYER SCORES A BLACKJACK
                                                if  len(eighth_hand.hand) < 3 and (eighth_hand.card_sum == 21) and (comp.card_sum != 21):
                                                    print(f"\n\t\t{eighth_hand.name} WINS!")
                                                    eighth_hand.view_hand()
                                                    print(f"\n\n\t\t*****BLACKJACK for {eighth_hand.name}*****")
                                                    eighth_hand.add_cash(2.5 * eighth_hand.bet)
                                                    first_hand.account = eighth_hand.account
                                                    first_hand.get_balance()
                                                    eighth_hand.hand.clear()
                                                    first_split = False
                                                    break

                                                # Computer's sixth card exposed
                                                comp.computer_faceup()

                                                # PLAYER'S SECOND HAND TURN
                                                # Second hand makes sixth move
                                                if eighth_split_time:
                                                    response = eighth_hand.four_options()
                                                else:
                                                    response = eighth_hand.two_options()

                                                answer = eighth_hand.player_action(dealer, response)

                                                # To continue playing or exit game
                                                first_hand.play_on()

                                                # PLAYER HITS
                                                if answer == 'hit':
                                                    eighth_split_time = False
                                                    continue

                                                # PLAYER DOUBLES
                                                elif answer == 'double':
                                                    eighth_hand.ace_adjust()
                                                    eighth_hand.view_hand()
                                                    first_hand.account = eighth_hand.account
                                                    first_hand.get_balance()
                                                    break

                                                elif answer == 'ask':
                                                    continue

                                                elif answer == 'wave':
                                                    break

                                                # PLAYER SURRENDERS
                                                else:
                                                    print(f"\n\n\t{eighth_hand.name} SURRENDERS!")
                                                    eighth_hand.view_hand()
                                                    first_hand.account = eighth_hand.account
                                                    first_hand.get_balance()
                                                    eighth_hand.hand.clear()
                                                    eighth_hand.bet = 0
                                                    break

                                        elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) < 1):
                                            ninth_hand.split_done(fourth_hand, first_hand)

                                            # To continue playing or exit game
                                            first_hand.play_on()


                                            ninth_split_time = True

                                            while True:

                                                # Making the necessary adjustments
                                                ninth_hand.ace_adjust()

                                                # Check for BLACKJACK
                                                # PLAYER SCORES A BLACKJACK
                                                if  len(ninth_hand.hand) < 3 and (ninth_hand.card_sum == 21) and (comp.card_sum != 21):
                                                    print(f"\n\t\t{ninth_hand.name} WINS!")
                                                    ninth_hand.view_hand()
                                                    print(f"\n\n\t\t*****BLACKJACK for {ninth_hand.name}*****")
                                                    ninth_hand.add_cash(2.5 * ninth_hand.bet)
                                                    first_hand.account = ninth_hand.account
                                                    first_hand.get_balance()
                                                    ninth_hand.hand.clear()
                                                    first_split = False
                                                    break

                                                # Computer's sixth card exposed
                                                comp.computer_faceup()

                                                # PLAYER'S SECOND HAND TURN
                                                # Second hand makes sixth move
                                                if ninth_split_time:
                                                    response = ninth_hand.four_options()
                                                else:
                                                    response = ninth_hand.two_options()

                                                answer = ninth_hand.player_action(dealer, response)

                                                # To continue playing or exit game
                                                first_hand.play_on()

                                                # PLAYER HITS
                                                if answer == 'hit':
                                                    ninth_split_time = False
                                                    continue

                                                # PLAYER DOUBLES
                                                elif answer == 'double':
                                                    ninth_hand.ace_adjust()
                                                    ninth_hand.view_hand()
                                                    first_hand.account = ninth_hand.account
                                                    first_hand.get_balance()
                                                    break

                                                elif answer == 'ask':
                                                    continue

                                                elif answer == 'wave':
                                                    break

                                                # PLAYER SURRENDERS
                                                else:
                                                    print(f"\n\n\t{ninth_hand.name} SURRENDERS!")
                                                    ninth_hand.view_hand()
                                                    first_hand.account = ninth_hand.account
                                                    first_hand.get_balance()
                                                    ninth_hand.hand.clear()
                                                    ninth_hand.bet = 0
                                                    break

                                        elif (len(tenth_hand) < 1) and (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) > 0):
                                            tenth_hand.split_done(fourth_hand, first_hand)

                                            # To continue playing or exit game
                                            first_hand.play_on()


                                            tenth_split_time = True

                                            while True:

                                                # Making the necessary adjustments
                                                tenth_hand.ace_adjust()

                                                # Check for BLACKJACK
                                                # PLAYER SCORES A BLACKJACK
                                                if  len(tenth_hand.hand) < 3 and (tenth_hand.card_sum == 21) and (comp.card_sum != 21):
                                                    print(f"\n\t\t{tenth_hand.name} WINS!")
                                                    tenth_hand.view_hand()
                                                    print(f"\n\n\t\t*****BLACKJACK for {tenth_hand.name}*****")
                                                    tenth_hand.add_cash(2.5 * tenth_hand.bet)
                                                    first_hand.account = tenth_hand.account
                                                    first_hand.get_balance()
                                                    tenth_hand.hand.clear()
                                                    first_split = False
                                                    break

                                                # Computer's sixth card exposed
                                                comp.computer_faceup()

                                                # PLAYER'S SECOND HAND TURN
                                                # Second hand makes sixth move
                                                if tenth_split_time:
                                                    response = tenth_hand.four_options()
                                                else:
                                                    response = tenth_hand.two_options()

                                                answer = tenth_hand.player_action(dealer, response)

                                                # To continue playing or exit game
                                                first_hand.play_on()

                                                # PLAYER HITS
                                                if answer == 'hit':
                                                    tenth_split_time = False
                                                    continue

                                                # PLAYER DOUBLES
                                                elif answer == 'double':
                                                    tenth_hand.ace_adjust()
                                                    tenth_hand.view_hand()
                                                    first_hand.account = tenth_hand.account
                                                    first_hand.get_balance()
                                                    break

                                                elif answer == 'ask':
                                                    continue

                                                elif answer == 'wave':
                                                    break

                                                # PLAYER SURRENDERS
                                                else:
                                                    print(f"\n\n\t{tenth_hand.name} SURRENDERS!")
                                                    tenth_hand.view_hand()
                                                    first_hand.account = tenth_hand.account
                                                    first_hand.get_balance()
                                                    tenth_hand.hand.clear()
                                                    tenth_hand.bet = 0
                                                    break


                                    fifth_hand.split_done(fourth_hand, first_hand)

                                    # To continue playing or exit game
                                    first_hand.play_on()

                                    fourth_split_time = True

                                    while True:

                                        # Making the necessary adjustments
                                        fifth_hand.ace_adjust()

                                        # Check for BLACKJACK
                                        # PLAYER SCORES A BLACKJACK
                                        if  len(fifth_hand.hand) < 3 and (fifth_hand.card_sum == 21) and (comp.card_sum != 21):
                                            print(f"\n\t\t{fifth_hand.name} WINS!")
                                            fifth_hand.view_hand()
                                            print(f"\n\n\t\t*****BLACKJACK for {fifth_hand.name}*****")
                                            fifth_hand.add_cash(2.5 * fifth_hand.bet)
                                            first_hand.account = fifth_hand.account
                                            first_hand.get_balance()
                                            fifth_hand.hand.clear()
                                            fourth_split = False
                                            break

                                        # Check second hand for matching card occurrence
                                        fifth_split = fifth_hand.split()

                                        # Player splits for the first time
                                        while fifth_split:

                                            if len(sixth_hand.hand) > 0:
                                                if len(seventh_hand.hand) < 1:
                                                    seventh_hand.split_done(fifth_hand, first_hand)

                                                    # To continue playing or exit game
                                                    first_hand.play_on()


                                                    seventh_split_time = True

                                                    while True:

                                                        # Making the necessary adjustments
                                                        seventh_hand.ace_adjust()

                                                        # Check for BLACKJACK
                                                        # PLAYER SCORES A BLACKJACK
                                                        if  len(seventh_hand.hand) < 3 and (seventh_hand.card_sum == 21) and (comp.card_sum != 21):
                                                            print(f"\n\t\t{seventh_hand.name} WINS!")
                                                            seventh_hand.view_hand()
                                                            print(f"\n\n\t\t*****BLACKJACK for {seventh_hand.name}*****")
                                                            seventh_hand.add_cash(2.5 * seventh_hand.bet)
                                                            first_hand.account = seventh_hand.account
                                                            first_hand.get_balance()
                                                            seventh_hand.hand.clear()
                                                            first_split = False
                                                            break

                                                        # Computer's sixth card exposed
                                                        comp.computer_faceup()

                                                        # PLAYER'S SECOND HAND TURN
                                                        # Second hand makes sixth move
                                                        if seventh_split_time:
                                                            response = seventh_hand.four_options()
                                                        else:
                                                            response = seventh_hand.two_options()

                                                        answer = seventh_hand.player_action(dealer, response)

                                                        # To continue playing or exit game
                                                        first_hand.play_on()

                                                        # PLAYER HITS
                                                        if answer == 'hit':
                                                            seventh_split_time = False
                                                            continue

                                                        # PLAYER DOUBLES
                                                        elif answer == 'double':
                                                            seventh_hand.ace_adjust()
                                                            seventh_hand.view_hand()
                                                            first_hand.account = seventh_hand.account
                                                            first_hand.get_balance()
                                                            break

                                                        elif answer == 'ask':
                                                            continue

                                                        elif answer == 'wave':
                                                            break

                                                        # PLAYER SURRENDERS
                                                        else:
                                                            print(f"\n\n\t{seventh_hand.name} SURRENDERS!")
                                                            seventh_hand.view_hand()
                                                            first_hand.account = seventh_hand.account
                                                            first_hand.get_balance()
                                                            seventh_hand.hand.clear()
                                                            seventh_hand.bet = 0
                                                            break


                                                elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) < 1):
                                                    eighth_hand.split_done(fifth_hand, first_hand)

                                                    # To continue playing or exit game
                                                    first_hand.play_on()


                                                    eighth_split_time = True

                                                    while True:

                                                        # Making the necessary adjustments
                                                        eighth_hand.ace_adjust()

                                                        # Check for BLACKJACK
                                                        # PLAYER SCORES A BLACKJACK
                                                        if  len(eighth_hand.hand) < 3 and (eighth_hand.card_sum == 21) and (comp.card_sum != 21):
                                                            print(f"\n\t\t{eighth_hand.name} WINS!")
                                                            eighth_hand.view_hand()
                                                            print(f"\n\n\t\t*****BLACKJACK for {eighth_hand.name}*****")
                                                            eighth_hand.add_cash(2.5 * eighth_hand.bet)
                                                            first_hand.account = eighth_hand.account
                                                            first_hand.get_balance()
                                                            eighth_hand.hand.clear()
                                                            first_split = False
                                                            break

                                                        # Computer's sixth card exposed
                                                        comp.computer_faceup()

                                                        # PLAYER'S SECOND HAND TURN
                                                        # Second hand makes sixth move
                                                        if eighth_split_time:
                                                            response = eighth_hand.four_options()
                                                        else:
                                                            response = eighth_hand.two_options()

                                                        answer = eighth_hand.player_action(dealer, response)

                                                        # To continue playing or exit game
                                                        first_hand.play_on()

                                                        # PLAYER HITS
                                                        if answer == 'hit':
                                                            eighth_split_time = False
                                                            continue

                                                        # PLAYER DOUBLES
                                                        elif answer == 'double':
                                                            eighth_hand.ace_adjust()
                                                            eighth_hand.view_hand()
                                                            first_hand.account = eighth_hand.account
                                                            first_hand.get_balance()
                                                            break

                                                        elif answer == 'ask':
                                                            continue

                                                        elif answer == 'wave':
                                                            break

                                                        # PLAYER SURRENDERS
                                                        else:
                                                            print(f"\n\n\t{eighth_hand.name} SURRENDERS!")
                                                            eighth_hand.view_hand()
                                                            first_hand.account = eighth_hand.account
                                                            first_hand.get_balance()
                                                            eighth_hand.hand.clear()
                                                            eighth_hand.bet = 0
                                                            break

                                                elif (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) < 1):
                                                    ninth_hand.split_done(fifth_hand, first_hand)

                                                    # To continue playing or exit game
                                                    first_hand.play_on()


                                                    ninth_split_time = True

                                                    while True:

                                                        # Making the necessary adjustments
                                                        ninth_hand.ace_adjust()

                                                        # Check for BLACKJACK
                                                        # PLAYER SCORES A BLACKJACK
                                                        if  len(ninth_hand.hand) < 3 and (ninth_hand.card_sum == 21) and (comp.card_sum != 21):
                                                            print(f"\n\t\t{ninth_hand.name} WINS!")
                                                            ninth_hand.view_hand()
                                                            print(f"\n\n\t\t*****BLACKJACK for {ninth_hand.name}*****")
                                                            ninth_hand.add_cash(2.5 * ninth_hand.bet)
                                                            first_hand.account = ninth_hand.account
                                                            first_hand.get_balance()
                                                            ninth_hand.hand.clear()
                                                            first_split = False
                                                            break

                                                        # Computer's sixth card exposed
                                                        comp.computer_faceup()

                                                        # PLAYER'S SECOND HAND TURN
                                                        # Second hand makes sixth move
                                                        if ninth_split_time:
                                                            response = ninth_hand.four_options()
                                                        else:
                                                            response = ninth_hand.two_options()

                                                        answer = ninth_hand.player_action(dealer, response)

                                                        # To continue playing or exit game
                                                        first_hand.play_on()

                                                        # PLAYER HITS
                                                        if answer == 'hit':
                                                            ninth_split_time = False
                                                            continue

                                                        # PLAYER DOUBLES
                                                        elif answer == 'double':
                                                            ninth_hand.ace_adjust()
                                                            ninth_hand.view_hand()
                                                            first_hand.account = ninth_hand.account
                                                            first_hand.get_balance()
                                                            break

                                                        elif answer == 'ask':
                                                            continue

                                                        elif answer == 'wave':
                                                            break

                                                        # PLAYER SURRENDERS
                                                        else:
                                                            print(f"\n\n\t{ninth_hand.name} SURRENDERS!")
                                                            ninth_hand.view_hand()
                                                            first_hand.account = ninth_hand.account
                                                            first_hand.get_balance()
                                                            ninth_hand.hand.clear()
                                                            ninth_hand.bet = 0
                                                            break

                                                elif (len(tenth_hand) < 1) and (len(seventh_hand.hand) > 0) and (len(eighth_hand) > 0) and (len(ninth_hand) > 0):
                                                    tenth_hand.split_done(fifth_hand, first_hand)

                                                    # To continue playing or exit game
                                                    first_hand.play_on()


                                                    tenth_split_time = True

                                                    while True:

                                                        # Making the necessary adjustments
                                                        tenth_hand.ace_adjust()

                                                        # Check for BLACKJACK
                                                        # PLAYER SCORES A BLACKJACK
                                                        if  len(tenth_hand.hand) < 3 and (tenth_hand.card_sum == 21) and (comp.card_sum != 21):
                                                            print(f"\n\t\t{tenth_hand.name} WINS!")
                                                            tenth_hand.view_hand()
                                                            print(f"\n\n\t\t*****BLACKJACK for {tenth_hand.name}*****")
                                                            tenth_hand.add_cash(2.5 * tenth_hand.bet)
                                                            first_hand.account = tenth_hand.account
                                                            first_hand.get_balance()
                                                            tenth_hand.hand.clear()
                                                            first_split = False
                                                            break

                                                        # Computer's sixth card exposed
                                                        comp.computer_faceup()

                                                        # PLAYER'S SECOND HAND TURN
                                                        # Second hand makes sixth move
                                                        if tenth_split_time:
                                                            response = tenth_hand.four_options()
                                                        else:
                                                            response = tenth_hand.two_options()

                                                        answer = tenth_hand.player_action(dealer, response)

                                                        # To continue playing or exit game
                                                        first_hand.play_on()

                                                        # PLAYER HITS
                                                        if answer == 'hit':
                                                            tenth_split_time = False
                                                            continue

                                                        # PLAYER DOUBLES
                                                        elif answer == 'double':
                                                            tenth_hand.ace_adjust()
                                                            tenth_hand.view_hand()
                                                            first_hand.account = tenth_hand.account
                                                            first_hand.get_balance()
                                                            break

                                                        elif answer == 'ask':
                                                            continue

                                                        elif answer == 'wave':
                                                            break

                                                        # PLAYER SURRENDERS
                                                        else:
                                                            print(f"\n\n\t{tenth_hand.name} SURRENDERS!")
                                                            tenth_hand.view_hand()
                                                            first_hand.account = tenth_hand.account
                                                            first_hand.get_balance()
                                                            tenth_hand.hand.clear()
                                                            tenth_hand.bet = 0
                                                            break


                                            sixth_hand.split_done(fifth_hand, first_hand)

                                            # To continue playing or exit game
                                            first_hand.play_on()


                                            fifth_split_time = True

                                            while True:

                                                # Making the necessary adjustments
                                                sixth_hand.ace_adjust()

                                                # Check for BLACKJACK
                                                # PLAYER SCORES A BLACKJACK
                                                if  len(sixth_hand.hand) < 3 and (sixth_hand.card_sum == 21) and (comp.card_sum != 21):
                                                    print(f"\n\t\t{sixth_hand.name} WINS!")
                                                    sixth_hand.view_hand()
                                                    print(f"\n\n\t\t*****BLACKJACK for {sixth_hand.name}*****")
                                                    sixth_hand.add_cash(2.5 * sixth_hand.bet)
                                                    first_hand.account = sixth_hand.account
                                                    first_hand.get_balance()
                                                    sixth_hand.hand.clear()
                                                    fifth_split = False
                                                    break

                                                # Computer's sixth card exposed
                                                comp.computer_faceup()

                                                # PLAYER'S SECOND HAND TURN
                                                # Second hand makes sixth move
                                                if fifth_split_time:
                                                    response = sixth_hand.four_options()
                                                else:
                                                    response = sixth_hand.two_options()

                                                answer = sixth_hand.player_action(dealer, response)

                                                # To continue playing or exit game
                                                first_hand.play_on()

                                                # PLAYER HITS
                                                if answer == 'hit':
                                                    fifth_split_time = False
                                                    continue

                                                # PLAYER DOUBLES
                                                elif answer == 'double':
                                                    sixth_hand.ace_adjust()
                                                    sixth_hand.view_hand()
                                                    first_hand.account = sixth_hand.account
                                                    first_hand.get_balance()
                                                    fifth_split = False
                                                    break

                                                elif answer == 'ask':
                                                    continue

                                                elif answer == 'wave':
                                                    fifth_split = False
                                                    break

                                                # PLAYER SURRENDERS
                                                else:
                                                    print(f"\n\n\t{sixth_hand.name} SURRENDERS!")
                                                    sixth_hand.view_hand()
                                                    first_hand.account = sixth_hand.account
                                                    first_hand.get_balance()
                                                    fifth_split = False
                                                    sixth_hand.hand.clear()
                                                    sixth_hand.bet = 0
                                                    break

                                        # Computer's fifth card exposed
                                        comp.computer_faceup()

                                        # PLAYER'S SECOND HAND TURN
                                        # Second hand makes fifth move
                                        if fourth_split_time:
                                            response = fifth_hand.four_options()
                                        else:
                                            response = fifth_hand.two_options()

                                        answer = fifth_hand.player_action(dealer, response)

                                        # To continue playing or exit game
                                        first_hand.play_on()

                                        # PLAYER HITS
                                        if answer == 'hit':
                                            fourth_split_time = False
                                            continue

                                        # PLAYER DOUBLES
                                        elif answer == 'double':
                                            fifth_hand.ace_adjust()
                                            fifth_hand.view_hand()
                                            first_hand.account = fifth_hand.account
                                            first_hand.get_balance()
                                            fourth_split = False
                                            break

                                        elif answer == 'ask':
                                            continue

                                        elif answer == 'wave':
                                            fourth_split = False
                                            break

                                        # PLAYER SURRENDERS
                                        else:
                                            print(f"\n\n\t{fifth_hand.name} SURRENDERS!")
                                            fifth_hand.view_hand()
                                            first_hand.account = fifth_hand.account
                                            first_hand.get_balance()
                                            fourth_split = False
                                            fifth_hand.hand.clear()
                                            fifth_hand.bet = 0
                                            break

                                # Computer's first card exposed
                                comp.computer_faceup()

                                # PLAYER'S SECOND HAND TURN
                                # Second hand makes first move
                                if third_split_time:
                                    response = fourth_hand.four_options()
                                else:
                                    response = fourth_hand.two_options()

                                answer = fourth_hand.player_action(dealer, response)

                                # To continue playing or exit game
                                first_hand.play_on()

                                # PLAYER HITS
                                if answer == 'hit':
                                    third_split_time = False
                                    continue

                                # PLAYER DOUBLES
                                elif answer == 'double':
                                    fourth_hand.ace_adjust()
                                    fourth_hand.view_hand()
                                    first_hand.account = fourth_hand.account
                                    first_hand.get_balance()
                                    third_split = False
                                    break

                                elif answer == 'ask':
                                    continue

                                elif answer == 'wave':
                                    third_split = False
                                    break

                                # PLAYER SURRENDERS
                                else:
                                    print(f"\n\n\t{fourth_hand.name} SURRENDERS!")
                                    fourth_hand.view_hand()
                                    first_hand.account = fourth_hand.account
                                    first_hand.get_balance()
                                    third_split = False
                                    fourth_hand.hand.clear()
                                    fourth_hand.bet = 0
                                    break

                        # Computer's third card exposed
                        comp.computer_faceup()

                        # PLAYER'S SECOND HAND TURN
                        # Second hand makes third move
                        if second_split_time:
                            response = third_hand.four_options()
                        else:
                            response = third_hand.two_options()

                        answer = third_hand.player_action(dealer, response)

                        # To continue playing or exit game
                        first_hand.play_on()

                        # PLAYER HITS
                        if answer == 'hit':
                            second_split_time = False
                            continue

                        # PLAYER DOUBLES
                        elif answer == 'double':
                            third_hand.ace_adjust()
                            third_hand.view_hand()
                            first_hand.account = third_hand.account
                            first_hand.get_balance()
                            second_split = False
                            break

                        elif answer == 'ask':
                            continue

                        # PLAY CONTINUES AFTER STAND OR DOUBLE
                        elif answer == 'wave':
                            second_split = False
                            break

                        # PLAYER SURRENDERS
                        # GAME RESTARTS DUE TO SURRENDER
                        else:
                            print(f"\n\n\t{third_hand.name} SURRENDERS!")
                            third_hand.view_hand()
                            first_hand.account = third_hand.account
                            first_hand.get_balance()
                            second_split = False
                            third_hand.hand.clear()
                            third_hand.bet = 0
                            break

                # Computer's second card exposed
                comp.computer_faceup()

                # PLAYER'S SECOND HAND TURN
                # Second hand makes second move
                if first_split_time:
                    response = second_hand.four_options()
                else:
                    response = second_hand.two_options()

                answer = second_hand.player_action(dealer, response)

                # To continue playing or exit game
                first_hand.play_on()

                # PLAYER HITS
                if answer == 'hit':
                    first_split_time = False
                    continue

                # PLAYER DOUBLES
                elif answer == 'double':
                    second_hand.ace_adjust()
                    second_hand.view_hand()
                    first_hand.account = second_hand.account
                    first_hand.get_balance()
                    first_split = False
                    break

                elif answer == 'ask':
                    continue

                elif answer == 'wave':
                    first_split = False
                    break

                # PLAYER SURRENDERS
                # GAME RESTARTS DUE TO SURRENDER
                else:
                    print(f"\n\n\t{second_hand.name} SURRENDERS!")
                    second_hand.view_hand()
                    first_hand.account = second_hand.account
                    first_hand.get_balance()
                    first_split = False
                    second_hand.hand.clear()
                    second_hand.bet = 0
                    break

        # To continue playing or exit game
        first_hand.play_on()

        # Computer's first card exposed
        comp.computer_faceup()

        # AFTER SPLIT TURNS
        if first_turn:
            response = first_hand.four_options()
        else:
            response = first_hand.two_options()


        answer = first_hand.player_action(dealer, response)

        # PLAYER HITS
        if answer == 'hit':
            first_turn = False
            continue

        # PLAYER DOUBLES
        elif answer == 'double':
            first_turn = False
            waiting = False

        elif answer == 'ask':
            continue

        elif answer == 'wave':
            first_turn = False
            waiting = False

        # PLAYER SURRENDERS
        # GAME RESTARTS DUE TO SURRENDER
        else:
            # EXPOSING PLAYER'S hand
            first_hand.hand.clear()
            first_hand.view_hand()
            comp.view_hand()
            first_turn = False
            waiting = False

        # Checking for presence of Aces in player's hand
        # Reduce the card total by 10 if ace is more than one
        first_hand.ace_adjust()


        # COMPUTER'S TURN:
        # CHECK IF COMPUTER'S CARD VALUE IS UP TO 17
        computer_turn = True
        while computer_turn:

            # Checking for presence of Aces in computer's hand
            # Reduce the card total by 10 * Number of aces (if ace is present)
            comp.ace_adjust()

            # Computer's hands get cleared if all of the player's hands are empty
            if len(first_hand.hand) < 1 and len(second_hand.hand) < 1 and len(third_hand.hand) < 1 and len(fourth_hand.hand) < 1 and len(fifth_hand.hand) < 1 and len(sixth_hand.hand) < 1 and len(seventh_hand.hand) < 1 and len(eighth_hand.hand) < 1 and len(ninth_hand.hand) < 1 and len(tenth_hand.hand) < 1:
                comp.hand.clear()
                break

            # Conditions for computer to hit or stand
            if comp.card_sum < 17:

                # When computer's card value is less than  17 and the opponent has a chance of winning the game
                if ((len(first_hand.hand) > 0) or (len(second_hand.hand) > 0) or (len(third_hand.hand) > 0) or (len(fourth_hand.hand) > 0) or (len(fifth_hand.hand) > 0) or (len(sixth_hand.hand) > 0) or (len(seventh_hand.hand) > 0) or (len(eighth_hand.hand) > 0) or (len(ninth_hand.hand) > 0) or (len(tenth_hand.hand) > 0)):
                    if ((first_hand.card_sum < 22) or (second_hand.card_sum < 22) or (third_hand.card_sum < 22) or (fourth_hand.card_sum < 22) or (fifth_hand.card_sum < 22) or (sixth_hand.card_sum < 22) or (seventh_hand.card_sum < 22) or (eighth_hand.card_sum < 22) or (ninth_hand.card_sum < 22) or (tenth_hand.card_sum < 22)):
                        comp.receive_card(dealer.deal_card())
                        continue

                # When computer has less than 17 and all the opponent's hands are lesser
            elif (first_hand.card_sum < comp.card_sum) and (second_hand.card_sum < comp.card_sum) and (third_hand.card_sum < comp.card_sum) and (fourth_hand.card_sum < comp.card_sum) and (fifth_hand.card_sum < comp.card_sum) and (sixth_hand.card_sum < comp.card_sum) and (seventh_hand.card_sum < comp.card_sum) and (eighth_hand.card_sum < comp.card_sum) and (ninth_hand.card_sum < comp.card_sum) and (tenth_hand.card_sum < comp.card_sum):
                print(f"\t{comp.name} WAVES!")
                computer_turn = False

            else:
                print(f"\t{comp.name} WAVES!")
                computer_turn = False


        first_hand.play_on()

        # WHEN PLAYER BUSTS
        if (len(tenth_hand.hand) != 0) and (tenth_hand.card_sum > 21):
            tenth_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{tenth_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {tenth_hand.name}")
            tenth_hand.hand.clear()
            tenth_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(ninth_hand.hand) != 0) and (ninth_hand.card_sum > 21):
            ninth_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{ninth_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {ninth_hand.name}")
            ninth_hand.hand.clear()
            ninth_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(eighth_hand.hand) != 0) and (eighth_hand.card_sum > 21):
            eighth_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{eighth_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {eighth_hand.name}")
            eighth_hand.hand.clear()
            eighth_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(seventh_hand.hand) != 0) and (seventh_hand.card_sum > 21):
            seventh_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{seventh_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {seventh_hand.name}")
            seventh_hand.hand.clear()
            seventh_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(sixth_hand.hand) != 0) and (sixth_hand.card_sum > 21):
            sixth_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{sixth_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {sixth_hand.name}")
            sixth_hand.hand.clear()
            sixth_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(fifth_hand.hand) != 0) and (fifth_hand.card_sum > 21):
            fifth_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{fifth_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {fifth_hand.name}")
            fifth_hand.hand.clear()
            fifth_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(fourth_hand.hand) != 0) and (fourth_hand.card_sum > 21):
            fourth_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{fourth_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {fourth_hand.name}")
            fourth_hand.hand.clear()
            fourth_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(third_hand.hand) != 0) and (third_hand.card_sum > 21):
            third_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{third_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {third_hand.name}")
            third_hand.hand.clear()
            third_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False

        if (len(second_hand.hand) != 0) and (second_hand.card_sum > 21):
            second_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{second_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {second_hand.name}")
            second_hand.hand.clear()
            second_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False


        if (len(first_hand.hand) != 0) and (first_hand.card_sum > 21):
            first_hand.view_hand()
            comp.view_hand()
            print(f"\n\n\t\t{first_hand.name} LOSES THE ROUND!")
            print(f"\n\t\tBUST for {first_hand.name}")
            first_hand.hand.clear()
            comp.hand.clear()
            first_hand.bet = 0
            if first_hand.account == 0:
                first_hand.get_balance()
                print(f"\n\t\t{first_hand.name} is OUT OF CASH!")
                print("\n\t\tGAME OVER!!!")
                game_on = False


        # WHEN COMPUTER BUSTS
        if comp.card_sum > 21:

            if (len(tenth_hand.hand) != 0) and (tenth_hand.card_sum < 22):
                tenth_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{tenth_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*tenth_hand.bet)
                tenth_hand.bet = 0
                first_hand.get_balance()
                tenth_hand.hand.clear()

            if (len(ninth_hand.hand) != 0) and (ninth_hand.card_sum < 22):
                ninth_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{ninth_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*ninth_hand.bet)
                ninth_hand.bet = 0
                first_hand.get_balance()
                ninth_hand.hand.clear()

            if (len(eighth_hand.hand) != 0) and (eighth_hand.card_sum < 22):
                eighth_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{eighth_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*eighth_hand.bet)
                eighth_hand.bet = 0
                first_hand.get_balance()
                eighth_hand.hand.clear()

            if (len(seventh_hand.hand) != 0) and (seventh_hand.card_sum < 22):
                seventh_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{seventh_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*seventh_hand.bet)
                seventh_hand.bet = 0
                first_hand.get_balance()
                seventh_hand.hand.clear()

            if (len(sixth_hand.hand) != 0) and (sixth_hand.card_sum < 22):
                sixth_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{sixth_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*sixth_hand.bet)
                sixth_hand.bet = 0
                first_hand.get_balance()
                sixth_hand.hand.clear()

            if (len(fifth_hand.hand) != 0) and (fifth_hand.card_sum < 22):
                fifth_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{fifth_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*fifth_hand.bet)
                fifth_hand.bet = 0
                first_hand.get_balance()
                fifth_hand.hand.clear()

            if (len(fourth_hand.hand) != 0) and (fourth_hand.card_sum < 22):
                fourth_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{fourth_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*fourth_hand.bet)
                fourth_hand.bet = 0
                first_hand.get_balance()
                fourth_hand.hand.clear()

            if (len(third_hand.hand) != 0) and (third_hand.card_sum < 22):
                third_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{third_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*third_hand.bet)
                third_hand.bet = 0
                first_hand.get_balance()
                third_hand.hand.clear()

            if (len(second_hand.hand) != 0) and (second_hand.card_sum < 22):
                second_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{second_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*second_hand.bet)
                second_hand.bet = 0
                first_hand.get_balance()
                second_hand.hand.clear()

            if (len(first_hand.hand) != 0) and (first_hand.card_sum < 22):
                first_hand.view_hand()
                comp.view_hand()
                print(f"\n\t\tBUST for {comp.name}")
                print(f"\n\t\t{first_hand.name} WINS THE ROUND!")
                first_hand.add_cash(2*first_hand.bet)
                first_hand.get_balance()
                first_hand.bet = 0
                first_hand.hand.clear()
                comp.hand.clear()


        # WHEN PLAYER HITS 21
        if comp.card_sum < 22:

            if (len(tenth_hand.hand) != 0) and (tenth_hand.card_sum == comp.card_sum):
                tenth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{tenth_hand.name} PUSH!!!")
                first_hand.add_cash(tenth_hand.bet)
                tenth_hand.hand.clear()
                tenth_hand.bet = 0
                first_hand.get_balance()

            if (len(ninth_hand.hand) != 0) and (ninth_hand.card_sum == comp.card_sum):
                ninth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{ninth_hand.name} PUSH!!!")
                first_hand.add_cash(ninth_hand.bet)
                ninth_hand.hand.clear()
                ninth_hand.bet = 0
                first_hand.get_balance()

            if (len(eighth_hand.hand) != 0) and (eighth_hand.card_sum == comp.card_sum):
                eighth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{eighth_hand.name} PUSH!!!")
                first_hand.add_cash(eighth_hand.bet)
                eighth_hand.hand.clear()
                eighth_hand.bet = 0
                first_hand.get_balance()

            if (len(seventh_hand.hand) != 0) and (seventh_hand.card_sum == comp.card_sum):
                seventh_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{seventh_hand.name} PUSH!!!")
                first_hand.add_cash(seventh_hand.bet)
                seventh_hand.hand.clear()
                seventh_hand.bet = 0
                first_hand.get_balance()

            if (len(sixth_hand.hand) != 0) and (sixth_hand.card_sum == comp.card_sum):
                sixth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{sixth_hand.name} PUSH!!!")
                first_hand.add_cash(sixth_hand.bet)
                sixth_hand.hand.clear()
                sixth_hand.bet = 0
                first_hand.get_balance()

            if (len(fifth_hand.hand) != 0) and (fifth_hand.card_sum == comp.card_sum):
                fifth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fifth_hand.name} PUSH!!!")
                first_hand.add_cash(fifth_hand.bet)
                fifth_hand.hand.clear()
                fifth_hand.bet = 0
                first_hand.get_balance()

            if (len(fourth_hand.hand) != 0) and (fourth_hand.card_sum == comp.card_sum):
                fourth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fourth_hand.name} PUSH!!!")
                first_hand.add_cash(fourth_hand.bet)
                fourth_hand.hand.clear()
                fourth_hand.bet = 0
                first_hand.get_balance()

            if (len(third_hand.hand) != 0) and (third_hand.card_sum == comp.card_sum):
                third_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{third_hand.name} PUSH!!!")
                first_hand.add_cash(third_hand.bet)
                third_hand.hand.clear()
                third_hand.bet = 0
                first_hand.get_balance()

            if (len(second_hand.hand) != 0) and (second_hand.card_sum == comp.card_sum):
                second_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{second_hand.name} PUSH!!!")
                first_hand.add_cash(second_hand.bet)
                second_hand.hand.clear()
                second_hand.bet = 0
                first_hand.get_balance()

            if (len(first_hand.hand) != 0) and (first_hand.card_sum == comp.card_sum):
                first_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{first_hand.name} PUSH!!!")
                first_hand.add_cash(first_hand.bet)
                first_hand.hand.clear()
                comp.hand.clear()
                first_hand.bet = 0
                first_hand.get_balance()



            if (len(tenth_hand.hand) != 0) and (tenth_hand.card_sum > comp.card_sum):
                tenth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{tenth_hand.name} WINS!")
                first_hand.add_cash(2 * tenth_hand.bet)
                tenth_hand.hand.clear()
                tenth_hand.bet = 0
                first_hand.get_balance()

            if (len(ninth_hand.hand) != 0) and (ninth_hand.card_sum > comp.card_sum):
                ninth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{ninth_hand.name} WINS!")
                first_hand.add_cash(2 * ninth_hand.bet)
                ninth_hand.hand.clear()
                ninth_hand.bet = 0
                first_hand.get_balance()

            if (len(eighth_hand.hand) != 0) and (eighth_hand.card_sum > comp.card_sum):
                eighth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{eighth_hand.name} WINS!")
                first_hand.add_cash(2 * eighth_hand.bet)
                eighth_hand.hand.clear()
                eighth_hand.bet = 0
                first_hand.get_balance()

            if (len(seventh_hand.hand) != 0) and (seventh_hand.card_sum > comp.card_sum):
                seventh_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{seventh_hand.name} WINS!")
                first_hand.add_cash(2 * seventh_hand.bet)
                seventh_hand.hand.clear()
                seventh_hand.bet = 0
                first_hand.get_balance()

            if (len(sixth_hand.hand) != 0) and (sixth_hand.card_sum > comp.card_sum):
                sixth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{sixth_hand.name} WINS!")
                first_hand.add_cash(2 * sixth_hand.bet)
                sixth_hand.hand.clear()
                sixth_hand.bet = 0
                first_hand.get_balance()

            if (len(fifth_hand.hand) != 0) and (fifth_hand.card_sum > comp.card_sum):
                fifth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fifth_hand.name} WINS!")
                first_hand.add_cash(2 * fifth_hand.bet)
                fifth_hand.hand.clear()
                fifth_hand.bet = 0
                first_hand.get_balance()

            if (len(fourth_hand.hand) != 0) and (fourth_hand.card_sum > comp.card_sum):
                fourth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fourth_hand.name} WINS!")
                first_hand.add_cash(2 * fourth_hand.bet)
                fourth_hand.hand.clear()
                fourth_hand.bet = 0
                first_hand.get_balance()

            if (len(third_hand.hand) != 0) and (third_hand.card_sum > comp.card_sum):
                third_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{third_hand.name} WINS!")
                first_hand.add_cash(2 * third_hand.bet)
                third_hand.hand.clear()
                third_hand.bet = 0
                first_hand.get_balance()

            if (len(second_hand.hand) != 0) and (second_hand.card_sum > comp.card_sum):
                second_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{second_hand.name} WINS!")
                first_hand.add_cash(2 * second_hand.bet)
                second_hand.hand.clear()
                second_hand.bet = 0
                first_hand.get_balance()

            if (len(first_hand.hand) != 0) and (first_hand.card_sum > comp.card_sum):
                first_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{first_hand.name} WINS!")
                first_hand.add_cash(2 * first_hand.bet)
                first_hand.hand.clear()
                comp.hand.clear()
                first_hand.bet = 0
                first_hand.get_balance()



            if (len(tenth_hand.hand) != 0) and (tenth_hand.card_sum < comp.card_sum):
                tenth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{tenth_hand.name} LOSES!")
                first_hand.get_balance()
                tenth_hand.bet = 0
                tenth_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(ninth_hand.hand) != 0) and (ninth_hand.card_sum < comp.card_sum):
                ninth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{ninth_hand.name} LOSES!")
                first_hand.get_balance()
                ninth_hand.bet = 0
                ninth_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(eighth_hand.hand) != 0) and (eighth_hand.card_sum < comp.card_sum):
                eighth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{eighth_hand.name} LOSES!")
                first_hand.get_balance()
                eighth_hand.bet = 0
                eighth_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(seventh_hand.hand) != 0) and (seventh_hand.card_sum < comp.card_sum):
                seventh_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{seventh_hand.name} LOSES!")
                first_hand.get_balance()
                seventh_hand.bet = 0
                seventh_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(sixth_hand.hand) != 0) and (sixth_hand.card_sum < comp.card_sum):
                sixth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{sixth_hand.name} LOSES!")
                first_hand.get_balance()
                sixth_hand.bet = 0
                sixth_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(fifth_hand.hand) != 0) and (fifth_hand.card_sum < comp.card_sum):
                fifth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fifth_hand.name} LOSES!")
                first_hand.get_balance()
                fifth_hand.bet = 0
                fifth_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(fourth_hand.hand) != 0) and (fourth_hand.card_sum < comp.card_sum):
                fourth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fourth_hand.name} LOSES!")
                first_hand.get_balance()
                fourth_hand.bet = 0
                fourth_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(third_hand.hand) != 0) and (third_hand.card_sum < comp.card_sum):
                third_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{third_hand.name} LOSES!")
                first_hand.get_balance()
                third_hand.bet = 0
                third_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(second_hand.hand) != 0) and (second_hand.card_sum < comp.card_sum):
                second_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{second_hand.name} LOSES!")
                first_hand.get_balance()
                second_hand.bet = 0
                second_hand.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False

            if (len(first_hand.hand) != 0) and (first_hand.card_sum < comp.card_sum):
                first_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{first_hand.name} LOSES THE ROUND!")
                first_hand.get_balance()
                first_hand.bet = 0
                first_hand.hand.clear()
                comp.hand.clear()
                if first_hand.account == 0:
                    first_hand.get_balance()
                    print(f"\n\n\t\t{first_hand.name} is OUT OF CASH!")
                    print("\n\t\tGAME OVER!!!")
                    game_on = False



        elif comp.card_sum > 21:

            if (len(tenth_hand.hand) != 0) and (tenth_hand.card_sum < 21):
                tenth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{tenth_hand.name} WINS!!!")
                first_hand.add_cash(2 * tenth_hand.bet)
                tenth_hand.hand.clear()
                tenth_hand.bet = 0
                first_hand.get_balance()

            if (len(ninth_hand.hand) != 0) and (ninth_hand.card_sum < 21):
                ninth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{ninth_hand.name} WINS!!!")
                first_hand.add_cash(2 * ninth_hand.bet)
                ninth_hand.hand.clear()
                ninth_hand.bet = 0
                first_hand.get_balance()

            if (len(eighth_hand.hand) != 0) and (eighth_hand.card_sum < 21):
                eighth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{eighth_hand.name} WINS!!!")
                first_hand.add_cash(2 * eighth_hand.bet)
                eighth_hand.hand.clear()
                eighth_hand.bet = 0
                first_hand.get_balance()

            if (len(seventh_hand.hand) != 0) and (seventh_hand.card_sum < 21):
                seventh_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{seventh_hand.name} WINS!!!")
                first_hand.add_cash(2 * seventh_hand.bet)
                seventh_hand.hand.clear()
                seventh_hand.bet = 0
                first_hand.get_balance()

            if (len(sixth_hand.hand) != 0) and (sixth_hand.card_sum < 21):
                sixth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{sixth_hand.name} WINS!!!")
                first_hand.add_cash(2 * sixth_hand.bet)
                sixth_hand.hand.clear()
                sixth_hand.bet = 0
                first_hand.get_balance()

            if (len(fifth_hand.hand) != 0) and (fifth_hand.card_sum < 21):
                fifth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fifth_hand.name} WINS!!!")
                first_hand.add_cash(2 * fifth_hand.bet)
                fifth_hand.hand.clear()
                fifth_hand.bet = 0
                first_hand.get_balance()

            if (len(fourth_hand.hand) != 0) and (fourth_hand.card_sum < 21):
                fourth_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{fourth_hand.name} WINS!!!")
                first_hand.add_cash(2 * fourth_hand.bet)
                fourth_hand.hand.clear()
                fourth_hand.bet = 0
                first_hand.get_balance()

            if (len(third_hand.hand) != 0) and (third_hand.card_sum < 21):
                third_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{third_hand.name} WINS!!!")
                first_hand.add_cash(2 * third_hand.bet)
                third_hand.hand.clear()
                third_hand.bet = 0
                first_hand.get_balance()

            if (len(second_hand.hand) != 0) and (second_hand.card_sum < 21):
                second_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{second_hand.name} WINS!!!")
                first_hand.add_cash(2 * second_hand.bet)
                second_hand.hand.clear()
                second_hand.bet = 0
                first_hand.get_balance()

            if (len(first_hand.hand) != 0) and (first_hand.card_sum < 21):
                first_hand.view_hand()
                comp.view_hand()
                print(f"\n\n\t\t{first_hand.name} WINS!!!")
                first_hand.add_cash(2 * first_hand.bet)
                first_hand.hand.clear()
                comp.hand.clear()
                first_hand.bet = 0
                first_hand.get_balance()
