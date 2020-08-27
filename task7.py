import random

print(" Guess the secret number between 1 to 100 ")
secret_num = random.randint(1,100)
attempts = 1

def guessTheSecret():
	""" This funtion returns true if the user guesses the secret number """
	guess = int(input('Guess the number > '))
	global attempts
	check = False
	while guess != secret_num:
		if  guess < secret_num:
			print('Your guess is too low')
		elif guess > secret_num:
			print('You guess to too high')
		guess = int(input('Guess again > '))
		attempts += 1
		if attempts >= 4:
			break
	if guess == secret_num:
		return True
		
if guessTheSecret():
	print(f'congrats, you made in {attempts} attempts')
else:
	print('sorry, you ran out of attempts.')
