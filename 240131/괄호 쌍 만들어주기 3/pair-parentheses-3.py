a_str = input()

result = 0

for i in range(len(a_str)):
    if a_str[i] == '(':
        for j in range(i + 1, len(a_str)):
            if a_str[j] == ')':
                result += 1

print(result)