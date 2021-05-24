####################################### 1,6,7,9,13,23,24,25 실패 #######################################
from collections import Counter
from operator import itemgetter

def solution(N, stages):
    cnt = dict(Counter(sorted(stages)))
    all_stages = [i for i in range(1, max(stages)+1)]
    for i in all_stages:
        if i not in cnt.keys():
            cnt[i] = 0

    cnt = sorted(cnt.items())
    prob = {}
    user_challenge = len(stages)

    for i in cnt:
        prob[i] = i[1] / user_challenge
        user_challenge -= i[1]
    
    prob_sorted = (sorted(prob.items(), key=itemgetter(1), reverse=True))
    answer = []
    
    for i in prob_sorted:
        if i[0][0] <= N:
            answer.append(i[0][0])
    
    return answer


################################## 참고 답안 #######################################
# list.count() !!!!

def solution(N, stages):
    answer = {}
    challengers = len(stages) # 전체 인원 수
    for stage in range(1, N+1): # 문제 자체에 stages에는 1이상 N+1이하의 수가 담겨있다고 명시되어 있음
        if challengers != 0: # zero division error 예외처리
            stage_users_count = stages.count(stage) # list.count() 메소드를 사용해서 해당 스테이지에 머물러 있는 인원 합산
            answer[stage] = stage_users_count / challengers # 해당 스테이지에 머물러 있는 인원 / 해당 스테이지 이후까지의 인원 합
            challengers -= stage_users_count # 지나온 스테이지 인원들 빼줌
        else:
            answer[stage] = 0

    print(answer)    
    answer = sorted(answer, key=lambda x: answer[x], reverse=True)
    
    return answer
