from random import randint


def roll_the_dice():
    print('Это игра в кости.\n'
          'Для броска нажмите "Enter".\n'
          'Для выхода введите "e".\n')
    
    while True:
        check = False
        while not check:
            player1_roll = input("Игрок 1. Для броска нажмите \"Enter\".")
            if player1_roll == "":
                player1_roll = randint(1, 6)
                print("Выпало число: " + str(player1_roll))
                check = True
            elif player1_roll == "e":
                return print("Игра завершена!")
            else:
                continue
        check = False
        
        while not check:
            player2_roll = input("Игрок 2. Для броска нажмите \"Enter\".")
            if player2_roll == "":
                player2_roll = randint(1, 6)
                print("Выпало число: " + str(player2_roll))
                check = True
            elif player2_roll == "e":
                return print("Игра завершена!")
            else:
                continue
        check = False
        
        if player1_roll == player2_roll:
            print("Ничья.\n")
        elif player1_roll > player2_roll:
            print("Победил игрок 1.\n")
        elif player2_roll > player1_roll:
            print("Победил игрок 2.\n")


roll_the_dice()
