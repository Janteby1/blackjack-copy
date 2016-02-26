# this file should have everyhting the game shows the user

# function to print out the rules 
class View:

	def rules (self):
		print ("Welcome to the Black Jack 2.0!")
		print ("If you are unfamiliar with the rules fo the game, try Google.")
		print ("Just make sure not to go over 21 and go bust!")
		print ("Here we go...")
		print (" ")

	def card(self, card):
		print ("You got delt a ", card)
		print ("")

	def dealer_card(self, card):
		print ("Dealer got delt a ", card)
		print ("")

	def dealer_card2(self):
		print ("Dealer got delt another card")
		print ("")

	def ace (self, card):
		choice = input("You got delt an ace, would you like to use it as a value of 1 or 11? ")
		if choice == "1":
			print ("You chose to use it as a value of 1")
			card = 1
			return card
		elif choice == "11":
			print ("You chose to use it as a value of 11")
			card = 11
			return card

	def dealer_bust(self):
		print ("The dealer went bust, you win!")
		print (" ")

	def player_bust(self):
		print ("You went bust, you lose!")
		print (" ")

	def dealer_hit(self):
		print (" ")
		print ("The dealer is under 15 so he hit and got another card")

	def player_21(self):
		print ("You have 21, you win!")
		print (" ")

	def dealer_21(self):
		print ("The dealer has 21, you lose!")
		print (" ")

	def dealer_win(self):
		print ("The dealer has a higher score, you lose!")
		print (" ")

	def player_win(self):
		print ("You have a higher score, you win!")
		print (" ")

	def push(self):
		print ("You both have the same score, it is a push ...")
		print (" ")

	def hit(self):
		print ("")
		print ("You chose to hit and get another card")

	def total(self, playertotal):
		print ("Your total score is ", playertotal)

	def hit_card(self, playercard3):
		print ("You got delt a ", playercard3)

	def stick(self):
		print ("")
		print ("You chose to stick and not receive another card ")
		print (" ")

	def repeate_hs(self):
		print ("Please enter 1 or 0 to choose if you want to hit (1) or stick (0)")

