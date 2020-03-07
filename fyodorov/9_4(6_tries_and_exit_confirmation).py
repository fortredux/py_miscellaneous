from random import randint


def guess_number():
    print('Это игра "Угадай число".'
    '\nПопробуйте угадать загаданное число в диапазоне от одного до ста.'
    '\nУ вас есть шесть попыток.'
    '\nДля выхода введите "exit".\n')
    
    x = randint(1, 101)
    
    for i in range(1, 7):
        y = input("Попытка " + str(i) + ". Угадайте число: ")
        
        while y == 'exit':
            choice = exit_check()
            if choice:
                return print("Игра завершена!")
            else:
                y = input("Попытка " + str(i) + ". Угадайте число: ")
        
        try:
            y = int(y)
        except:
            print("Нужно было ввести число.")
            continue

        if y > x:
            print("Загаданное число меньше, чем " + str(y) + ".")
        elif y < x:
            print("Загаданное число больше, чем " + str(y) + ".")
        elif y == x:
            return print("\nПоздравляем! Вы угадали. Было загадано число " + str(x))
            
    return print("\nВы проиграли. Было загадано число " + str(x) + ".")


def exit_check():
    while True:
        choice = input("Вы действительно хотите выйти? (y\\n) ")
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Ведите "y" или "n" ')
            continue


guess_number()
