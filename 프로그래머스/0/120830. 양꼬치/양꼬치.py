def solution(n, k):
    n12000 = n*12000
    k2000 = k*2000
    if n >= 10:
        free = n // 10      
        answer = n12000 + k2000 - (free*2000)
    else:
        answer = n12000 + k2000
    return answer