from datetime import datetime
from random import randint

cash = 2500
round_number = 1
start = datetime.now()
result = dict()

while cash != 0:
    try:
        bet = int(input(f'Введите ставку: (доступно {cash}): '))
    except:
        print('Вы ввели некоректное значение!')
        continue

    if cash < bet:
        print('Недостаточно средств!')
        continue

    elif bet < 0:
        print('Ставка не может быть отрицательной!')
        continue

    player = randint(1, 6), randint(1, 6)
    comp = randint(1, 6), randint(1, 6)
    print(player)
    print(sum(player))

    if sum(player) > sum(comp):
        cash += bet
        results[round_number] = f'Player - {player}, Comp - {comp}, YOU WON!!!'
    elif sum(player) < sum(comp):
        cash = -bet
        result[round_number] = f'Player - {player}, Comp - {comp}, YOU LOSE!!!'
    else:
        results[round_number] = f'Player - {player}, Comp - {comp}, DRAW!!!'

    for key, val in results.items():
        print(f'ROUND {key}: {val}')
    round_number += 1

end = datetime.now()
