
'''
def countdown(i):
    while i > 0:
        print(i)
        return countdown(i-1)
'''

def countdown(i):
    if i == 0:
        return print(0)
    else:
        print(i)
        countdown(i-1)


countdown(16)
