""" Rock, Papper and Scissors Game """
import random

options = ['rock','papper','scissors']
times = 0
user1_score = 0
user2_score = 0

while times < 5:
    user1 = random.choices(options)
    user2 = random.choices(options)    
    a = user1[0]
    b = user2[0]
    print(a,b)
    if a == 'rock' and b == 'scissors':
        user1_score += 1
    if a == 'scissors' and b == 'papper':
        user1_score += 1
    if a == 'papper' and b == 'rock':
        user1_score += 1

    if a == 'scissors' and b == 'rock':
        user2_score += 1
    if a == 'papper' and b == 'scissors':
        user2_score += 1
    if a == 'rock' and b == 'papper':
        user2_score += 1
    
    times += 1
print('------------------------')
print(f'user1 score: {user1_score}\nuser2 score: {user2_score}')
print('------------------------')
if user1_score > user2_score:
    print('user1 wins')
elif user1_score == user2_score:
    print('No one wins')
else:
    print('use2 wins')
