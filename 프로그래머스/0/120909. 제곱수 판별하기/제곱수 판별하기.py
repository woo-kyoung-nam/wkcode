def solution(n):
    answer = n ** 0.5     # 루트 = 0.5의 제곱
    if answer % 1 == 0:
        answer = 1
    else:
        answer = 2        
    return answer