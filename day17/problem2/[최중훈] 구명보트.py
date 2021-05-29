from collections import deque

def solution(people, limit):
    cnt = 0
    people = sorted(people)
    deq = deque(people) # list를 사용해서 반복문 돌리면 실패하고, deque로 변환후 돌리면 효율성 통과됨
                        # list에서 pop(0)은 O(n)인 반면, deque.popleft()는 O(1)

    while deq:
        if len(deq) >= 2: # 남은 사람이 2명 이상
            light = deq[0]
            heavy = deq[-1]
            if light + heavy <= limit: # (제일 가벼운 사람+제일 무거운 사람)이 보트 제한 무게를 넘는지 확인
                deq.popleft()
                deq.pop()
                cnt += 1
            else: # (제일 가벼운 사람+제일 무거운 사람)이 제한무게를 넘으면 제일 무거운 사람만 태워서 내보냄.. 무거우면 빨리 살 수 있구나?^^
                deq.pop()
                cnt += 1 
                     
        else: # 남은 사람이 1명일 때
            cnt += 1
            break

    return cnt
