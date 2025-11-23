def solution(num_list):
    plus = 0
    mul = 1
    
    for i in num_list:
        plus += i
        mul *= i
    if mul < plus**2:
        return 1
    else:
        return 0