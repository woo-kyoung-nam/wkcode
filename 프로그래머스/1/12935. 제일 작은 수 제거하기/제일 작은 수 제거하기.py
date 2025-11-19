# def solution(arr):
#     answer = []
#     if len(arr) == 1:
#         answer.append(-1)
#     else:
#         answer = [x for x in arr if x != min(arr)]
#     return answer

def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr