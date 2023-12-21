n = int(input())

def sum_div(n):
    sum = 0
    for i in range(1, n +  1):
        sum += i
    return sum // 10

print(sum_div(n))