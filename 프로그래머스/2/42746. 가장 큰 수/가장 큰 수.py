def solution(numbers):
    answer = ''
    num_str = list(map(str,numbers))
    num_str.sort(key=lambda x:x*3, reverse=True)
    
    # result = ''.join(num_str)
    for i in num_str:
        answer += i
    
    return str(int(answer))



    # for i in numbers:
    #     answer += str(i)

# from itertools import permutations
# print(max(int(''.join(map(str, p))) for p in permutations(numbers)))

