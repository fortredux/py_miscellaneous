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
        return countdown(i-1)
        
    else:
        return print('Number must be positive')


countdown(n)
