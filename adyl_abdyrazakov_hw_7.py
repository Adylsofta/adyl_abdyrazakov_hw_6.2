from random import randint
import datetime

start = datetime.datetime.now()
secret_word = randint(1, 100)
print(secret_word)
c = 1

while True:
    try:
        guess = int(input('Try to guess number from 1 to 100: '))
        if guess > 100 or guess < 1:
            print('Choose from 1 - 100')
        elif guess > secret_word:
            print('<')
            c += 1
        elif guess < secret_word:
            print('>')
            c += 1
        elif guess == secret_word:
            print('\nYou won!')
            break
    except:
        print('Choose only numbers')
print(f'\nYou used {c} guesses')
print(f'Время опроса: {datetime.datetime.now() - start}')
