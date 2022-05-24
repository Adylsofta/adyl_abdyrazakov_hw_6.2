ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*ten)
evens = list(filter(lambda x: x % 2 == 0, ten))
print(*evens)
d = list(map(lambda x: x ** 2, evens))
print(*d)


def abc():
    while 1:
        try:
            index = int(input('enter index'))
            if index == 94:
                break
            print(ten[index])
        except ValueError:
            print('НЕ ВВОДИТЬ БУКВЫ!')
        except IndexError:
            print(f"Вводить только числа! от 0 - {len(ten) - 1}")


abc()