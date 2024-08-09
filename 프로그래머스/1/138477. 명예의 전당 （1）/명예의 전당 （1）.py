def solution(k, score):
    answer = []
    temp = []
    for i in score:
        temp.append(i)
        temp = sorted(temp, reverse=True)
        answer.append(min(temp[:k:]))
    return answer