def solution(n):
    i = 0
    while True:
        i += 1
        if i % 3 == 0:
            n+=1
        elif "3" in str(i):
            n+=1
        if(i == n):
            break
    return n