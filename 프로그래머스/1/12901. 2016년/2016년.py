def solution(a, b):
    arr = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    sum = 0
    for i in range(1, a):
        if i%2 == 1:
            sum += 31
        if i%2 == 0:
            sum += 30
        
    if a > 2:
        sum -= 1
    if a == 9:
        sum += 1
    if a == 11:
        sum += 1
    return arr[(sum+b)%7]