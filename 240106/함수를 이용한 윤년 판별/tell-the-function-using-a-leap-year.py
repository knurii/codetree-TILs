y = int(input())

def year_disc(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return print('true')
            return print('false')
        return print('true')
    return print('false')

year_disc(y)