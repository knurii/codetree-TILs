n = int(input())
num_people = list(map(int, input().split()))
dist_lst = []

for i in range(len(num_people)):
    sum_dist = 0
    # for num in num_people:
    for j in range(len(num_people)):
        # sum_dist += num * i
        sum_dist += num_people[j] * abs(i - j)
    dist_lst.append(sum_dist)

print(min(dist_lst))