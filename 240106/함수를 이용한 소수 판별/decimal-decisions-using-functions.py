a, b = map(int, input().split())

def is_dec(i):
    if i < 2:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

ans = 0
for i in range(a, b + 1):
    if is_dec(i) == True:
        ans += i

print(ans)