def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-9):
        arr = discount[i:10+i:]
        for j in range(len(want)):
            if arr.count(want[j]) != number[j]:
                break
            if j == len(want)-1:
                answer+=1
    
    return answer