# 정확성 100 / 효율성 0

def solution(people, limit):
    people.sort()
    cnt = 0

    while people:
        min_ = people[0]
        max_ = people[-1]

        if min_ + max_ <= limit:
            people = people[1:-1]
            cnt += 1
        else:
            people = people[:-1]
            cnt += 1
    return cnt
  
  # deque 활용후 성공
  
from collections import deque

def solution(people, limit):
    cnt = 0
    people = deque(sorted(people))

    while people:
        if len(people) < 2:
            cnt += 1
            break
        
        min_ = people[0]
        max_ = people[-1]
            
        if min_ + max_ <= limit:
            cnt += 1
            people.popleft()
            people.pop()
        else:
            cnt += 1
            people.pop()
            
    return cnt
