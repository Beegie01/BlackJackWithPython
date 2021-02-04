import random

'''
OBJECTS:
card, player, dealer

DATA:
card.rank, card.shape, card.value,
player.name, player.account, player.hand,
dealer.hand

ACTIONS:
card: details, deck
dealer: shuffle, share_card
player: place_bet, receive_card, hit, stand, surrender, double_down, split
'''

class Card:
    '''
    Attributes and methods for each card instance
    '''

    shapes = ("Hearts", "Clubs", "Diamonds", "Spades")
    ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
    values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
              "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

    def __init__(self, rank, shape):
        self.rank = rank
        self.shape = shape
        self.value = Card.values[rank]

    def __str__(self):
        return f"\n\t\t{self.rank}/{self.value} of {self.shape}"


class Dealer:
    '''
    Data and Actions of dealer
    '''

    def __init__(self):
        self.deck = []

    def deck_up(self):
        holder = []
        for shape in Card.shapes:
            for rank in Card.ranks:
                each_card = Card(rank, shape)
                holder.append(each_card)
        self.deck = holder

    def deck_shuffle(self):
        random.shuffle(self.deck)
        print("\n\t\tDeck shuffled!")

    def deal_card(self):
        if len(self.deck) == 0:
            print("\n\n\t\tDealer restocking deck")
            self.deck_up()
            self.deck_shuffle()
            return self.deck.pop(0)
        return self.deck.pop(0)

    def get_deck(self):
        print(f"\n\n\t\tDeck: {len(self.deck)} cards")



