def solution(n):
    answer = 0
    
    for j in range(n):
        temp = 0
        for k in range(j, n):
            temp += k+1
            if temp == n:
                answer+=1
                break
            elif temp > n:
                break
    
    return answer