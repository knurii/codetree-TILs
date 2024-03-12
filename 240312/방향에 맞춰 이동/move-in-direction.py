N = int(input())
loc = [0, 0]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(N):
    tmp = tuple(input().split())
    # print(f'이동 전 {loc}')
    if tmp[0] == 'W':
        loc[0] += dx[0] * int(tmp[1])
        loc[1] += dy[0] * int(tmp[1])
    elif tmp[0] == 'S':
        loc[0] += dx[1] * int(tmp[1])
        loc[1] += dy[1] * int(tmp[1])
    elif tmp[0] == 'N':
        loc[0] += dx[2] * int(tmp[1])
        loc[1] += dy[2] * int(tmp[1])
    elif tmp[0] == 'E':
        loc[0] += dx[3] * int(tmp[1])
        loc[1] += dy[3] * int(tmp[1])
    # print(f'이동 위치는 {loc}')

print(f'{loc[0]} {loc[1]}')

# W = -1, 0
# S = 0, -1
# N = 0, 1
# E = 1, 0