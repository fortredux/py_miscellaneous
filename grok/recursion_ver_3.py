

def check(i):

    i = int(i)

    if i == 0:
        print('0')
        return False

    else:
        return True


def countdown(num):
    x = check(num)
    
    while x is True:
        num = int(num)
        print(num)
        return countdown(num-1)


countdown('15')
