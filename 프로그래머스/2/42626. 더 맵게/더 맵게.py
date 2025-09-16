# SOL 1-1) 힙(heap) 자료구조 이용, try / except IndexError 이용
# 힙을 사용하는 이유 : 일반적인 리스트와 달리 push(), pop() 이후 자동 정렬
import heapq

def solution(scoville, K):
    answer = 0
    mix_scoville = 0
    heapq.heapify(scoville)         # 최초 리스트에서 힙 정렬
    
    while scoville[0] < K:          # 스코빌이 기준점 넘어가면 반복 종료
        if(len(scoville)<2):        # 스코빌 지수 하나 남았을 때 더 이상 불가하므로 -1 리턴
            return -1
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mix_scoville)           
        answer +=1                          
       # 그 외에는 스코빌 계산하면서 값 빼주고 나온값 push
        
    return answer