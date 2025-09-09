def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer





# def solution(people, limit):
#     answer = 0
#     answer2 = 0
#     for i in people:
#         for j in people:
#             if i+j <= 100:
#                 answer += 1
#         if i <= 100:
#             answer2 += 1
#     return answer + answer2