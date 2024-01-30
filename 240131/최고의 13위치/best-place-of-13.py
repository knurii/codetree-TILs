n = int(input())
map_lst = []
for i in range(n):
    tmp = list(map(int, input().split()))
    map_lst.append(tmp)

max_cnt = 0
# 일단 세로는 N 다 돌고
for i in range(n):
    # 가로는 범위 벗어나면 안됨 3칸이면 N - 2
    for j in range(n - 2):
        # 1 x 3이니까.. 그럼 3 x 3은? 어떤 식이지?
        cnt = map_lst[i][j] + map_lst[i][j + 1] + map_lst[i][j + 2]
        max_cnt = max(max_cnt, cnt)

print(max_cnt)