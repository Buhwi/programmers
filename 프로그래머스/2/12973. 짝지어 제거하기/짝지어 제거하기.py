def solution(s):
    if len(s)%2 == 1:
        return 0
    
    arr = []
    for i in range(len(s)):
        if not arr:
            arr.append(s[i])
            continue
        if arr[-1] == s[i]:
            arr.pop()
        else:
            arr.append(s[i])
        
    return 1 if not arr else 0