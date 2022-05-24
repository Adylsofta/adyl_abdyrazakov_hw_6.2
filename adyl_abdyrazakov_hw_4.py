GeekTech = {
    'adress': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bug': ['fails', 'errors', 'stack']
}

del GeekTech['bug']  # удалили "bug"

GeekTech['adress'] = 'Ibraimova 103'  # изменили адресс

GeekTech['number'] = '0507052018'   # добавили номер, intagramm, другие курсы
GeekTech['instagram'] = 'geektech__kg'
GeekTech['courses'].append('UX/UI designer')
GeekTech['courses'].append('IOS developer')
GeekTech['courses'].append('GeekCamp')

GeekTech['courses'] = set(GeekTech['courses'])

for k, v in GeekTech.items():
    print(f'{k}: {v}')

print(GeekTech.keys())
print(GeekTech.values())
