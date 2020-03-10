from random import randint


def roll_the_dice():
    print('Это игра в кости.\n'
          'Для броска нажмите "Enter".\n'
          'Для выхода введите "exit".\n')

    counter = 0
    player1_win_count = []
    player2_win_count = []
    draw_count = []

    while True:
        counter += 1
        print(f"Раунд {counter}. Начинаем!")
        
        player1_roll = players_roll(1)
        if player1_roll == "exit":
                break
        player2_roll = players_roll(2)
        if player2_roll == "exit":
                break

        if player1_roll == player2_roll:
            print(f"Раунд {counter}: Ничья.\n")
            draw_count.append(str(counter))
        elif player1_roll > player2_roll:
            print(f"Раунд {counter}: Победил игрок 1.\n")
            player1_win_count.append(str(counter))
        elif player2_roll > player1_roll:
            print(f"Раунд {counter}: Победил игрок 2.\n")
            player2_win_count.append(str(counter))

    if len(player1_win_count) > len(player2_win_count):
        result = "\nИгрок 1 объявляется победителем турнира. Поздравляем!"
    elif len(player1_win_count) < len(player2_win_count):
        result = "\nИгрок 2 объявляется победителем турнира. Поздравляем!"
    elif len(player1_win_count) == len(player2_win_count):
        result = "\nТурнир не выявил победителя. Оба участника проявили себя достойно."

    while True:
        print(result)
        choice = input("Показать статистику? y/n ")

        if choice == 'y':
            print("\nСтатистика:")
            print(f"Раундов сыграно: {counter}.")
            
            print(f"Всего ничьих: {len(draw_count)}.", end="")
            if len(draw_count) == 1:
                print(f" В раунде: {draw_count[0]}.", end="")
            elif len(draw_count) > 1:
                print(f" В раундах: {', '.join(draw_count)}.", end="")
            
            print(f"\nПобед игрока 1: {len(player1_win_count)}.", end="")
            if len(player1_win_count) == 1:
                print(f" В раунде: {player1_win_count[0]}.", end="")
            elif len(player1_win_count) > 1:
                print(f" В раундах: {', '.join(player1_win_count)}.", end="")
            
            print(f"\nПобед игрока 2: {len(player2_win_count)}.", end="")
            if len(player2_win_count) == 1:
                #print(f" В раунде: {str(player2_win_count)}.", end="")
                print(f" В раунде: {player2_win_count[0]}.", end="")
            elif len(player2_win_count) > 1:
                print(f" В раундах: {', '.join(player2_win_count)}.", end="")
            return print("\nИгра завершена!")
            
        elif choice == 'n':
            return print("\nИгра завершена!")


def players_roll(players_turn):
    check = False

    while not check:
        player_action = input(f"Игрок {players_turn}. Для броска нажмите \"Enter\".")
        if player_action == "exit":
            return 'exit'
        else:
            player_roll = randint(1, 6)
            print("Выпало число: " + str(player_roll))
            check = True

    return player_roll


roll_the_dice()
