from collections import Counter

def solution(N, stages):
    answer = []
    
    num_users = len(stages)
    counter = Counter(stages)
    for i in range(1,N+1) :
        counter[i] = counter.get(i,0)
    
    for i,j in sorted(counter.items()) :
        counter[i] = j / num_users
        num_users -= j
    
    if N+1 in counter :
        del counter[N+1]
    
    sorted_list = sorted(list(counter.items()))
    sorted_list = sorted(sorted_list,key=lambda x : x[1],reverse=True)
    answer = [x[0] for x in sorted_list]
    return answer

# =====================================================================
# 재도전

from collections import Counter

def solution(N, stages):
    num_users = len(stages) # 게임 유저 수
    counter = Counter(stages) # 카운터 활용
    for i in range(1,N+1) : 
        counter[i] = counter.get(i,0) # stages 리스트에 1부터 N 까지 없을 수도 있음 ==> 없는 거는 해당 stage를 key 로 , 해당 count 을 0 으로 
    
    for i,j in sorted(counter.items()) : # 1 라운드부터 올라가기 때문에 오름차순으로 정렬
        if j == 0 and num_users == 0 : # 유저 수가 0 명이고 count 도 0 일 때 실패율 0 으로 간주
            counter[i] = 0
        else :
            counter[i] = j / num_users # 실패율 공식
            num_users -= j # 총 유저수 - 스테이지에 도달했으나 클리어하지 못한 유저수 (반복 수행)
    
    if N+1 in counter :
        del counter[N+1] # N+1 스테이지는 필요없기 때문에 만약 포함하고 있다면 제거할 것
    
    # '문자열 내 마음대로 정렬하기' 문제랑 비슷 ==> 헷갈리면 해당 문제 풀이 참고할 것
    sorted_list = sorted(list(counter.items())) # 우선 전체적으로 오름차순으로 정렬
    sorted_list = sorted(sorted_list,key=lambda x : x[1],reverse=True) # 그 다음 실패율 기준으로 내림차순 정렬 
    answer = [x[0] for x in sorted_list] # 스테이지 리스트 반환
    return answer

# Key points
    # 유저 수가 0 명이고 count 도 0 일 때를 생각못했다..
    # 이 때 0/0 이 되버려서 오류가 발생한 듯
    
    # ex) Test Case 
        # N = 5
        # stages = [2,1,2,4,2,4,3,3]
        
        # 이 때 counter 는 [(1, 1), (2, 3), (3, 2), (4, 2), (5, 0)]
        # 실패율은         [  1/8,    3/7,    2/4,    2/2,    0/0 ] ==> 마지막이 0/0이 됨 ==> 예외처리 해주면 됌 ==> 실패율 0 으로 간주
