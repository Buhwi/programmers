def solution(p, lim):
    answer = 0
    l = 0
    r = len(p)-1
    p = sorted(p)
    
    while l <= r:
        if l == r:
            answer += 1
            break
        if p[l] + p[r] <= lim:
            l += 1
        r -= 1
        answer += 1
    
        
    return answer