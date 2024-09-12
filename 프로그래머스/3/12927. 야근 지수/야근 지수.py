import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)
    

    for _ in range(n):
        max_value = -heapq.heappop(max_heap)  
        max_value -= 1  
        heapq.heappush(max_heap, -max_value)  
    
    answer = 0
    
    for work in max_heap:
        answer += work*work
    return answer