# 1  2  3
# 4  5  6
# 7  8  9
game0 = [1, 2, 3]
game1 = [4, 5, 6]
game2 = [7, 8, 9]
hod_1 = 0
hod_2 = 0
a = ["крестик"]
b = ["нолик"]
c = ["Начало игры!"]
print(c[0])
f = [1]
def kuku(func):
    def wrapper():
        func()

        if any([game0[0] == game1[0] == game2[0],
         game0[1] == game1[1] == game2[1],
         game0[2] == game1[2] == game2[2],
         game0[0] == game0[1] == game0[2],
         game1[0] == game1[1] == game1[2],
         game2[0] == game2[1] == game2[2],
         game0[2] == game1[1] == game2[0],
         game0[0] == game1[1] == game2[2]]):

            print(game0, game1, game2, sep='\n')
            print('Game Over')
            print(F"Выиграли {c[0]}и!")
            exit()
        elif len(f) == 9:
            print(game0, game1, game2, sep='\n')
            print('Ничья!')
            exit()
    return wrapper

@kuku
def hod_k():
    print(game0, game1, game2, sep='\n')
    print(f'Ход {a[0]}ов')
    c[0] = a[0]
    hod_1 = (int(input('введите число от 1 до 9: ')))
    if hod_1 in game0:
        i = game0.index(hod_1)
        game0[i] = 'X'
    elif hod_1 in game1:
        i = game1.index(hod_1)
        game1[i] = 'X'
    elif hod_1 in game2:
        i = game2.index(hod_1)
        game2[i] = 'X'
    elif hod_1 > 9 or hod_1 < 0:
        print('введите число от 1 до 9: ')
        hod_k()
    else:
        print('Ячейка уже занята, повторите ход')
        hod_k()
hod_k()

@kuku
def hod_O():
    print(game0, game1, game2, sep='\n')
    print(f'Ход {b[0]}ов')
    c[0] = b[0]
    hod_2 = (int(input('введите число от 1 до 9: ')))
    if hod_2 in game0:
        i = game0.index(hod_2)
        game0[i] = 'O'
    elif hod_2 in game1:
        i = game1.index(hod_2)
        game1[i] = 'O'
    elif hod_2 in game2:
        i = game2.index(hod_2)
        game2[i] = 'O'
    elif hod_2 > 9 or hod_2 < 0:
        print('введите число от 1 до 9: ')
        hod_O()
    else:
        print('Ячейка уже занята, повторите ход')
        hod_O()

while True:
    f.append(1)
    if len(f)%2 == 0:
        hod_O()
    else:
        hod_k()