prompts = input()
x, y = 0, 0
curr_dir = 3

# 동, 남, 서, 북
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

for prompt in prompts:
    if prompt == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4
    elif prompt == 'R':
        curr_dir = (curr_dir + 1) % 4
    elif prompt == 'F':
        x, y = x + dxs[curr_dir], y + dys[curr_dir]

print(x, y)