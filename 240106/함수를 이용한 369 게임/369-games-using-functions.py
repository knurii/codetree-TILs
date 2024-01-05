a, b = map(int, input().split())

def mul_three(i):
    to_str = str(i)
    for s in to_str:
        if s == '3' or s == '6' or s =='9':
            return True
    return False

def game(i):
    to_str = str(i)
    sum_i = 0
    for i in range(len(to_str)):
        sum_i += int(to_str[i])
    if sum_i % 3 == 0:
        return True
    return False

cnt = 0
for i in range(a, b + 1):
    if mul_three(i) or game(i):
        cnt += 1

print(cnt)