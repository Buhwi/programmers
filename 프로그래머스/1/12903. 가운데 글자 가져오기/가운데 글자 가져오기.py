def solution(s):
    
    return s if len(s)==1 else s[int((len(s)-1)/2)] + (s[int((len(s)-1)/2)+1]*((len(s)-1)%2))