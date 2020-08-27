import numpy as np
import random

class Rolldice():
	def play():
		""" This is a dice roll game, computer rolls the dice two times for you.
		If the sum of two rolls is greater or equat to 8, You win else you're asked to try again."""

		print("\t Welcome to Roll Dice Game")
		name = input('Enter your name: ')
		quit = 'y'
		score = 0
		attempts = 0
		while quit != 'n':
			first_roll = np.array([random.randint(1,6)])
			second_roll = np.array([random.randint(1,6)])
			if first_roll+second_roll >= 8:
				print('You earned 10 points!')
				score += 10
				attempts += 1
			else:
				print('You Lost 10 points!')
				attempts += 1
				score -= 10
				if score < 0:
					score = 0
			quit = input('Want to  try again (y/n) ')
		print(f'You made: {score} score in {attempts} attempts')

