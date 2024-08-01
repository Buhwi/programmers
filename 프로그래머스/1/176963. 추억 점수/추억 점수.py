def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    for i in range(len(photo)):
        for j in photo[i]:
            if j in name:
                for k in range(len(name)):
                    if j == name[k]:
                        answer[i] += yearning[k]
    return answer