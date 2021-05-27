# 정확성 테스트 1 / 3~7 / 9~13
# 효율성 1~5 .. ㅠㅠ

def solution(people, limit):
    answer = 0
    sorted_people = sorted(people,reverse=True)
    while sorted_people :
        if len(sorted_people) >= 2 :
            if sorted_people[0] + sorted_people[1] > limit :
                del sorted_people[0]
                answer+=1
            elif sorted_people[0] + sorted_people[1] <= limit :
                del sorted_people[0:2]
                answer+=1
        else :
            del sorted_people[0]
            answer+=1

    return answer

# =================================================================
# 재도전

from collections import deque

def solution(people, limit):
    answer = 0
    sorted_people = deque(sorted(people,reverse=True)) # 내림차순으로 정렬
    while sorted_people :
        if len(sorted_people) >= 2 : # 만약 list 에 element 가 2개 이상일 때 실행
            # 이 때 몸무게 가장 큰 사람 & 가장 작은 사람과 비교
            if sorted_people[0] + sorted_people[-1] > limit : # 만약 limit 값 보다 크다면 무게 많이 나가는 사람 pop
                sorted_people.popleft()
                answer+=1
            elif sorted_people[0] + sorted_people[-1] <= limit : # 만약 limit 값 보다 적거나 같다면 둘이 같이 pop
                sorted_people.popleft()
                sorted_people.pop() # deque 에서 가장 오른쪽에 있는 거 pop 시키는 방법 
                answer+=1
        else :
            sorted_people.popleft() # 만약 list 에 element 가 1개 일 경우 그냥 pop 시키기
            answer+=1
    return answer

# Key points
    # 단순히 몸무게가 많이 나가는 사람부터 채우면 되지 않을까 하는 생각부터 했다..
    # 몸무게 가장 많이 나가는 사람 + 몸무게 가장 적게 나가는 사람끼리 무게 합산 후 limit 값과 비교하는 방식으로 진행해야 함
        # 그러면 최대한 적은 보트 수를 구할 수 있음 
        # ex) 
        
        # people = [80,70,40,40,20,10,10,10]
        # limit = 100
        
            # 큰 것 부터 해결해나가면 구명보트 5개 필요 
            # 큰 것 & 작은 것 같이 해결해나가면 구명보트 4개 필요 (더 이득)
        
    # 또 중요한 점 
        # 일반 리스트에서 pop() 또는 del 함수를 썼을 때 효율성 테스트 통과 못 하는 것 같음 
            # 리스트 pop 시간복잡도 --> O(n)
            # deque popleft / pop 시간복잡도 --> O(1)
            
            # 알아두자!!