class Player:
    '''
    Data and Actions of each player
    '''

    def __init__(self, name):
        self.name = name
        self.account = 0.00
        self.hand = []
        self.card_sum = 0
        self.bet = 0


    def receive_card(self, new_card):
        self.sumup_cards()
        self.ace_adjust()
        ace = self.ace_counter()
        if self.card_sum < 21:
            self.hand.append(new_card)
            print(f"\n\t\tCard received by {self.name}")
        else:
            print(f"\n\n{self.name} CANNOT RECEIVE MORE CARDS!\n\nEnter 'stand' to continue")

    def view_hand(self):
        print(f"\n\t\tShowing {self.name}'s hand")
        for ind, card in enumerate(self.hand):
            print(f"\n\t\tCard {ind+1}: {card}")
        self.show_sum()

    def show_sum(self):
        self.ace_adjust()
        print(f"{self.name}'s cards sum to: {self.card_sum}")

    def bankroll_account(self, amount):
        self.account = amount
        round(self.account, 2)

    def get_balance(self):
        print("\n","\t"*8,f"{self.name}'s account: ${self.account}")

    def get_hand(self):
        print(f"\n{self.name} has {len(self.hand)} cards")

    def play_on(self):
        response = self.quick_check()
        if response:
            pass

    def computer_faceup(self):
        # Computer's ninth card exposed
        print(f"\n\n{self.name}'s card 1: {self.hand[0]}")

    def withdraw(self):
        while True:
            print("\n","\t"*8,f"{self.name} currently has ${self.account}")
            val = input("\n"+"\t"*8+f"Enter amount \n\t\t\t\t\t\tMinimum: $50 | Maximum: $1000\n\n\t\t\t\t\t\t:")

            try:
                amount = float(val)
                round(amount, 2)
            except:
                continue

            if self.account < amount:
                print("\n","\t"*8, "Insufficient Funds!")
                continue

            elif (amount < 50) or (amount > 1000):
                print("\n","\t"*8,f"{amount} is invalid!")
                continue

            return round(amount, 2)

    def place_bet(self):
        self.bet = 0
        self.bet = self.withdraw()
        self.account -= self.bet
        round(self.account, 2)
        print("\n","\t"*8,f"Bet Placed:   ${self.bet}")
        print("\n","\t"*8,f"{self.name}'s Remaining Balance:   ${self.account}")

    def sumup_cards(self):
        self.card_sum = 0
        for card in self.hand:
            self.card_sum += card.value

    def add_cash(self, amount):
        round(amount, 2)
        self.account += amount
        round(self.account, 2)

    def ace_counter(self):
        counter = 0
        for card in self.hand:
            if card.rank == 'Ace':
                counter += 1
        return counter

    def ace_adjust(self):
        self.sumup_cards()
        ace = self.ace_counter()

        if (ace > 1) and (self.card_sum > 21) and (self == Player('Computer')):
            self.card_sum -= 10

        if (ace > 0) and (self.card_sum > 21):
            print(f"\n\n{self.name} has {ace} Aces")
            if (ace == 1) and (self.card_sum > 21):
                self.card_sum -= (10*ace)
            elif (ace > 1) and (self.card_sum > 21) and (self != Player('Computer')):
                while True:
                    val = input("\n\t\tHow many aces do you want to assign 1?\n")

                    try:
                        n = int(val)
                        if n > ace:
                            print(f"\n\t{self.name} enter a valid number")
                            continue
                        else:
                            self.card_sum -= (10*n)
                            break
                    except:
                        continue


    def split(self):
        self.view_hand()
        recurrence = self.recurrrence()
        if recurrence:
            ans = self.ask_split()
            if ans == 'yes':
                return True
            print("\nNOT SPLITTING")
            self.view_hand()
            return False

    def recurrrence(self):
        count = 0
        for ind in range(len(self.hand)-1):
            for card in self.hand:

                if self.hand[ind].value == self.hand[ind+1].value:
                    count += 1
                    break
            continue

        if count > 0:
            return True
        return False

    def ask_split(self):
        while True:
            print(f"\n\t\t\t\t{self.name}, want to split?")
            val = input("\n\t\t\t\tYes or No:\n\t\t\t\tAnswer:    ")

            if val.lower() not in ['yes', 'no']:
                print(f"\n{val} is invalid!")
                continue

            else:
                return val.lower()


    def split_done(self, old_hand, main_hand):

        # Bet is created for second hand (twin) of player
        self.bet = main_hand.bet

        # An equivalent amount is deducted from player's main account
        main_hand.account -= self.bet

        # Player's main account is replicated for the second hand
        self.bankroll_account(main_hand.account)

        # Second hand receives first card from player's hand (SPLIT)
        self.receive_card(old_hand.hand.pop())

        print("\n\n\tSPLIT DONE!")

        # Viewing the remaining amount
        main_hand.get_balance()


    def quick_check(self):
        while True:
            print("\nScreen Pause!")
            val = input("\nPress Enter to continue, or 'e' to exit game:")

            acc_range = ['', 'e', 'exit']
            if val not in acc_range:
                print(f"\n{val} is not valid!")
                continue
            else:
                if val.lower() == '':
                    return True
                elif val.lower() in ['e', 'exit']:
                    return self.exit_play()

    def four_options(self):

        acc_range = ['s', 'stand', 'h', 'hit', 'd', 'double', 'q', 'surrender']
        while True:
            print(f"\n\n\n\t\t\t\t\t\t{self.name}'s TURN")
            self.view_hand()

            if self.account >= self.bet:
                print("\n\t\tTO HIT, STAND, DOUBLE_DOWN, OR SURRENDER?")
                val = input("\n\t\tEnter 'h', 's', 'd', or 'q' \n\n\t\t:  ")

            else:
                acc_range = ['s', 'stand', 'h', 'hit', 'q', 'surrender']
                print("\n\t\tTO HIT, STAND, OR SURRENDER?")
                print()
                while True:
                    val = input("\n\t\tEnter 'h', 's', or 'q' \n\n\t\t:  ")

                    if val.lower() not in acc_range:
                        continue

                    else:
                        break

            if val.isdigit() or (val.lower() not in acc_range):
                print(f"\n{val} is invalid!")
                continue

            else:
                return val.lower()


    def two_options(self):

        print(f"\n\t{self.name}'s TURN")
        self.view_hand()

        acc_range = ['s', 'h']

        while True:
            print("\n\t\tTO HIT OR STAND?")
            print()
            val = input("\n\t\tEnter 'h' or 's' \n\n\t\t:  ")

            if val.isdigit() or (val.lower() not in acc_range):
                print(f"\n{val} is invalid!")
                continue

            else:
                return val.lower()


    def first_available_hand(self, hands_dict):
        empty_key = None

        for k,v in hands_dict.items():
            if v == 0:
                empty_key = k
                break

        if empty_key == None:
            return None
        return empty_key


    def player_action(self, dealer, response):
        if (response == 'h') or (response == 'hit'):
            print(f"\n\n{self.name} HITS!!!\n")
            self.receive_card(dealer.deal_card())
            return 'hit'

        elif (response == 'stand') or (response == 's'):
            print(f"\n\n{self.name} WAVES!!!")
            return 'wave'

        elif (response == 'd') or (response == 'double'):
            if self.account >= self.bet:
                print(f"\n\n{self.name} DOUBLES!!!")
                self.account -= self.bet
                self.bet *= 2
                round(self.account, 2)
                self.receive_card(dealer.deal_card())
                return 'double'
            else:
                print("\nInsufficient Funds!")
                print(f"\n{self.name} CANNOT DOUBLE!")
                return "ask"

        elif (response == 'q') or (response == 'surrender'):
            if self.card_sum < 22:
                print(f"\n\n{self.name} SURRENDERS!")
                self.account += (self.bet / 2)
                round(self.account, 2)
                return 'surrender'
            else:
                print(f"\n{self.name} CANNOT SURRENDER!")
                return 'wave'

    def exit_play(self):
        print("{self.name}, thank you for playing!")
        quit()






def player_name():
    while True:
        val = input("\n\t\tPlayer Name:   \n\t\t")
        if val.isdigit():
            print("\n\Enter a valid name")
            continue
        return val.upper()
