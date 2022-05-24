movies = {
    'Django Unchained': {
        'John': 10,
        'Jack': 9
    }, 'Морбиус': {}
}


def add_movie(movie):
    if movie in movies.keys():
        print("НЕТ такого фильма!!!")
    else:
        movies.update({movie: dict()})


def add_rating(Title, name, rating):
    Title = input('Введите название фильма для оценки рейтинга: ')

    if not Title.title() in movies.keys():
        print("This movie doesn't exist")
    elif Title.title() in movies:
        name = input('Имя оценивающего: ')
        rating = int(input('Oценку от 0 до 10: '))
        for i in movies:
            if name.title() in movies[i]:
                print('Ошибка! Такое имя уже есть!')
                name = input('Введите новое имя: ')
        if rating >= 1 and rating <= 10:
            print(f'A rating has been added for {Title}: {name} rated it {rating}')
            movies[Title.title()][name.title()] = rating
        else:
            print('Ошибка! Такой рейтинг не сушествует!')


def View_Ratings(a):
    for i in movies:
        mov_val = list(movies[i].values())
        if len(mov_val) == 0:
            print(f'Rating is not yet available for {i}')
        else:
            a = sum(mov_val) / len(movies)
            print(f'{i} is rated {round(a, 1)}')


while True:
    command = input(f'{movies} \n'
                    f'Выберите команду: \n'1
                    f'1 - Добавить фильм \n'
                    f'2 - Добавить рейтинг к фильму \n'
                    f'3 - Просматреть рейтинги всех фильмов \n'
                    f'4 - Выход \n')
    if command == '4':
        print("До скорых встреч!!!")
        break
    elif command == '1':
        movie = input("Введите название фильма:").capitalize()
        add_movie(movie)
        print(movies)
    elif command == '2':
        add_rating('Title', 'name', 'rating')
        print(movies)
    elif command == '3':
        View_Ratings('a')