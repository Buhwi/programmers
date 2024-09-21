temp = input()

answer = 0
m = temp[0]

for i in list(temp):
    if i == m:
        continue
    else:
        m = i
        answer += 1
print(answer//2 if answer%2==0 else answer//2 + 1)