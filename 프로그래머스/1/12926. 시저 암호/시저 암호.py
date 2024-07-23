def solution(s, n):
    answer = ""
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            continue
        temp = ord(s[i])+n
        
        if temp-n <= 90 and temp >= 97:
            temp -= 26
        
        if temp > 122:
            temp = temp - 26
        elif 97 > temp and temp > 90:
            temp = temp - 26
        answer += chr(temp)
    return answer