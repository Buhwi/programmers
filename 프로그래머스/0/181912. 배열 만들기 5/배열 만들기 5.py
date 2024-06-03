def solution(intStrs, k, s, l):
    answer = []
    
    for i in range(len(intStrs)):
        temp = intStrs[i][s:s+l]
        if(int(temp) > int(k)):
            answer.append(int(temp))
    return answer