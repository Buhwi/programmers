def solution(brown, yellow):
    div = []
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            div.append(i)
    
    k = len(div)-1
    for j in range(int((len(div)-0.5)/2)+1):
        if ((div[j] + div[k] + 2)*2) == brown:
            answer.append(div[k]+2)
            answer.append(div[j]+2)
        k -= 1
    return answer