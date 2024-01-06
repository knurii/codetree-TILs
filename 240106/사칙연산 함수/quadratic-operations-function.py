a, o, c = input().split()

def cal_int(a, o, c):
    a = int(a)
    c = int(c)
    
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '/':
         return int(a / c)
    elif o == '*':
        return a * c
    else:
        return False

ans = cal_int(a, o, c)

if ans == False:
    print('False')
else:
    print(f'{a} {o} {c} = {cal_int(a, o, c)}')