def solution(s):
    answer = []
    zero = 0
    i = 0
    
    while True:
        if s == "1":
            answer.append(i)
            answer.append(zero)
            break
        
        zero += s.count("0")
        s = str(bin(len(s.replace("0", "")))).replace("0b", "")
        i += 1
    return answer