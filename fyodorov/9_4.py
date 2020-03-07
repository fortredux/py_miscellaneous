from random import randint


def guess_number():
    print('Это игра "Угадай число".'
    '\nПопробуйте угадать загаданное число в диапазоне от одного до ста.'
    '\nДля выхода введите "exit".\n')
    
    x = randint(1, 101)
    
    guess = False
    
    while not guess:
        y = input("Угадайте число: ")
        
        if y == 'exit':
            return
        
        try:
            y = int(y)
        except:
            print("Нужно было ввести число.")
            continue

        if y > x:
            print("Загаданное число меньше, чем " + str(y) + ".")
        elif y < x:
            print("Загаданное число больше, чем " + str(y) + ".")
        elif y == 'exit':
            return
        elif y == x:
            guess = True
            
    return print("\nПоздравляем! Вы угадали. Было загадано число " + str(x) + ".")


guess_number()
