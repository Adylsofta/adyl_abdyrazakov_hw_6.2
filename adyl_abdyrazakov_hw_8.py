from random import randint
from datetime import datetime
name = input("Укажите имя:")
attempts = int(input("Сколько попыток?"))
count = 0
start = datetime.now()
with open('results.txt', 'a', encoding="utf-8") as a:
    while True:
        if count == attempts:
            print('Попытки закончились!')
            break
        else:
            count += 1
            number1 = randint(1, 9)
            number2 = randint(1, 9)
            numbers_input = int(input(f"{number1} * {number2} = ?"))
            result = number1 * number2
            print(result)
            if numbers_input == result:
                a.write(f'{number1} * {number2} = {numbers_input} ({result}) правильно\n')
            else:
                a.write(f'{number1} * {number2} = {numbers_input} ({result}) неправильно\n')
    a.write(f'было {count} попыток, потраченное время {datetime.now() - start}, имя: {name}\n')
