def solution(b):
    answer=0
    for i in range(len(b)):
        b[i] = b[i].replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ")
        b[i] = b[i].replace(" ", "")
        if not b[i]:
            answer+=1
    
    return answer