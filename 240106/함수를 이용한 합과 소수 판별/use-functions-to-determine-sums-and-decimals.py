a, b = map(int, input().split())

def disc(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

def sum_even(i):
    to_i = str(i)
    sum_i = 0
    for j in range(len(to_i)):
        sum_i += int(to_i[j])
    if sum_i % 2 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b + 1):
    if disc(i) and sum_even(i):
        cnt += 1

print(cnt)