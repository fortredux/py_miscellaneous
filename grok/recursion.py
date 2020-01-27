

def countdown(i):
    while i > 0:
        print(i)
        return countdown(i-1)


countdown(16)

