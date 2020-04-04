from random import randint

"""
def roll_the_dice():
    print('Это игра в кости.\n'
          'Для броска нажмите "Enter".\n'
          'Для выхода введите "e".\n')
          
    while True:
        '''
        players = ['player1_roll', 'player2_roll']
        for player in range(len(players)):
            print(str(player+1) + players[player])
            players[player] = players_roll(player+1)
        '''
        
        '''
        for player_number in range(1, 3):
            player_roll(players_turn)
        '''
        
        '''
        player1_roll = player_roll(1)
        player2_roll = player_roll(2)
        '''
        #player1_roll = 0
        #player2_roll = 0
        
        for players_turn in range(1, 3):
            roll = players_roll(players_turn)
            if players_turn == 1:
                player1_roll = roll
                # При достижении превого if - этоусловие не срабатывает.
            elif player1_roll == "exit":
                return print("Игра завершена!")
            elif players_turn == 2:
                player2_roll = roll
                # Здесь же, если ввести 'e' на второй попытке, вообще будет ошибка.
            elif player1_roll == "exit" or player2_roll == "exit":
                return print("Игра завершена!")

        for players_turn in range(1, 3):
            roll = players_roll(players_turn)
            if players_turn == 1:
                player1_roll = roll
            elif player1_roll == "exit":
                return print("Игра завершена!")
            elif players_turn == 2:
                player2_roll = roll
            elif player1_roll == "exit" or player2_roll == "exit":
                return print("Игра завершена!")


        if player1_roll == player2_roll:
            print("Ничья.\n")
        elif player1_roll > player2_roll:
            print("Победил игрок 1.\n")
        elif player2_roll > player1_roll:
            print("Победил игрок 2.\n")
