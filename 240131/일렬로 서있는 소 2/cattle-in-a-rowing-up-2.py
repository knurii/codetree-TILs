n = int(input())
cows_tall = list(map(int, input().split()))

# 조건문으로 풀지 말고, 모든 경우의 수 다 잡아보기
# for i in range(len(cows_tall) - 2):
#     if cows_tall[i] < min(cows_tall[i + 1:]):

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if cows_tall[i] <= cows_tall[j] and cows_tall[j] <= cows_tall[k]:
                cnt += 1

print(cnt)