# 1  2  3
# 4  5  6
# 7  8  9
mas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def print_table():
    for i in mas:
            for i2 in i:
                print(i2, end=' ')
            print()

hod_1 = 0
b = ["крестик"]
a = ["нолик"]
c = ["Начало игры!"]
k = 'O'
print(c[0])
f = [1]
def kuku(func):
    def wrapper():
        func()

        if any([mas[0][0] == mas[1][0] == mas[2][0],
         mas[0][1] == mas[1][1] == mas[2][1],
         mas[0][2] == mas[1][2] == mas[2][2],
         mas[0][0] == mas[0][1] == mas[0][2],
         mas[1][0] == mas[1][1] == mas[1][2],
         mas[2][0] == mas[2][1] == mas[2][2],
         mas[0][2] == mas[1][1] == mas[2][0],
         mas[0][0] == mas[1][1] == mas[2][2]]):

            print_table()
            print('Game Over')
            print(F"Выиграли {c[0]}и!")
            exit()
        elif len(f) == 10:
            print_table()
            print('Ничья!')
            exit()
    return wrapper

@kuku
def hod():
    print_table()
    print(f'Ход {a[0]}ов')
    c[0] = a[0]
    hod_1 = (int(input('введите число от 1 до 9: ')))
    if hod_1 in mas[0]:
        i = mas[0].index(hod_1)
        mas[0][i] = k
    elif hod_1 in mas[1]:
        i = mas[1].index(hod_1)
        mas[1][i] = k
    elif hod_1 in mas[2]:
        i = mas[2].index(hod_1)
        mas[2][i] = k
    elif hod_1 > 9 or hod_1 < 0:
        print('введите число от 1 до 9: ')
        hod()
    else:
        print('Ячейка уже занята, повторите ход')
        hod()

while True:
    f.append(1)
    if len(f)%2 == 0:
        k = 'X'
        a, b = b, a
        hod()
    else:
        k = 'O'
        a, b = b, a
        hod()
