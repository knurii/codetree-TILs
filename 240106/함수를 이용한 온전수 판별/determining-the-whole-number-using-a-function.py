a, b = map(int, input().split())

def cal_int(i):
    if i % 2 == 0 or str(i)[-1] == '5':
        return False
    if i % 3 == 0 and i % 9 != 0:
        return False
    return True

def cnt_int(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if cal_int(i):
            cnt += 1
    return cnt

print(cnt_int(a, b))