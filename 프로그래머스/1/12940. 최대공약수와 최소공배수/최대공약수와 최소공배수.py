def solution(n, m):
    answer = [n, m]
    temp1, temp2 = min(answer), max(answer)
    flag1, flag2 = True, True
    
    while flag1 or flag2:
        if n%temp1 == 0 and m%temp1 == 0:
            answer[0] = temp1
            flag1 = False
            
        if temp2%n == 0 and temp2%m == 0:
            answer[1] = temp2
            flag2 = False
        if flag1 == True:
            temp1 -= 1
        if flag2 == True:
            temp2 += 1
        
    return answer