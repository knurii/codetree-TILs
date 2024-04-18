n, m = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
visited = [
    [0 for _ in range(n)]
    for _ in range(m)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or graph[x][y] == 0:
        return False
    return True

def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n - 1][m - 1])


# ---
# n, M = map(int, input().split())
# graph = [[] for _ in range(n + 1)]

# visited = [False for _ in range(n + 1)]
# vertex_cnt = 0

# for i in range(M):
#     v1, v2 = tuple(map(int, input().split()))
#     graph[v1].append(v2)
#     graph[v2].append(v1)

# def dfs(vertex):
#     global vertex_cnt
#     for curr_v in graph[vertex]:
#         if not visited[curr_v]:
#             visited[curr_v] = True
#             vertex_cnt += 1
#             dfs(curr_v)

# visited[1] = True
# dfs(1)

# print(vertex_cnt)