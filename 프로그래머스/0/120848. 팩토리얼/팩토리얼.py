def solution(n):
    answer = 1
    num = 1
    while num*(answer+1) <= n:
        answer += 1
        num *= answer
    return answer