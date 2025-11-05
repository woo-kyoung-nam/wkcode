def solution(n):
    answer = 0
    a = list(str(n))
    a.sort(reverse=True)
    # for i in a:
    #     answer = i
    return int("".join(a))


# def solution(n):
#     a = list(str(n))
#     a.sort(reverse=True)

#     result = ""
#     for i in a:
#         result += i
        
#     return int(result)