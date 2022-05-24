mentor = ['Sultan', 'Alim', 'Shamil']
while True:
    command = input(f'{mentor} \n'
                    f'Выберите команду: \n'
                    f'1 - Добавление \n'
                    f'2 - Изменение \n'
                    f'3 - Удаление \n'
                    f'4 - Выход \n')
    if command == '4':
        print(f'Код завершен{tuple(mentor)}')
        break
    if command == '1':
        new_mentor = input('\nВведите имя ментора, которого  хотите добавить:').capitalize()
        if new_mentor in mentor:
            print("Этот ментор уже есть в списке!")
        if len(mentor) >= 5:
            print("Нельзя больше добавлять!")
            continue
        elif len(new_mentor) <= 15:
            mentor.append(new_mentor)
        else:
            print('\n Имя должно содержать не более 15 букв')
            continue
    if command == '2':
        changed_mentor = input('\n Введите имя ментора, которого хотите заменить:').capitalize()
        add_mentor = input('\n Введите имя нового ментора:').capitalize()
        if changed_mentor in mentor and len(add_mentor) <= 15:
            mentor.remove(changed_mentor)
            mentor.append(add_mentor)
        elif changed_mentor in mentor and len(add_mentor) != 15:
            print('\n Имя должно содержать не менее 15 букв')
            continue
        else:
            print('\n Ментора, которого вы хотите изменить, нет в списке')
            continue
    if command == '3':
        b = input('Выберите способ по которому будете удалять по индексу или по имени?n/i ')
        if b == 'n':
            g = input('Введите имя:').capitalize()
            if g in mentor:
                mentor.remove(g)
            else:
                print('Этого ментора нет в списке!')
                continue
        elif b == 'i':
            f = int(input('Введите индекс:'))
            if f > len(mentor) - 1:
                print('Этого индекса нет!')
                continue
            else:
                del mentor[f]
    else:
        print('Выберите только от 1-4:')
