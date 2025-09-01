def solution(s):
    answer = []
    sp =  s.split()          # 구분자로 변환
    sp2 = list(map(int,sp))  # 리스트 내 문자열을 정수형으로 변환
    sp2min = str(min(sp2))
    sp2max = str(max(sp2))
    
    answer.append(sp2min)
    answer.append(sp2max)
    answer1 = " ".join(answer)  # 공백으로 구분
    return answer1

    # def solution(s):
#     answer = ''
#     sp = s.split()
#     for i in sp:
#         if i.min():
#             answer.append(i)
#         else i.max():
#             answer.append(i)
#     return answer

    # for i in sp2min:
    #     for j in sp2max:
    #         answer.append(i,j)


