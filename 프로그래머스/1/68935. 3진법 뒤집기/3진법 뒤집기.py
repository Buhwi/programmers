def solution(n):
    array = []
    answer = 0
    
    while n > 0:
        array.append(n%3)
        n = n//3
        
    for i in range(1, len(array)+1):
        answer += array[i-1]*(3**(len(array)-i))
    return answer