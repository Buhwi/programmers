def solution(s):
    answer = []
    
    for i in range(len(s)):
        indices = list(find(s[:i:], s[i]))
        answer.append(-1 if not indices else i - max(indices))
    
    return answer


def find(string, char):
    for i, c in enumerate(string):
        if c == char:
            yield i
