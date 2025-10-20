def solution(n):
    answer = 0
    n_split=list(str(n))
    for i in n_split:
        answer += int(i)
    
    return answer