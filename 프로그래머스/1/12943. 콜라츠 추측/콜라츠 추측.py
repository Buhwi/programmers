def solution(num):
    i = 0
    while True:
        if(i == 500):
            return -1
        if(num == 1):
            break
        elif (num%2) == 0:
            num = num / 2
        else :
            num = num * 3 + 1  
        i += 1
    return i