from time import sleep

"""
n = input('Enter number in range from 1 to 9: ')


def countdown(i):
    try:
        i = int(i)
    except ValueError:
        return print('You should have entered number')

    if i == 0:
        return print(0)
        
    if i > 9:
        return print('Number must be less than 10')

    if i > 0:
        print(i)
        sleep(1)
        return countdown(i-1)

    else:
        return print('Number must be positive')
"""

n = input('Enter number in range from 1 to 15: ')


def countdown(i):
    check = False

    while check == False:
        try:
            i = int(i)
            if i == 0:
                return print(0)
            elif i > 15:
                i = input('Number must be less than 16. Try again: ')
            elif i < 16:
                check = True

        except ValueError:
            i = input('You should have entered number in range from 1 to 15: ')

    if i > 0:
        print(i)
        sleep(0.1)
        return countdown(i-1)

    else:
        return print('Number must be positive')


countdown(n)
