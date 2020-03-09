from random import randint


def roll_the_dice():
    print('Это игра в кости.\n'
          'Для броска нажмите "Enter".\n'
          'Для выхода нажмите "e".\n')
    
    while True:
        player1_roll = input("Игрок 1. Для броска нажмите \"Enter\".")
        player1_roll = randint(1, 6)
        print("Выпало число: " + str(player1_roll))

        player2_roll = input("Игрок 2. Для броска нажмите \"Enter\".")
        player2_roll = randint(1, 6)
        print("Выпало число: " + str(player2_roll))
        
        if player1_roll == player2_roll:
            print("Ничья.\n")
        elif player1_roll > player2_roll:
            print("Победил игрок 1!\n")
        elif player2_roll > player1_roll:
            print("Победил игрок 2!\n")


roll_the_dice()
