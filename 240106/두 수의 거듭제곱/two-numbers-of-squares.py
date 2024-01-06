a, b = map(int, input().split())

def print_sqr(a, b):
    ans = 1
    for i in range(b):
        ans *= a
    return ans

print(print_sqr(a, b))