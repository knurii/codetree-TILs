n = int(input())

def is_five(n):
    n_sum = 0
    n = str(n)

    for i in n:
        n_sum += int(i)

    if n_sum % 5 == 0 and int(n) % 2 == 0:
        return print('Yes')
    else:
        return print('No')

is_five(n)