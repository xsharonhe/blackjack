import random

#global variables:
suits = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack': 10, 'Queen': 10, 'King': 10, 
'Ace': 11}

playing = True

class Card():
    def __init__(self, suit, rank):
    	self.suit = suit
    	self.rank = rank

    def __str__(self):
    	return '{} of {}'.format(self.rank, self.suit)

class Deck(): #review!
	def __init__(self):
		self.deck = [] #has to refer to self!

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		print_cards = ''

		for card in self.deck:
			print_cards += '\n ' + card.__str__()

		return 'This deck has the following cards: ' + print_cards

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		dealt_card = self.deck.pop()
		return dealt_card

class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.ace = 0

	def add_card(self, card): #from Deck.deal()
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.ace += 1

	def adjust_for_ace(self):
		if self.value > 21 and self.ace:
			self.value -= 10
			self.ace -= 1

class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):
	while True: 
		try:
			chips.bet = int(input("Please input your bet: "))
		except ValueError:
			print("Sorry that is not a valid bet!")
		else: 
			if chips.bet > chips.total:
				print("Sorry, your bet cannot exceed your total balance.")
			else:
				break

def hit(deck, hand):
	hand.append(add_card(deck.deal()))
	hand.adjust_for_ace()

def hit_or_stand(deck, hand):
	global playing

	while True:
		ans = input("Would you like to hit or stand? Press 'h' for hit and 's' for stand.")

		if ans[0].lower() == 'h':
			hit(deck, hand)
		elif ans[0].lower() == 's':
			print("Player's turn is finishe d. Dealer's turn now.")
			playing = False
		else:
			print("Please enter a valid move!")
			continue
		break


def show_some(player, dealer):
	print("\nDealer's Hand: ")
	print("<card hidden>")
	print("", dealer.cards[1])
	print("\nPlayer's Hand: ", *player.cards, sep = " ->")

def show_all(player, dealer):
	print("\nDealer's Hand: ", *dealer.cards, sep = " ->")
	print("\nDealer's Value: ", dealer.value, sep = " ->")
	print("\nPlayer's Hand: ", *player.cards, sep = " ->")
	print("\nPlayer's Value: ", player.value, sep = " ->")

def player_busts(player, dealer, chips):
	print("Unfortunately, you have busted and you have lost the bet!")
	chips.lose_bet()

def player_wins(player, dealer, chips):
	print("You have won!")
	chips.win_bet()

def dealer_busts(player, dealer, chips):
	print("The dealer has busted!")
	chips.win_bet()

def dealer_wins(player, dealer, chips):
	print("The dealer has won!")
	chips.lose_bet()

def push(player, dealer):
	print("It's a push! You and the dealer have tied.")

while True:
	print("Welcome to the SIMPLIFIED version of BLACKJACK!")

	#Creating Deck:
	deck = Deck()

	#Shuffling the Deck:
	deck.shuffle()

	#Deal two cards to each player:

	player = Hand()
	player.add_card(deck.deal())
	player.add_card(deck.deal())

	dealer = Hand()
	dealer.add_card(deck.deal())
	dealer.add_card(deck.deal())

	#Setting up Player's Chips and Prompt
	chips = Chips()
	bet = take_bet(chips)

	#Show Cards:
	show_some(player, dealer)

	while playing:

		#Prompt hit or stand
		hit_or_stand(player,deck)

		#show cards
		show_some(player,dealer)

		if player.value > 21:
			player_busts(player, dealer, chips)
			break
		#could cleanup this code
		elif player.value <= 21:
			while dealer.value <= 17:
				hit(deck, dealer)
		
		#show all cards:
		show_all(player, dealer)    
    
        #run different winning scenarios
        if player.value > dealer.value:
        	player_wins(player, dealer, chips)
        elif player.value < dealer.value:
        	dealer_wins(player, dealer, chips)
        elif dealer.value > 21: #forgot scenario
        	dealer_busts(player, dealer, chips)
        elif player.value = dealer.value:
        	push(player, dealer, chips)

        #inform player of their chips total
        print("\nYour chip total is: {}".format(chip.total))

        while True:
			ans = input("Would you like to play again? Press 'y' for yes 'n' for no.")
			if ans[0].lower() != 'y' or ans[0].lower() != 'n':
				print("Sorry that is not a valid answer!")
				continue
			else:
				break

		if ans[0].lower() = 'n':
			print("Thanks for playing!")
			break
