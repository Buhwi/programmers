def solution(spell, dic):
    answer = 1
    for i in range(len(dic)):
        answer = 1
        for j in range(len(spell)):
            if spell[j] not in dic[i]:
                answer = 2
        if answer == 1:
            return answer
    return answer