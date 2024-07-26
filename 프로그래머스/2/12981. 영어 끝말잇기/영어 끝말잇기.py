def solution(n, words):
    answer = []
    x = []
    
    for i in range(len(words)):
         #중복 제거
        if words[i] not in x:
            x.append(words[i])
        else:
            a = (i%n)+1
            return [a, (i//n)+1]
        
        #단어 처음과 끝을 비교
        start = (words[i])[0]
        if i == 0:
            end = start
        if start != end:
            a = (i%n)+1
            return [a, (i//n)+1]
        
        end = (words[i])[len(words[i])-1]
        
    
    
    return [0, 0] if not answer else answer