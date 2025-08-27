def solution(numbers):
    answer = sorted(numbers)
    
    num = answer[-2]*answer[-1]
    return num