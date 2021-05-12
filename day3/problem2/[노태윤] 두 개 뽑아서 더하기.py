from itertools import combinations

def solution(numbers):
    # combination 으로 모든 경우의 수가 담긴 list 반환
    # [(a,b),(a,c),(a,d),(b,c)...] 이런 식으로 되어 있음
    combi_list = list(combinations(numbers,2))
    
    # lambda 를 써서 안에 element 값들 더하기
    # 이 때 중복 값이 있을 수 있으므로 set 씌워주기
    # list 로 반환하고 오름차순으로 정열!
    answer = sorted(list(set(map(lambda x : x[0]+x[1],combi_list))))
    return answer
