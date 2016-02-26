# check object orientation of it - OK
# split into M, V, c files - DONE
# Add database to it with SQL)

# blackjack game (MVP)
import random 
import sys
from random import shuffle

from view_blackjack import View

# # dont acctually use these classes in the create suit method bc I counlt add non-int to find total
# class Deck ():
# 	def __init__ (self, value, name):
# 		self.value = value
# 		self.name = name
# 	def __repr__ (self):
# 		return str(self.value)

# class Player ():
# 	def __init__ (self, total, hits):
# 		self.total = total
# 		self.hits = hits
# 	def __repr__ (self):
# 		return str(self.value)


class Game ():
	def __init__ (self, roll):
		self.roll = None 
		self.view = View()

	def rules (self):
		self.view.rules()

	def create_suit(self):
		"""creates a list with one card of each value and shuffles them"""
		suit = []
		for i in range (1,14):
			if i < 11:
				suit.append(i)
			else:
				suit.append(10)
		shuffle(suit)		
		return suit 

	def create_full_deck (self):
		"""creates 4 copies of the suits, full deck of random cards"""
		deck = {}
		for i in range (1,5):
			deck[i] = self.create_suit()
		self.deck = deck

	def pick_card (self):
		"""	try to randomize the card pick (random deck, plus 2 random rolls to pick diff positions)"""
		roll = random.random()
		roll2 = random.random()

		if roll2 > .5:
			if roll < .25:
				card = (game1.deck[1][4])
				# take cards out of the deck once they are picked in a hand
				game1.deck[1].remove(card)
				return card
			elif roll > .25 and roll < .5:
				card = (game1.deck[2][7])
				game1.deck[2].remove(card)
				return card
			elif roll > .5 and roll < .75:
				card = (game1.deck[1][1])
				game1.deck[1].remove(card)
				return card
			else:
				card = (game1.deck[3][9])
				game1.deck[3].remove(card)
				return card
		else: 
			if roll < .25:
				card = (game1.deck[2][9])
				game1.deck[2].remove(card)
				return card
			elif roll > .25 and roll < .5:
				card = (game1.deck[3][10])
				game1.deck[3].remove(card)
				return card
			elif roll > .5 and roll < .75:
				card = (game1.deck[2][2])
				game1.deck[2].remove(card)
				return card
			else:
				card = (game1.deck[4][1])
				game1.deck[4].remove(card)
				return card

	def deal_cards (self):
		card = self.pick_card()
		self.view.card(card)
		# check if it is an ace, can use it as an 11
		if card == 1:
			choice = input("You got delt an ace, would you like to use it as a value of 1 or 11? ")
			if choice == "1":
				print ("You chose to use it as a value of 1")
				card = 1
				return card
			elif choice == "11":
				print ("You chose to use it as a value of 11")
				card = 11
				return card
		else:
			return card

	def dealer_cards (self):
		card = self.pick_card()
		self.view.dealer_card(card)
		return card

	def dealer_cards_hidden (self):
		card = self.pick_card()
		self.view.dealer_card2()
		return card

	def choose_hit (self, playertotal, dealertotal):
		hit = input ("Do you want to hit (1) or stick (0)? ")
		if hit == "1":
			self.view.hit()
			playercard3 = game1.pick_card()
			self.view.hit_card(playercard3)
			playertotal = playertotal + playercard3
			self.view.total(playertotal)
			game1.check_bust(playertotal, dealertotal)
			game1.check_21(playertotal, dealertotal)
			game1.choose_hit(playertotal, dealertotal)
		elif hit == "0":
			self.view.stick()
			game1.check_bust(playertotal, dealertotal)
			game1.check_21(playertotal, dealertotal)
			game1.check_win(playertotal, dealertotal)
		else:
			self.view.repeate_hs()
			game1.choose_hit(playertotal, dealertotal)

	def check_bust (self, playertotal, dealertotal):
		if playertotal > 21:
			self.view.player_bust()
			sys.exit()
		elif dealertotal >21:
			self.view.dealer_bust()
			sys.exit()
		else:
			pass

	def dealer_hit (self, dealertotal, playertotal):
		if dealertotal <= 15:
			self.view.dealer_hit()
			dealercard3 = game1.pick_card()
			print ("He got delt a ", dealercard3)
			dealertotal = dealertotal + dealercard3
			game1.check_bust(playertotal, dealertotal)
			game1.check_21(playertotal, dealertotal)

	def check_win (self, playertotal, dealertotal):
		game1.check_21(playertotal, dealertotal)
		if dealertotal > playertotal:
			self.view.dealer_win()
			sys.exit()
		elif dealertotal == playertotal:
			self.view.push()
			sys.exit()
		else:
			self.view.player_win()
			sys.exit()

	def check_21 (self, playertotal, dealertotal):
		if playertotal == 21:
			self.view.player_21()
			sys.exit()
		elif dealertotal == 21:
			self.view.dealer_21()
			sys.exit()

	def play (self):
		playertotal = 0
		dealertotal = 0

		# give out cards and take them out of the deck
		playercard = game1.deal_cards()
		dealercard = game1.dealer_cards()

		# calculate totals 
		playertotal = playertotal + playercard
		dealertotal = dealertotal + dealercard

		# give out second cards and take them out of the deck
		playercard = game1.deal_cards()
		dealercard = game1.dealer_cards_hidden()

		# calculate totals 
		playertotal = playertotal + playercard
		dealertotal = dealertotal + dealercard
		print ("Your total is ", playertotal)
		game1.check_21(playertotal, dealertotal)

		# dealer automatic hit or stick
		game1.dealer_hit (dealertotal, playertotal)

		# ask player to hit or stick
		print ("")
		game1.choose_hit(playertotal, dealertotal)

		# check bust
		game1.check_bust(playertotal, dealertotal)

		# compare scores to see who wins 
		game1.check_win(playertotal, dealertotal)



# create the game
game1 = Game(None)

# print the rules
game1.rules()

# create a deck of shuffled cards
game1.create_full_deck()
print (game1.deck)
print ("")

# play the game 
game1.play()





'''
Rules 
* `10` /`J` / `Q`/ `K` - are all counted as 10
* `Ace` can be counted as a 10 or a 1
* There should be at least 1 deck with 52 cards
* Player should have the option to hit or stay
* Dealer should know when to hit or stay
* When either the player or dealer bust they automatically lose
* `bust` when a player/dealer has a combination of cards that go over 21
'''

'''
Jacks-MacBook-Pro-2:blackjack JackAAnteby$ python3 blackjack.py 
You got delt a  5

Dealer got delt a  2

You got delt a  8

Dealer got delt another card

Your total is  13
 
The dealer is under 15 so he hit and got another card

Do you want to hit (1) or stick (0)? 1

You chose to hit and get another card
You got delt a  3
Your total score is  16
Do you want to hit (1) or stick (0)? 1

You chose to hit and get another card
You got delt a  5
Your total score is  21
You have 21, you win!
Jacks-MacBook-Pro-2:blackjack JackAAnteby$ 
'''










