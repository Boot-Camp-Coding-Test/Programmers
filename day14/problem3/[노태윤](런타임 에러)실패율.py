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
